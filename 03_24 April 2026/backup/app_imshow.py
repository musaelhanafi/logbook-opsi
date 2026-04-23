import cv2
import time

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  // 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
fps    = cap.get(cv2.CAP_PROP_FPS) or 30.0

print(f"Resolusi: {width}x{height} @ {fps:.0f} FPS")
print("Tekan 'r' untuk mulai/stop rekam | 's' untuk screenshot | 'q' untuk keluar")

writer    = None
recording = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: gagal membaca frame dari kamera")
        break

    frame = cv2.resize(frame, (width, height))

    if recording and writer is not None:
        writer.write(frame)

    display = frame.copy()

    if recording:
        cv2.circle(display, (20, 20), 8, (0, 0, 255), -1)
        cv2.putText(display, "REC", (35, 27),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

    cv2.imshow("Kamera", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('s'):
        filename = f"screenshot_{int(time.time())}.png"
        cv2.imwrite(filename, frame)
        print(f"Screenshot disimpan: {filename}")
    elif key == ord('r'):
        if not recording:
            filename = f"rekaman_{int(time.time())}.avi"
            writer = cv2.VideoWriter(
                filename,
                cv2.VideoWriter_fourcc(*"MJPG"),
                fps,
                (width, height),
            )
            recording = True
            print(f"Rekaman dimulai: {filename}")
        else:
            recording = False
            writer.release()
            writer = None
            print("Rekaman dihentikan dan disimpan.")

if recording and writer is not None:
    writer.release()

cap.release()
cv2.destroyAllWindows()
