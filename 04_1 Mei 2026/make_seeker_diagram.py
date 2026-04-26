"""Generate seeker.png — control system block diagram: ex/ey → PID → aileron/elevator."""

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyArrowPatch, FancyBboxPatch

fig, ax = plt.subplots(figsize=(14, 7))
ax.set_xlim(0, 14)
ax.set_ylim(0, 7)
ax.axis("off")
fig.patch.set_facecolor("#0f1117")
ax.set_facecolor("#0f1117")

# ── Colour palette ────────────────────────────────────────────────────────────
C_BOX_CAM   = "#1a3a5c"
C_BOX_CALC  = "#1a4a2a"
C_BOX_MAV   = "#3a2a5c"
C_BOX_PID   = "#5c3a1a"
C_BOX_SRV   = "#4a1a1a"
C_BORDER    = "#aaaaaa"
C_ARROW     = "#dddddd"
C_LABEL     = "#ffffff"
C_SUB       = "#aaaaaa"
C_EX        = "#4da6ff"   # blue  — lateral channel
C_EY        = "#ff6b6b"   # red   — vertical channel
C_AIL       = "#4da6ff"
C_ELV       = "#ff6b6b"
C_MAV_LINE  = "#cc88ff"

def box(cx, cy, w, h, fc, label, sublabel="", lc=C_LABEL, sc=C_SUB, fs=10, sfs=8):
    rect = FancyBboxPatch((cx - w/2, cy - h/2), w, h,
                          boxstyle="round,pad=0.05",
                          facecolor=fc, edgecolor=C_BORDER, linewidth=1.2)
    ax.add_patch(rect)
    dy = 0.18 if sublabel else 0
    ax.text(cx, cy + dy, label,    ha="center", va="center",
            color=lc, fontsize=fs, fontweight="bold")
    if sublabel:
        ax.text(cx, cy - 0.22, sublabel, ha="center", va="center",
                color=sc, fontsize=sfs)

def arrow(x0, y0, x1, y1, color=C_ARROW, lw=1.5, style="->"):
    ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                arrowprops=dict(arrowstyle=style, color=color,
                                lw=lw, connectionstyle="arc3,rad=0"))

def label_on_arrow(x, y, text, color=C_LABEL, fs=8.5, ha="center"):
    ax.text(x, y, text, ha=ha, va="center", color=color,
            fontsize=fs, fontweight="bold",
            bbox=dict(facecolor="#0f1117", edgecolor="none", pad=1))

# ── Column x positions ────────────────────────────────────────────────────────
X_CAM   = 1.5
X_PROC  = 3.7
X_ERR   = 5.9
X_MAV   = 7.6
X_PID   = 9.8
X_SRV   = 12.2

Y_TOP   = 4.8   # lateral channel (ex / aileron)
Y_MID   = 3.5   # shared / MAVLink
Y_BOT   = 2.2   # vertical channel (ey / elevator)
Y_TITLE = 6.5

# ── Title ─────────────────────────────────────────────────────────────────────
ax.text(7, 6.6, "Sistem Kendali Seeker — Signal Input vs Output",
        ha="center", va="center", color=C_LABEL, fontsize=13, fontweight="bold")

# ── Blocks ────────────────────────────────────────────────────────────────────
# Camera
box(X_CAM, Y_MID, 2.0, 2.8, C_BOX_CAM, "Kamera", "frame BGR\n(W × H piksel)")

# Centroid detection
box(X_PROC, Y_MID, 2.0, 2.8, C_BOX_CALC, "Deteksi\nCentroid", "CamShift /\nHSV mask → (cx, cy)")

# Error calc — lateral
box(X_ERR, Y_TOP, 1.8, 0.9, C_BOX_CALC,
    "ex = (cx − W/2) / (W/2)", "", lc=C_EX, fs=8.5)

# Error calc — vertical
box(X_ERR, Y_BOT, 1.8, 0.9, C_BOX_CALC,
    "ey = −(cy − H/2) / (H/2)", "", lc=C_EY, fs=8.5)

# MAVLink block
box(X_MAV, Y_MID, 1.7, 2.8, C_BOX_MAV,
    "MAVLink", "TRACKING_\nMESSAGE\n(ID 11045)", fs=9)

# PID Roll
box(X_PID, Y_TOP, 2.0, 0.9, C_BOX_PID,
    "PID Roll", "ArduPlane TRACKING", lc=C_EX, fs=9)

# PID Pitch
box(X_PID, Y_BOT, 2.0, 0.9, C_BOX_PID,
    "PID Pitch", "ArduPlane TRACKING", lc=C_EY, fs=9)

# Aileron
box(X_SRV, Y_TOP, 1.9, 0.9, C_BOX_SRV,
    "Aileron", "servo1_raw (µs)", lc=C_AIL, fs=9)

# Elevator
box(X_SRV, Y_BOT, 1.9, 0.9, C_BOX_SRV,
    "Elevator", "vtail demix\nsv2 + sv4 (µs)", lc=C_ELV, fs=9)

# ── Arrows: Camera → Centroid ─────────────────────────────────────────────────
arrow(X_CAM + 1.0, Y_MID, X_PROC - 1.0, Y_MID, C_ARROW)
label_on_arrow((X_CAM + X_PROC) / 2, Y_MID + 0.2, "frame", fs=8)

