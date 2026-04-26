import cv2
import numpy as np
import threading
import queue
from collections import deque

# --- key handler di background thread ---
_key_queue   = queue.Queue()
_lock_event  = threading.Event()
_reset_event = threading.Event()
_quit_event  = threading.Event()

def _key_handler():
    while True:
        key = _key_queue.get()
        if key == ord('l'):
            _lock_event.set()
        elif key == ord('r'):
            _reset_event.set()
        elif key == ord('q'):
            _quit_event.set()
            break

threading.Thread(target=_key_handler, daemon=True).start()

# --- moving average buffers (window = 20 frame) ---
MA_LEN  = 20
_ma_buf = {ch: deque(maxlen=MA_LEN) for ch in ('H', 'S', 'V', 'B', 'G', 'R')}

def _ma(ch, val):
    _ma_buf[ch].append(val)
    return sum(_ma_buf[ch]) / len(_ma_buf[ch])

def _reset_ma():
    for d in _ma_buf.values():
        d.clear()

# --------------------------------------------------

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

print("Klik dan drag untuk pilih region | 'l' lock/unlock | 'r' reset | 'q' keluar")

roi_start = None
roi_end   = None
drawing   = False
locked    = False

def on_mouse(event, x, y, _flags, _param):
    global roi_start, roi_end, drawing
    if locked:
        return
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_start = (x, y)
        roi_end   = (x, y)
        drawing   = True
        _reset_ma()
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        roi_end = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        roi_end = (x, y)
        drawing = False

cv2.namedWindow("Kamera")
cv2.setMouseCallback("Kamera", on_mouse)

HIST_W = 540
HIST_H = 200
BGR_CHANNELS = [(0, (255, 80,  80),  "B"),
                (1, (80,  200, 80),  "G"),
                (2, (80,  80,  255), "R")]
HSV_CHANNELS = [(1, (80,  200, 200), "S"),
                (2, (200, 200, 200), "V")]

