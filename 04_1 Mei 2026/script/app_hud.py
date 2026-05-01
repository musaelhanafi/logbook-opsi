"""app_hud.py — Feed kamera + overlay HUD dari MAVLink.

Membaca frame kamera secara real-time dan menampilkan HUD attitude (pitch
ladder, roll, yaw compass, koordinat GPS) yang datanya diambil dari pesan
MAVLink ATTITUDE dan GLOBAL_POSITION_INT.

Penggunaan
----------
    python app_hud.py                          # kamera 0, UDP 14550
    python app_hud.py --connection udp:0.0.0.0:14550
    python app_hud.py --connection /dev/ttyUSB0 --baud 57600
    python app_hud.py --camera 1
    python app_hud.py --res 640 480            # set resolusi akuisisi kamera
    python app_hud.py --crop 0,0,640,480       # crop frame ke region x,y,w,h

Kontrol
-------
    q  — keluar
    s  — screenshot
    h  — toggle HUD on/off
"""

import argparse
import math
import sys
import os
import threading
import time

import cv2

# ── Import HudDisplay dari drone-seeker -----------------------------------
_HERE   = os.path.dirname(os.path.abspath(__file__))
_SEEKER = os.path.normpath(os.path.join(_HERE, "..", "..", "..", "drone-seeker"))
if _SEEKER not in sys.path:
    sys.path.insert(0, _SEEKER)

from hud_display import HudDisplay
from pymavlink import mavutil


# ── MAVLink poller (thread terpisah) --------------------------------------

class MavState:
    def __init__(self):
        self.roll_deg  = 0.0
        self.pitch_deg = 0.0
        self.yaw_deg   = 0.0
        self.lat       = 0.0
        self.lon       = 0.0
        self._lock     = threading.Lock()

    def update_attitude(self, msg):
        with self._lock:
            self.roll_deg  = math.degrees(msg.roll)
            self.pitch_deg = math.degrees(msg.pitch)
            self.yaw_deg   = math.degrees(msg.yaw) % 360

    def update_position(self, msg):
        with self._lock:
            self.lat = msg.lat * 1e-7
            self.lon = msg.lon * 1e-7

    def snapshot(self):
        with self._lock:
            return (self.roll_deg, self.pitch_deg,
                    self.yaw_deg, self.lat, self.lon)


def mavlink_thread(connection_string: str, baud: int, state: MavState,
                   stop_event: threading.Event):
    print(f"[MAV] Menghubungkan ke {connection_string} ...")
    try:
        master = mavutil.mavlink_connection(connection_string, baud=baud)
        master.wait_heartbeat(timeout=10)
        print(f"[MAV] Heartbeat diterima "
              f"(sys={master.target_system} comp={master.target_component})")

        # Minta stream ATTITUDE @ 25 Hz dan GLOBAL_POSITION_INT @ 5 Hz
        master.mav.request_data_stream_send(
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_EXTRA1, 25, 1,
        )
        master.mav.request_data_stream_send(
            master.target_system, master.target_component,
            mavutil.mavlink.MAV_DATA_STREAM_POSITION, 5, 1,
        )

        _counts: dict[str, int] = {}
        _last_print = time.time()

        while not stop_event.is_set():
            msg = master.recv_match(blocking=True, timeout=0.5)
            if msg is None:
                continue
            t = msg.get_type()
            _counts[t] = _counts.get(t, 0) + 1

            if t == "ATTITUDE":
                state.update_attitude(msg)
            elif t == "GLOBAL_POSITION_INT":
                state.update_position(msg)

            if time.time() - _last_print >= 3.0:
                _last_print = time.time()
                top = sorted(_counts.items(), key=lambda x: -x[1])[:6]
                print("[MAV] msgs: " + "  ".join(f"{k}={v}" for k, v in top))

    except Exception as e:
        print(f"[MAV] Error: {e}")


# ── Helpers ---------------------------------------------------------------

def parse_crop(s: str):
    try:
        parts = [int(v) for v in s.split(",")]
        if len(parts) != 4:
            raise ValueError
        return tuple(parts)
    except ValueError:
        raise argparse.ArgumentTypeError("--crop harus berupa X,Y,W,H (contoh: 0,0,640,480)")


