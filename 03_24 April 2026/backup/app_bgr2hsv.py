import cv2
import numpy as np

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

print("Tekan 'q' untuk keluar")

def half(img):
    return cv2.resize(img, None, fx=0.5, fy=0.5)

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: gagal membaca frame dari kamera")
        break

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    h, s, v = cv2.split(hsv)

    vis_top = np.hstack([frame, hsv])
    vis_mid = frame
    vis_bot = np.hstack([
        cv2.cvtColor(h, cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(s, cv2.COLOR_GRAY2BGR),
        cv2.cvtColor(v, cv2.COLOR_GRAY2BGR),
    ])

    # Label kolom di vis_top
    fw = frame.shape[1]
    cv2.putText(vis_top, "BGR", (10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
    cv2.putText(vis_top, "HSV", (fw + 10, 25), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Label kolom di vis_mid dan vis_bot
    for img, labels in [(vis_bot, ["H", "S", "V"])]:
        for i, label in enumerate(labels):
            cv2.putText(img, label, (i * fw + 10, 25),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)

    # Nilai piksel di titik tengah frame
    cy, cx = frame.shape[0] // 2, frame.shape[1] // 2
    bgr_val = frame[cy, cx]
    hsv_val = hsv[cy, cx]
    info = f"Pusat — BGR:{bgr_val.tolist()}  HSV:{hsv_val.tolist()}"
    cv2.putText(vis_top, info, (10, vis_top.shape[0] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)

    cv2.imshow("BGR | HSV", half(vis_top))
    cv2.imshow("BGR", half(vis_mid))
    cv2.imshow("H | S | V", half(vis_bot))

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
