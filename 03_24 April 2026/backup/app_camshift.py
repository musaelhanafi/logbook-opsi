import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

print("Klik dan drag untuk pilih target | 'r' reset | 'q' keluar")

roi_start    = None
roi_end      = None
drawing      = False
needs_init   = False   # flag: hitung histogram setelah LBUTTONUP
tracking     = False
track_window = None
roi_hist     = None

def on_mouse(event, x, y, flags, param):
    global roi_start, roi_end, drawing, tracking, needs_init
    if event == cv2.EVENT_LBUTTONDOWN:
        roi_start  = (x, y)
        roi_end    = (x, y)
        drawing    = True
        tracking   = False
        needs_init = False
    elif event == cv2.EVENT_MOUSEMOVE and drawing:
        roi_end = (x, y)
    elif event == cv2.EVENT_LBUTTONUP:
        roi_end    = (x, y)
        drawing    = False
        needs_init = True   # sinyal ke main loop untuk init sekali

cv2.namedWindow("CamShift Tracker")
cv2.setMouseCallback("CamShift Tracker", on_mouse)

criteria = (cv2.TERM_CRITERIA_EPS | cv2.TERM_CRITERIA_COUNT, 10, 1)
HSV_LOW  = np.array([0,  60,  32])
HSV_HIGH = np.array([180, 255, 255])

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: gagal membaca frame dari kamera")
        break

    frame   = cv2.resize(frame, None, fx=0.5, fy=0.5)
    hsv     = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    display = frame.copy()

    # Gambar kotak seleksi saat drag
    if drawing and roi_start and roi_end:
        cv2.rectangle(display, roi_start, roi_end, (0, 255, 0), 2)

    # Inisialisasi tracking — hanya terpicu sekali per seleksi
    if needs_init:
        needs_init = False
        x1 = min(roi_start[0], roi_end[0])
        y1 = min(roi_start[1], roi_end[1])
        x2 = max(roi_start[0], roi_end[0])
        y2 = max(roi_start[1], roi_end[1])

        if x2 > x1 and y2 > y1:
            roi_hsv  = hsv[y1:y2, x1:x2]
            mask     = cv2.inRange(roi_hsv, HSV_LOW, HSV_HIGH)
            roi_hist = cv2.calcHist([roi_hsv], [0], mask, [180], [0, 180])
            cv2.normalize(roi_hist, roi_hist, 0, 255, cv2.NORM_MINMAX)
            track_window = (x1, y1, x2 - x1, y2 - y1)
            tracking = True
        # skip CamShift frame ini — biarkan backproj stabil dulu
        cv2.imshow("CamShift Tracker", display)
        cv2.waitKey(1)
        continue

    # CamShift tracking
    if tracking and roi_hist is not None:
        fh, fw   = frame.shape[:2]
        mask     = cv2.inRange(hsv, HSV_LOW, HSV_HIGH)
        backproj = cv2.calcBackProject([hsv], [0], roi_hist, [0, 180], 1)
        backproj &= mask

        # Clamp track_window ke batas frame sebelum CamShift
        x, y, w, h = track_window
        x = int(max(0, min(x, fw - 2)))
        y = int(max(0, min(y, fh - 2)))
        w = int(max(2, min(w, fw - x)))
        h = int(max(2, min(h, fh - y)))
        track_window = (x, y, w, h)

        ret_cs, track_window = cv2.CamShift(backproj, track_window, criteria)

        pts = np.intp(cv2.boxPoints(ret_cs))
        cv2.polylines(display, [pts], True, (0, 255, 0), 2)

        cx, cy = int(ret_cs[0][0]), int(ret_cs[0][1])
        cv2.circle(display, (cx, cy), 5, (0, 0, 255), -1)

        tw, th = int(ret_cs[1][0]), int(ret_cs[1][1])
        cv2.putText(display, f"cx={cx} cy={cy}  {tw}x{th}px",
                    (10, display.shape[0] - 10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.45, (0, 255, 0), 1)

        cv2.imshow("Back Projection", backproj)

    cv2.imshow("CamShift Tracker", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('r'):
        roi_start    = roi_end = None
        drawing      = False
        needs_init   = False
        tracking     = False
        track_window = None
        roi_hist     = None
        cv2.destroyWindow("Back Projection")

cap.release()
cv2.destroyAllWindows()