def draw_hsv_histogram(roi_hsv):
    panels = []

    # Panel H — per-bin hue color, range 0–179
    img   = np.zeros((HIST_H, HIST_W, 3), dtype=np.uint8)
    hist  = cv2.calcHist([roi_hsv], [0], None, [180], [0, 180])
    cv2.normalize(hist, hist, 0, HIST_H - 40, cv2.NORM_MINMAX)
    bin_w = HIST_W // 180
    for i in range(180):
        h         = int(hist[i])
        color_bgr = cv2.cvtColor(np.uint8([[[i, 255, 200]]]), cv2.COLOR_HSV2BGR)[0][0].tolist()
        cv2.rectangle(img, (i * bin_w, HIST_H - 40 - h), ((i + 1) * bin_w, HIST_H - 40), color_bgr, -1)

    mean, std = cv2.meanStdDev(roi_hsv[:, :, 0])
    m, s  = mean[0, 0], std[0, 0]
    ma_m  = _ma('H', m)
    mx    = int(m    * HIST_W / 180)
    mxma  = int(ma_m * HIST_W / 180)
    sx0   = int(max(0,   ma_m - s) * HIST_W / 180)
    sx1   = int(min(179, ma_m + s) * HIST_W / 180)

    cv2.line(img, (mx,   0), (mx,   HIST_H - 40), (100, 100, 100), 1)   # raw: tipis abu
    cv2.line(img, (mxma, 0), (mxma, HIST_H - 40), (255, 255, 255), 2)   # MA: tebal putih
    lx = mxma + 3 if mxma < HIST_W - 40 else mxma - 40
    cv2.putText(img, f"{ma_m:.1f}", (lx, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)
    cv2.putText(img, f"{ma_m-s:.1f}", (max(0, sx0 - 2), 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
    cv2.putText(img, f"{ma_m+s:.1f}", (min(HIST_W - 35, sx1 + 2), 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
    for i in range(0, 181, 30):
        x = i * bin_w
        cv2.line(img, (x, HIST_H - 45), (x, HIST_H - 40), (180, 180, 180), 1)
        cv2.putText(img, str(i), (x + 2, HIST_H - 27), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (200, 200, 200), 1)
    cv2.putText(img, f"H  ma={ma_m:.1f}  raw={m:.1f}  std={s:.1f}", (10, HIST_H - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
    panels.append(img)

    # Panel S dan V — struktur sama dengan BGR
    for ch, color, label in HSV_CHANNELS:
        img  = np.zeros((HIST_H, HIST_W, 3), dtype=np.uint8)
        hist = cv2.calcHist([roi_hsv], [ch], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, HIST_H - 40, cv2.NORM_MINMAX)
        for i in range(256):
            h  = int(hist[i])
            x0 = i * HIST_W // 256
            x1 = (i + 1) * HIST_W // 256
            cv2.rectangle(img, (x0, HIST_H - 40 - h), (x1, HIST_H - 40), [c // 3 for c in color], -1)

        mean, std = cv2.meanStdDev(roi_hsv[:, :, ch])
        m, s  = mean[0, 0], std[0, 0]
        ma_m  = _ma(label, m)
        mx    = int(m    * HIST_W / 256)
        mxma  = int(ma_m * HIST_W / 256)
        sx0   = int(max(0,   ma_m - s) * HIST_W / 256)
        sx1   = int(min(255, ma_m + s) * HIST_W / 256)

        cv2.line(img, (mx,   0), (mx,   HIST_H - 40), (80, 80, 80), 1)   # raw: tipis abu
        cv2.line(img, (mxma, 0), (mxma, HIST_H - 40), color, 2)           # MA: tebal
        lx = mxma + 3 if mxma < HIST_W - 40 else mxma - 40
        cv2.putText(img, f"{ma_m:.1f}", (lx, 14), cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
        cv2.putText(img, f"{ma_m-s:.1f}", (max(0, sx0 - 2), 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
        cv2.putText(img, f"{ma_m+s:.1f}", (min(HIST_W - 35, sx1 + 2), 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
        for i in range(0, 257, 64):
            x = i * HIST_W // 256
            cv2.line(img, (x, HIST_H - 45), (x, HIST_H - 40), (140, 140, 140), 1)
            cv2.putText(img, str(i), (x + 2, HIST_H - 27), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (160, 160, 160), 1)
        cv2.putText(img, f"{label}  ma={ma_m:.1f}  raw={m:.1f}  std={s:.1f}", (10, HIST_H - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)
        panels.append(img)

    return np.vstack(panels)

def draw_bgr_histogram(roi_bgr):
    panel_h = HIST_H
    panels  = []

    for ch, color, label in BGR_CHANNELS:
        img = np.zeros((panel_h, HIST_W, 3), dtype=np.uint8)

        hist = cv2.calcHist([roi_bgr], [ch], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, panel_h - 40, cv2.NORM_MINMAX)

        for i in range(256):
            h  = int(hist[i])
            x0 = i * HIST_W // 256
            x1 = (i + 1) * HIST_W // 256
            cv2.rectangle(img, (x0, panel_h - 40 - h), (x1, panel_h - 40),
                          [c // 3 for c in color], -1)

        mean, std = cv2.meanStdDev(roi_bgr[:, :, ch])
        m, s  = mean[0, 0], std[0, 0]
        ma_m  = _ma(label, m)
        mx    = int(m    * HIST_W / 256)
        mxma  = int(ma_m * HIST_W / 256)
        sx0   = int(max(0,   ma_m - s) * HIST_W / 256)
        sx1   = int(min(255, ma_m + s) * HIST_W / 256)

        cv2.line(img, (mx,   0), (mx,   panel_h - 40), (80, 80, 80), 1)  # raw: tipis abu
        cv2.line(img, (mxma, 0), (mxma, panel_h - 40), color, 2)          # MA: tebal

        lx = mxma + 3 if mxma < HIST_W - 40 else mxma - 40
        cv2.putText(img, f"{ma_m:.1f}", (lx, 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)
        cv2.putText(img, f"{ma_m-s:.1f}", (max(0, sx0 - 2), 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
        cv2.putText(img, f"{ma_m+s:.1f}", (min(HIST_W - 35, sx1 + 2), 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)

        for i in range(0, 257, 64):
            x = i * HIST_W // 256
            cv2.line(img, (x, panel_h - 45), (x, panel_h - 40), (140, 140, 140), 1)
            cv2.putText(img, str(i), (x + 2, panel_h - 27),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (160, 160, 160), 1)

        cv2.putText(img, f"{label}  ma={ma_m:.1f}  raw={m:.1f}  std={s:.1f}",
                    (10, panel_h - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 1)

        panels.append(img)

    return np.vstack(panels)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: gagal membaca frame dari kamera")
        break

    hsv     = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    display = cv2.resize(frame, None, fx=0.5, fy=0.5)

    if roi_start and roi_end:
        rect_color = (0, 200, 255) if locked else (0, 255, 0)
        cv2.rectangle(display, roi_start, roi_end, rect_color, 2)

        if locked:
            cv2.putText(display, "LOCKED", (roi_start[0] + 4, roi_start[1] - 6),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 200, 255), 1)

        # Koordinat pada frame full-res (display = 50%)
        x1 = min(roi_start[0], roi_end[0]) * 2
        y1 = min(roi_start[1], roi_end[1]) * 2
        x2 = max(roi_start[0], roi_end[0]) * 2
        y2 = max(roi_start[1], roi_end[1]) * 2

        if x2 > x1 and y2 > y1:
            roi_bgr = frame[y1:y2, x1:x2]
            roi_hsv = hsv[y1:y2, x1:x2]
            cv2.imshow("Histogram HSV", draw_hsv_histogram(roi_hsv))
            cv2.imshow("Histogram BGR", draw_bgr_histogram(roi_bgr))

    cv2.imshow("Kamera", display)
    key = cv2.waitKey(1) & 0xFF
    if key != 0xFF:
        _key_queue.put(key)

    if _quit_event.is_set():
        break

    if _lock_event.is_set():
        _lock_event.clear()
        if roi_start and roi_end:
            locked = not locked
            print("ROI dikunci." if locked else "ROI dibuka.")

    if _reset_event.is_set():
        _reset_event.clear()
        roi_start = roi_end = None
        locked = False
        _reset_ma()

cap.release()
cv2.destroyAllWindows()