# ── Arrows: Centroid → Error blocks ──────────────────────────────────────────
# fork up to ex
ax.annotate("", xy=(X_ERR - 0.9, Y_TOP), xytext=(X_PROC + 1.0, Y_MID),
            arrowprops=dict(arrowstyle="->", color=C_EX, lw=1.4,
                            connectionstyle="arc3,rad=-0.25"))
label_on_arrow(X_PROC + 1.5, Y_TOP + 0.3, "cx", color=C_EX, fs=8.5)

# fork down to ey
ax.annotate("", xy=(X_ERR - 0.9, Y_BOT), xytext=(X_PROC + 1.0, Y_MID),
            arrowprops=dict(arrowstyle="->", color=C_EY, lw=1.4,
                            connectionstyle="arc3,rad=0.25"))
label_on_arrow(X_PROC + 1.5, Y_BOT - 0.3, "cy", color=C_EY, fs=8.5)

# ── Arrows: Error → MAVLink ───────────────────────────────────────────────────
ax.annotate("", xy=(X_MAV - 0.85, Y_TOP - 0.2), xytext=(X_ERR + 0.9, Y_TOP),
            arrowprops=dict(arrowstyle="->", color=C_MAV_LINE, lw=1.4,
                            connectionstyle="arc3,rad=-0.2"))
label_on_arrow((X_ERR + X_MAV) / 2 + 0.1, Y_TOP + 0.35, "ex", color=C_EX, fs=9)

ax.annotate("", xy=(X_MAV - 0.85, Y_BOT + 0.2), xytext=(X_ERR + 0.9, Y_BOT),
            arrowprops=dict(arrowstyle="->", color=C_MAV_LINE, lw=1.4,
                            connectionstyle="arc3,rad=0.2"))
label_on_arrow((X_ERR + X_MAV) / 2 + 0.1, Y_BOT - 0.35, "ey − offset", color=C_EY, fs=9)

# pitch offset note
ax.text(X_ERR + 0.9, Y_BOT - 0.6,
        "ey_adj = ey − pitch_offset / TRK_MAX_DEG",
        ha="center", va="center", color="#ffcc66", fontsize=7.5,
        style="italic")

# ── Arrows: MAVLink → PID ─────────────────────────────────────────────────────
ax.annotate("", xy=(X_PID - 1.0, Y_TOP), xytext=(X_MAV + 0.85, Y_TOP - 0.2),
            arrowprops=dict(arrowstyle="->", color=C_EX, lw=1.4,
                            connectionstyle="arc3,rad=-0.2"))
ax.annotate("", xy=(X_PID - 1.0, Y_BOT), xytext=(X_MAV + 0.85, Y_BOT + 0.2),
            arrowprops=dict(arrowstyle="->", color=C_EY, lw=1.4,
                            connectionstyle="arc3,rad=0.2"))

# ── Arrows: PID → Servo ───────────────────────────────────────────────────────
arrow(X_PID + 1.0, Y_TOP, X_SRV - 0.95, Y_TOP, C_AIL)
arrow(X_PID + 1.0, Y_BOT, X_SRV - 0.95, Y_BOT, C_ELV)

# ── Channel labels (left margin) ─────────────────────────────────────────────
ax.text(0.25, Y_TOP, "Lateral\n(Roll)", ha="center", va="center",
        color=C_EX, fontsize=8.5, fontweight="bold",
        bbox=dict(facecolor="#0f1117", edgecolor=C_EX, linewidth=0.8,
                  boxstyle="round,pad=0.3"))
ax.text(0.25, Y_BOT, "Vertikal\n(Pitch)", ha="center", va="center",
        color=C_EY, fontsize=8.5, fontweight="bold",
        bbox=dict(facecolor="#0f1117", edgecolor=C_EY, linewidth=0.8,
                  boxstyle="round,pad=0.3"))

# ── Normalised range note ─────────────────────────────────────────────────────
ax.text(X_ERR, Y_MID, "∈ [−1, 1]", ha="center", va="center",
        color="#888888", fontsize=8, style="italic")

# ── Component labels (top) ────────────────────────────────────────────────────
for x, lbl in [(X_CAM,  "Laptop\n(Seeker)"),
               (X_PROC, "Laptop\n(Seeker)"),
               (X_ERR,  "Laptop\n(Seeker)"),
               (X_MAV,  "UDP\nMAVLink"),
               (X_PID,  "Pixhawk\n(ArduPlane)"),
               (X_SRV,  "Pixhawk\n(ArduPlane)")]:
    ax.text(x, 0.55, lbl, ha="center", va="center",
            color="#666666", fontsize=7)

# ── Divider line between laptop and pixhawk domains ──────────────────────────
ax.axvline(x=8.5, ymin=0.08, ymax=0.92, color="#444444",
           linewidth=1.0, linestyle="--")
ax.text(8.5, 0.18, "◄ Laptop          Pixhawk ►",
        ha="center", va="center", color="#555555", fontsize=7.5)

plt.tight_layout(pad=0.3)
out = "seeker.png"
plt.savefig(out, dpi=150, bbox_inches="tight", facecolor=fig.get_facecolor())
print(f"Saved: {out}")
