import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

print("Klik dan drag untuk pilih region | 'r' reset | 'q' keluar")

roi_start = None
roi_end   = None
drawing   = False

def on_mouse(event, x, y, flags, param):
    global roi_start, roi_end, drawing
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_start = (x, y)
        roi_end   = (x, y)
        drawing   = True
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

def draw_hue_histogram(roi_hsv):
    hist_img = np.zeros((HIST_H, HIST_W, 3), dtype=np.uint8)

    hist = cv2.calcHist([roi_hsv], [0], None, [180], [0, 180])
    cv2.normalize(hist, hist, 0, HIST_H - 40, cv2.NORM_MINMAX)

    bin_w = HIST_W // 180
    for i in range(180):
        h = int(hist[i])
        color_hsv = np.uint8([[[i, 255, 200]]])
        color_bgr = cv2.cvtColor(color_hsv, cv2.COLOR_HSV2BGR)[0][0].tolist()
        cv2.rectangle(hist_img,
                      (i * bin_w, HIST_H - 40 - h),
                      ((i + 1) * bin_w, HIST_H - 40),
                      color_bgr, -1)

    # Mean dan std dev channel Hue
    mean, std = cv2.meanStdDev(roi_hsv[:, :, 0])
    m, s = mean[0, 0], std[0, 0]

    mx  = int(m * HIST_W / 180)
    sx0 = int(max(0, m - s) * HIST_W / 180)
    sx1 = int(min(179, m + s) * HIST_W / 180)

    # Area mean ± std
    cv2.rectangle(hist_img, (sx0, 0), (sx1, HIST_H - 40), (60, 60, 60), -1)
    # Garis mean
    cv2.line(hist_img, (mx, 0), (mx, HIST_H - 40), (255, 255, 255), 2)

    # Angka mean di atas garis mean
    mean_label = f"{m:.1f}"
    lx = mx + 3 if mx < HIST_W - 40 else mx - 35
    cv2.putText(hist_img, mean_label, (lx, 14),
                cv2.FONT_HERSHEY_SIMPLEX, 0.45, (255, 255, 255), 1)

    # Angka batas std (mean-std dan mean+std)
    cv2.putText(hist_img, f"{m-s:.1f}", (max(0, sx0 - 2), 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
    cv2.putText(hist_img, f"{m+s:.1f}", (min(HIST_W - 35, sx1 + 2), 30),
                cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)

    # Label sumbu x setiap 30 hue
    for i in range(0, 181, 30):
        x = i * bin_w
        cv2.line(hist_img, (x, HIST_H - 45), (x, HIST_H - 40), (180, 180, 180), 1)
        cv2.putText(hist_img, str(i), (x + 2, HIST_H - 27),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.35, (200, 200, 200), 1)

    # Hue dominan, mean, std
    peak_hue = int(np.argmax(hist))
    cv2.putText(hist_img, f"dominan={peak_hue}  mean={m:.1f}  std={s:.1f}",
                (10, HIST_H - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)

    return hist_img

def draw_bgr_histogram(roi_bgr):
    panel_h = HIST_H
    panels  = []

    for ch, color, label in BGR_CHANNELS:
        img = np.zeros((panel_h, HIST_W, 3), dtype=np.uint8)

        hist = cv2.calcHist([roi_bgr], [ch], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, panel_h - 40, cv2.NORM_MINMAX)

        bin_w = HIST_W // 256
        for i in range(256):
            h = int(hist[i])
            x0 = i * HIST_W // 256
            x1 = (i + 1) * HIST_W // 256
            cv2.rectangle(img, (x0, panel_h - 40 - h), (x1, panel_h - 40),
                          [c // 3 for c in color], -1)

        mean, std = cv2.meanStdDev(roi_bgr[:, :, ch])
        m, s = mean[0, 0], std[0, 0]

        mx  = int(m * HIST_W / 256)
        sx0 = int(max(0,   m - s) * HIST_W / 256)
        sx1 = int(min(255, m + s) * HIST_W / 256)

        # Area mean ± std
        cv2.rectangle(img, (sx0, 0), (sx1, panel_h - 40), (50, 50, 50), -1)
        # Garis mean
        cv2.line(img, (mx, 0), (mx, panel_h - 40), color, 2)

        # Angka mean di atas garis
        lx = mx + 3 if mx < HIST_W - 40 else mx - 35
        cv2.putText(img, f"{m:.1f}", (lx, 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, color, 1)

        # Batas std
        cv2.putText(img, f"{m-s:.1f}", (max(0, sx0 - 2), 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)
        cv2.putText(img, f"{m+s:.1f}", (min(HIST_W - 35, sx1 + 2), 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, (160, 160, 160), 1)

        # Label sumbu x setiap 64 nilai
        for i in range(0, 257, 64):
            x = i * HIST_W // 256
            cv2.line(img, (x, panel_h - 45), (x, panel_h - 40), (140, 140, 140), 1)
            cv2.putText(img, str(i), (x + 2, panel_h - 27),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.35, (160, 160, 160), 1)

        # Label channel + ringkasan
        cv2.putText(img, f"{label}  mean={m:.1f}  std={s:.1f}",
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
        cv2.rectangle(display, roi_start, roi_end, (0, 255, 0), 2)

        # Koordinat pada frame full-res (display = 50%)
        x1 = min(roi_start[0], roi_end[0]) * 2
        y1 = min(roi_start[1], roi_end[1]) * 2
        x2 = max(roi_start[0], roi_end[0]) * 2
        y2 = max(roi_start[1], roi_end[1]) * 2

        if x2 > x1 and y2 > y1:
            roi_bgr = frame[y1:y2, x1:x2]
            roi_hsv = hsv[y1:y2, x1:x2]
            cv2.imshow("Histogram Hue", draw_hue_histogram(roi_hsv))
            cv2.imshow("Histogram BGR", draw_bgr_histogram(roi_bgr))

    cv2.imshow("Kamera", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        roi_start = roi_end = None

cap.release()
cv2.destroyAllWindows()