# ── Main ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Kamera + HUD MAVLink")
    parser.add_argument("--connection", default="udpin:0.0.0.0:14550",
                        help="MAVLink connection string")
    parser.add_argument("--baud",   type=int, default=57600)
    parser.add_argument("--camera", type=int, default=0,
                        help="Index kamera (default: 0)")
    parser.add_argument("--res", nargs=2, type=int, metavar=("W", "H"),
                        help="Resolusi akuisisi kamera (contoh: --res 640 480)")
    parser.add_argument("--crop", type=parse_crop, metavar="X,Y,W,H",
                        help="Crop frame dari titik (X,Y) selebar W tinggi H (contoh: --crop 0,0,640,480)")
    parser.add_argument("--no-pitch", action="store_true",
                        help="Sembunyikan pitch ladder")
    parser.add_argument("--no-yaw",   action="store_true",
                        help="Sembunyikan yaw compass")
    args = parser.parse_args()

    # ── Kamera ───────────────────────────────────────────────────────────
    cap = cv2.VideoCapture(args.camera, cv2.CAP_AVFOUNDATION)
    if not cap.isOpened():
        print(f"Error: kamera {args.camera} tidak ditemukan")
        sys.exit(1)

    if args.res:
        cap.set(cv2.CAP_PROP_FRAME_WIDTH,  args.res[0])
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, args.res[1])

    cam_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    cam_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps   = cap.get(cv2.CAP_PROP_FPS) or 30.0

    if args.crop:
        cx, cy, cw, ch = args.crop
        if cx + cw > cam_w or cy + ch > cam_h:
            print(f"[CAM] Error: --crop {args.crop} melebihi ukuran akuisisi {cam_w}x{cam_h}")
            sys.exit(1)
        out_info = f"  output={cw}x{ch}  crop={args.crop}"
    else:
        out_info = ""

    print(f"[CAM] akuisisi={cam_w}x{cam_h} @ {fps:.0f} FPS{out_info}")

    # ── MAVLink thread ────────────────────────────────────────────────────
    state      = MavState()
    stop_event = threading.Event()
    mav_t = threading.Thread(
        target=mavlink_thread,
        args=(args.connection, args.baud, state, stop_event),
        daemon=True, name="mavlink",
    )
    mav_t.start()

    # ── HUD ───────────────────────────────────────────────────────────────
    hud     = HudDisplay(show_pitch=not args.no_pitch,
                         show_yaw=not args.no_yaw)
    hud_on  = True

    print("Tekan  h = toggle HUD  |  r = mulai/stop rekam  |  s = screenshot  |  q = keluar")

    writer    = None
    recording = False

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[CAM] Gagal membaca frame.")
                break

            if args.crop:
                cx, cy, cw, ch = args.crop
                frame = frame[cy:cy + ch, cx:cx + cw]
            roll, pitch, yaw, lat, lon = state.snapshot()

            hud.draw_hud(hud_on, frame, lat, lon, yaw, pitch, roll)

            if recording and writer is not None:
                writer.write(frame)
                cv2.circle(frame, (20, 20), 8, (0, 0, 255), -1)
                cv2.putText(frame, "REC", (35, 27),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 255), 2)

            cv2.imshow("HUD", frame)
            key = cv2.waitKey(1) & 0xFF

            if key == ord("q"):
                break
            elif key == ord("h"):
                hud_on = not hud_on
                print(f"[HUD] {'ON' if hud_on else 'OFF'}")
            elif key == ord("s"):
                fname = f"screenshot_{int(time.time())}.png"
                cv2.imwrite(fname, frame)
                print(f"[CAM] Screenshot disimpan: {fname}")
            elif key == ord("r"):
                if not recording:
                    h, w = frame.shape[:2]
                    fname = f"rekaman_{int(time.time())}.avi"
                    writer = cv2.VideoWriter(
                        fname,
                        cv2.VideoWriter_fourcc(*"MJPG"),
                        fps,
                        (w, h),
                    )
                    recording = True
                    print(f"[REC] Rekaman dimulai: {fname}")
                else:
                    recording = False
                    writer.release()
                    writer = None
                    print("[REC] Rekaman dihentikan dan disimpan.")

    finally:
        if recording and writer is not None:
            writer.release()
        stop_event.set()
        cap.release()
        cv2.destroyAllWindows()
        mav_t.join(timeout=2.0)


if __name__ == "__main__":
    main()
