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
        for msg_id, hz in ((30, 25), (33, 5)):
            master.mav.command_long_send(
                master.target_system, master.target_component,
                mavutil.mavlink.MAV_CMD_SET_MESSAGE_INTERVAL,
                0, msg_id, int(1e6 / hz), 0, 0, 0, 0, 0,
            )

        while not stop_event.is_set():
            msg = master.recv_match(
                type=("ATTITUDE", "GLOBAL_POSITION_INT"),
                blocking=True, timeout=0.5,
            )
            if msg is None:
                continue
            t = msg.get_type()
            if t == "ATTITUDE":
                state.update_attitude(msg)
            elif t == "GLOBAL_POSITION_INT":
                state.update_position(msg)

    except Exception as e:
        print(f"[MAV] Error: {e}")


# ── Main ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description="Kamera + HUD MAVLink")
    parser.add_argument("--connection", default="udpin:0.0.0.0:14550",
                        help="MAVLink connection string")
    parser.add_argument("--baud",   type=int, default=57600)
    parser.add_argument("--camera", type=int, default=0,
                        help="Index kamera (default: 0)")
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

    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  // 2
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) // 2
    fps    = cap.get(cv2.CAP_PROP_FPS) or 30.0
    print(f"[CAM] {width}x{height} @ {fps:.0f} FPS")

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

    print("Tekan  h = toggle HUD  |  s = screenshot  |  q = keluar")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("[CAM] Gagal membaca frame.")
                break

            frame = cv2.resize(frame, (width, height))
            roll, pitch, yaw, lat, lon = state.snapshot()

            hud.draw_hud(hud_on, frame, lat, lon, yaw, pitch, roll)

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

    finally:
        stop_event.set()
        cap.release()
        cv2.destroyAllWindows()
        mav_t.join(timeout=2.0)


if __name__ == "__main__":
    main()
