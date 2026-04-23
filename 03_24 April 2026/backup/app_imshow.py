import cv2
import numpy as np
import time
import subprocess

cap = cv2.VideoCapture(0, cv2.CAP_AVFOUNDATION)

if not cap.isOpened():
    print("Error: kamera tidak ditemukan")
    exit()

width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  // 2
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
fps    = cap.get(cv2.CAP_PROP_FPS) or 30.0

print(f"Resolusi: {width}x{height} @ {fps:.0f} FPS")
print("Tekan 'r' untuk mulai/stop rekam | 's' untuk screenshot | 'q' untuk keluar")

ffmpeg_proc = None
recording   = False

HIST_W, HIST_H = 512, 200
CHANNELS = [(0, (255, 80,  80),  "B"),
            (1, (80,  200, 80),  "G"),
            (2, (80,  80,  255), "R")]

def draw_stat_histogram(frame):
    img = np.zeros((HIST_H, HIST_W, 3), dtype=np.uint8)
    for ch, color, label in CHANNELS:
        hist = cv2.calcHist([frame], [ch], None, [256], [0, 256])
        cv2.normalize(hist, hist, 0, HIST_H - 30, cv2.NORM_MINMAX)
        for x in range(256):
            h = int(hist[x])
            x0 = x * HIST_W // 256
            x1 = (x + 1) * HIST_W // 256
            cv2.rectangle(img, (x0, HIST_H - h), (x1, HIST_H),
                          [c // 3 for c in color], -1)

        mean, std = cv2.meanStdDev(frame[:, :, ch])
        m, s = mean[0, 0], std[0, 0]
        mx  = int(m * HIST_W / 256)
        sx0 = int(max(0, m - s) * HIST_W / 256)
        sx1 = int(min(255, m + s) * HIST_W / 256)

        # Rentang mean ± std
        cv2.rectangle(img, (sx0, 0), (sx1, HIST_H - 30),
                      [c // 5 for c in color], -1)
        # Garis mean
        cv2.line(img, (mx, 0), (mx, HIST_H - 30), color, 2)
        # Label
        cv2.putText(img, f"{label} u={m:.0f} s={s:.0f}",
                    (sx0 + 2, HIST_H - 30 + 14 + CHANNELS.index((ch, color, label)) * 14),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.4, color, 1)

    return img

while True:
    ret, frame = cap.read()
    if not ret:
        print("Error: gagal membaca frame dari kamera")
        break

    frame = cv2.resize(frame, (width, height))

    if recording and ffmpeg_proc is not None:
        ffmpeg_proc.stdin.write(frame.tobytes())

    display = frame.copy()

    cv2.imshow("Statistik BGR", draw_stat_histogram(frame))

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
            filename = f"rekaman_{int(time.time())}.mp4"
            try:
                ffmpeg_proc = subprocess.Popen(
                    [
                        "ffmpeg", "-y",
                        "-f", "rawvideo",
                        "-vcodec", "rawvideo",
                        "-pix_fmt", "bgr24",
                        "-s", f"{width}x{height}",
                        "-r", str(fps),
                        "-i", "pipe:0",
                        "-c:v", "libx264",
                        "-pix_fmt", "yuv420p",
                        "-preset", "fast",
                        filename,
                    ],
                    stdin=subprocess.PIPE,
                    stderr=subprocess.DEVNULL,
                )
                recording = True
                print(f"Rekaman dimulai: {filename}")
            except FileNotFoundError:
                print("Error: ffmpeg tidak ditemukan — install dengan 'brew install ffmpeg'")
        else:
            recording = False
            ffmpeg_proc.stdin.close()
            ffmpeg_proc.wait()
            ffmpeg_proc = None
            print("Rekaman dihentikan dan disimpan.")

if recording and ffmpeg_proc is not None:
    ffmpeg_proc.stdin.close()
    ffmpeg_proc.wait()

cap.release()
cv2.destroyAllWindows()
