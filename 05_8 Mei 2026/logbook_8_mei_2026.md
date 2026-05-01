# Logbook Kegiatan — 8 Mei 2026

| | |
|---|---|
| **Penelitian** | Sistem Kendali Drone Kamikaze Berbasis Deteksi Objek Warna dalam Simulasi HITL |
| **Tim** | Musa El Hanafi & Muhammad Ihsan Fahriansyah |
| **Lokasi** | Lab Komputer SMA Swasta Alfa Centauri, Kota Bandung |
| **Hari/Tanggal** | Jumat, 8 Mei 2026 |

---

Kegiatan hari ini berfokus pada **integrasi sistem seeker dengan simulasi HITL**. Seeker dijalankan di laptop yang sama, mengambil input dari kamera webcam yang mengarah ke layar X-Plane. Komunikasi antara seeker dan Pixhawk menggunakan MAVLink melalui UDP loopback. Pengujian mencakup deteksi objek berwarna merah muda (pink), pengiriman error tracking, manajemen mode terbang otomatis, dan rekaman video saat fase terminal.

---

## Arsitektur Sistem Integrasi Seeker–HITL


![Physical Architecture HITL](chart_00_physical_architecture.png)

**Aliran data integrasi:**

| Arah | Jalur | Konten |
|---|---|---|
| Kamera → Seeker | USB | Frame BGR dari kamera |
| Seeker → Pixhawk | UDP 14560 | MAVLink: `TRACKING_MESSAGE` (ID 11045), `SET_MODE`, `COMMAND_LONG` |
| Pixhawk → Seeker | UDP 14560 | MAVLink: `HEARTBEAT`, `ATTITUDE`, `VFR_HUD`, `GLOBAL_POSITION_INT`, `MISSION_CURRENT`, `RC_CHANNELS` |
| Pixhawk ↔ X-Plane | PPP (TELEM2 USB-UART) | DATA@ rows sensor, DREF aktuator |


---

## 1. Repositori Pengembangan Seeker

**Repositori:** [https://github.com/musaelhanafi/drone-seeker](https://github.com/musaelhanafi/drone-seeker)

Seluruh kode seeker dikembangkan secara terbuka di repositori GitHub `musaelhanafi/drone-seeker`. Pengembangan dimulai pada **27 Maret 2026** dan berlangsung secara aktif hingga sesi integrasi HITL ini.


### Class Diagram

![Class Diagram drone-seeker](chart_04_class_diagram.png)

### Struktur Modul

| File | Baris | Fungsi |
|---|---|---|
| `seeker.py` | 1026 | Deteksi warna HSV, CamShift/MeanShift tracker, Kalman filter, HUD overlay |
| `seekerctrl.py` | 832 | MAVLink conn, mode management, TRACKING_MESSAGE, CSV logger, FFmpeg recorder |
| `main.py` | 226 | Entry point CLI, argument parsing |
| `hud_display.py` | — | Overlay HUD pitch/yaw pada frame video |
| `joystick_handler.py` | — | Joystick input → RC override MAVLink |



---

## 2. Setup Koneksi HITL (pppd + MAVProxy)

### PPP Tunnel — Laptop ke Pixhawk

Pixhawk terhubung ke laptop melalui USB–UART adapter pada port TELEM2 (SERIAL2, 115200 baud). `pppd` membuat tunnel IP point-to-point sehingga ArduPlane dapat mengirim DATA@ sensor ke X-Plane dan menerima DREF aktuator balik.

**Identifikasi device:**

```bash
# macOS
ls /dev/tty.usbserial-*

# Linux
ls /dev/ttyUSB*
```

**Jalankan pppd:**

```bash
# macOS
sudo pppd /dev/tty.usbserial-XXXX 115200 \
  10.0.0.1:10.0.0.2 \
  noauth local nodetach \
  asyncmap 0 novj nopcomp noaccomp \
  lcp-echo-interval 0
```

```bash
# Linux
sudo pppd /dev/ttyUSB0 115200 \
  10.0.0.1:10.0.0.2 \
  noauth local nodetach \
  asyncmap 0 novj nopcomp noaccomp \
  lcp-echo-interval 0
```

| IP | Host |
|---|---|
| `10.0.0.1` | Laptop (X-Plane) |
| `10.0.0.2` | Pixhawk |

> `lcp-echo-interval 0` — nonaktifkan LCP keepalive (tanpa ini pppd putus setelah ~12 detik)

### MAVProxy — Forward MAVLink ke QGroundControl dan drone-seeker

Setelah PPP tunnel aktif, `mavproxy.py` meneruskan stream MAVLink dari Pixhawk ke QGroundControl (port 14550) dan ke drone-seeker (port 14560) secara bersamaan.

```bash
mavproxy.py \
  --master=udp:10.0.0.2:14560 \
  --out=udp:127.0.0.1:14550 \
  --out=udp:127.0.0.1:14560
```

| Parameter | Nilai | Keterangan |
|---|---|---|
| `--master` | `udp:10.0.0.2:14560` | MAVLink masuk dari Pixhawk via PPP |
| `--out` (1) | `udp:127.0.0.1:14550` | QGroundControl (auto-connect loopback) |
| `--out` (2) | `udp:127.0.0.1:14560` | drone-seeker (`udpin:0.0.0.0:14560`) |

**Jalankan drone-seeker** (setelah mavproxy aktif):

```bash
python3 main.py --source 0 --connection udpin:0.0.0.0:14560 \
    --record --debug --auto
```

![System Architecture](chart_02_architecture.png)

---

## 3. Setup Kamera Webcam sebagai Input Seeker

**Kegiatan:**
Kamera webcam diarahkan ke layar laptop yang menampilkan tampilan kokpit X-Plane. Objek target disimulasikan sebagai benda berwarna merah muda (pink) yang ditempatkan di area pandang kamera.

**Konfigurasi:**
```bash
python3 main.py --source 0 --connection udpin:0.0.0.0:14560 \
    --record --debug --auto
```

| Parameter | Nilai | Keterangan |
|---|---|---|
| `--source 0` | index 0 | Webcam pertama yang terdeteksi sistem |
| `--connection` | `udpin:0.0.0.0:14560` | MAVLink UDP dari Pixhawk/QGC |
| `--record` | aktif | Rekam video takeoff dan tracking |
| `--debug` | aktif | Tulis CSV telemetri setiap frame tracking |
| `--auto` | aktif | Mode manajemen otomatis berbasis waypoint |

**Hasil:** Seeker berhasil membuka webcam dan menampilkan feed video real-time dengan overlay HUD.

---

## 4. Pipeline Deteksi dan Tracking Objek

**Kegiatan:**
Verifikasi pipeline deteksi warna merah muda (pink) menggunakan masker HSV dan tracker CamShift berjalan normal pada input webcam.

**Alur pipeline:**

```
Frame BGR
    │
    ▼
Gaussian blur + HSV convert
    │
    ▼
Masker HSV adaptif (inRange)
    │
    ▼
Nearest blob detection (rectangular)
    │
    ▼
CamShift tracker                     ← update ROI per frame
    │
    ▼
Kalman filter prediksi posisi        ← kompensasi oklusi sementara
    │
    ▼
(cx, cy) → ex, ey            ← dinormalisasi ke [-1, 1]
    │
    ▼
Latency + PN lead prediction         ← LATENCY_S=0.08s, PN_LEAD_S=0.30s
    │
    ▼
Pitch offset adjustment              ← errory -= pitch_offset / TRK_MAX_DEG
    │
    ▼
TRACKING_MESSAGE → Pixhawk
```

**Parameter error:**

```
ex  =  (cx - w/2) / (w/2)         # positif = target di kanan
ey  = -(cy - h/2) / (h/2)         # positif = target di atas
ey_adj = errory - TRK_PITCH_OFFSET / TRK_MAX_DEG   # kompensasi bias pitch karena arah mounting kamera
```

![Detection Algorithm](chart_01_detection.png)

![Per-Frame Tracking Logic](chart_frame_tracking_logic.png)

**Hasil:** Deteksi dan tracking berjalan pada minimal throughput 15 FPS. CamShift berhasil mempertahankan lock selama target terlihat jelas.

---

## 5. Manajemen Mode Terbang Otomatis

**Kegiatan:**
Pengujian siklus operasional penuh drone kamikaze dalam simulasi HITL — mencakup tiga fase berurutan: takeoff otonom, cruise mengikuti waypoint, dan fase terminal saat seeker mendeteksi dan mengunci objek target. Ketiga fase ini dieksekusi dalam satu run tanpa intervensi manual.

**Aturan transisi mode (`--auto`):**

| Kondisi | Aksi |
|---|---|
| Mode bukan AUTO | Kirim SET_MODE → AUTO |
| AUTO + WP bukan WP terakhir | Pertahankan AUTO, ikuti waypoint misi |
| AUTO + WP terakhir + jarak ≤ 1000 m + target terkunci | SET_MODE → TRACKING (mode 27) |
| Tracking hilang ≥ 10 frame berturut-turut | SET_MODE → AUTO (kembali ke misi) |

![Siklus Otonom Drone Kamikaze](siklus_otonom.png)

### Siklus Operasional Drone Kamikaze

Misi drone kamikaze dibagi menjadi tiga fase utama yang berjalan secara berurutan dan otonom:

**Fase 1 — Takeoff**

<a href="https://www.youtube.com/watch?v=kMWYlDaOB6g" target="_blank">
  <div style="position:relative; display:inline-block;">
    <img src="https://img.youtube.com/vi/kMWYlDaOB6g/maxresdefault.jpg"
         alt="Drone Kamikaze Satria — Auto Takeoff HITL Simulasi X-Plane" width="640"/>
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                width:68px; height:48px; background:rgba(255,0,0,0.85); border-radius:12px;
                display:flex; align-items:center; justify-content:center; pointer-events:none;">
      <div style="width:0; height:0; border-top:14px solid transparent;
                  border-bottom:14px solid transparent; border-left:24px solid white;
                  margin-left:5px;"></div>
    </div>
  </div>
</a>

*Drone Kamikaze Satria lepas landas secara otonom dari WP 0, mengikuti waypoint misi hingga ketinggian cruise. Direkam dari sudut FPV kamera seeker pada sesi HITL 8 Mei 2026.*

Setelah seeker aktif, sistem memerintahkan Pixhawk masuk ke mode AUTO. Pixhawk mengeksekusi misi waypoint mulai dari WP 0 (takeoff). Pada fase ini ArduPlane mengontrol throttle, pitch, dan roll untuk mencapai ketinggian misi secara mandiri. Di simulasi HITL, X-Plane mensimulasikan fisika pesawat dan ArduPlane merespons seolah-olah pesawat sungguhan. Rekaman video takeoff dimulai otomatis saat drone melewati WP 1.

**Fase 2 — Cruise (Mengikuti Waypoint)**

Setelah mencapai ketinggian jelajah, drone terbang mengikuti jalur waypoint yang telah diprogram di QGroundControl dalam mode AUTO. Sistem menunggu hingga dua kondisi terpenuhi sekaligus: drone berada di **waypoint terakhir** dan jarak ke target kira-kira ≤ **1000 m**.

**Fase 3 — Terminal (Seeker Aktif)**

Saat kondisi fase terminal terpenuhi dan target terkunci oleh kamera, seeker memerintahkan Pixhawk (Flight Controller) beralih ke mode **TRACKING (custom mode 27)**. Pada fase ini kendali penuh diserahkan ke sistem seeker. PID roll mengarahkan pesawat secara lateral mengikuti errorx, sementara PID pitch menukikkan hidung pesawat ke bawah mengikuti errory. Drone menukik tajam menuju target — pada pengujian ini puncak kecepatan vertikal mencapai **-38.60 m/s**. Apabila lock target hilang lebih dari 10 frame berturut-turut, sistem kembali ke mode AUTO untuk mencegah drone kehilangan arah dan kembali melakukan pelacakan saat objek terdeteksi kembali.

**Transisi yang berhasil diverifikasi:**
1. Seeker memerintahkan mode AUTO → Pixhawk mengeksekusi misi takeoff dari WP 0
2. Drone terbang mengikuti waypoint misi di X-Plane
3. Ketika mencapai WP terakhir dan jarak horizontal ≤ 1000 m, seeker mengaktifkan TRACKING
4. Pixhawk beralih ke mode TRACKING (custom mode 27) dan menerima error dari seeker

**Hasil:** Transisi AUTO → TRACKING berhasil terpicu secara otomatis tanpa intervensi manual.

---

## 6. Pengiriman TRACKING_MESSAGE ke Pixhawk

**Kegiatan:**
Verifikasi pesan MAVLink `TRACKING_MESSAGE` (ID 11045, ardupilotmega dialect) diterima dan diproses oleh firmware ArduPlane custom.

**Format pesan:**

| Field | Tipe | Nilai | Keterangan |
|---|---|---|---|
| `timestamp_us` | uint64 | `time.monotonic() × 1e6` | Timestamp mikrosecond |
| `errorx` | float | [−1.0, +1.0] | Error horizontal (kanan positif) |
| `errory` | float | [−1.0, +1.0] | Error vertikal adjusted (atas positif) |

**Di firmware (`mode_tracking.cpp`):**

```cpp
// handle_tracking_error() mengkonversi normalized → radians
_errorx_rad = errorx_rad;   // × TRACKING_MAX_DELTA_RAD
_errory_rad = errory_rad;

// update(): PID roll dan pitch
// Roll PID: drives errorx → 0
// Pitch PID: drives errory → pitch_offset (setpoint = TRK_PITCH_OFFSET deg)
const float pitch_cd = tracking_pitch_pid.update_all(
    degrees(ey), pitch_offset_deg, dt_s) * ramp;
```

![PID Flow Firmware Tracking](chart_02_pid_flow.png)

![Tracking Logic Loop](chart_03_tracking_logic.png)

**Hasil:** Pixhawk menerima dan merespons `TRACKING_MESSAGE`. Log GCS menampilkan `Tracking: active` saat mode diaktifkan.

---

## 7. Logging CSV Telemetri

**Kegiatan:**
Verifikasi CSV logger mencatat seluruh kolom telemetri dengan benar selama fase TRACKING aktif.

**Kolom CSV (`tracking.csv`):**

| Kolom | Sumber | Keterangan |
|---|---|---|
| `timestamp_s` | `time.monotonic()` | Waktu frame |
| `errorx` | seeker | Error horizontal normalized |
| `errory` | seeker | Error vertikal (pitch-adjusted) |
| `aileron`, `elevator` | `SERVO_OUTPUT_RAW` | Output servo demixed |
| `roll_deg`, `pitch_deg` | `ATTITUDE` | Sikap pesawat |
| `roll_rate_dps`, `pitch_rate_dps` | `ATTITUDE` | Laju rotasi |
| `pid_roll_*`, `pid_pitch_*` | `PID_TUNING` | Term PID individual |
| `alt_rel_m` | `GLOBAL_POSITION_INT` | Ketinggian relatif (AGL) |
| `groundspeed_ms` | `VFR_HUD` | Kecepatan tanah (m/s) |
| `throttle_pct` | `VFR_HUD` | Throttle (%) |
| `nav_pitch_deg` | `NAV_CONTROLLER_OUTPUT` | Pitch target autopilot |
| `target_locked` | seeker | 1 = lock aktif, 0 = hilang |
| `dist_m` | haversine | Jarak horizontal ke target (m) |

**Hasil:** CSV berhasil dihasilkan. File dianalisis menggunakan `terminal_analyse.py` untuk evaluasi fase terminal.

---

## 8. Analisis Fase Terminal dengan terminal_analyse.py

**Kegiatan:**
Analisis CSV hasil logging menggunakan script `terminal_analyse.py` untuk mengevaluasi performa sistem pada fase pendekatan akhir.

**Perintah:**
```bash
python3 terminal_analyse.py tracking_kiri.csv
```

**Output ringkasan (`tracking_kiri.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 36.2 s  (617 rows)
  Target locked   : 603 rows  (97.7%)
  Track lost      : 14 rows  (2.3%)

  ── First track acquisition ──
  Time            : t+0.1 s
  Alt above target: 59.5 m
  Speed           : 88.3 km/h
  Distance        : 970.8 m

  ── Nearest point (hit) ──
  Time            : t+35.9 s
  Distance        : 5.0 m
  Speed at hit    : 101.9 km/h  (28.3 m/s)
  Alt at hit      : 2.4 m

  ── Descent ──
  Mean descent    : 1.65 m/s
  Peak descent    : 26.22 m/s
  Total alt drop  : 57.0 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -3.9 deg
  Mean nav_pitch  : -4.2 deg
───────────────────────────────────────────────────────
```

**Screenshot sesaat sebelum menabrak target:**

![Sesaat sebelum menabrak target](sesaat_sebelum_nabrak_target.png)

**Video Drone Kamikaze Satria — Fase Terminal: Deteksi, Tracking, dan Hit Target (HITL Simulasi X-Plane)**

*Seeker mendeteksi dan mengunci objek target berwarna pink, mode TRACKING aktif, drone menukik dan menabrak target pada kecepatan 102 km/h. Akurasi tracking 93.9% — HITL 8 Mei 2026.*

<a href="https://youtu.be/oXJA1Vcrbvw" target="_blank">
  <div style="position:relative; display:inline-block;">
    <img src="https://img.youtube.com/vi/oXJA1Vcrbvw/maxresdefault.jpg"
         alt="Drone Kamikaze Satria — Fase Terminal HITL Simulasi X-Plane" width="640"/>
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                width:68px; height:48px; background:rgba(255,0,0,0.85); border-radius:12px;
                display:flex; align-items:center; justify-content:center; pointer-events:none;">
      <div style="width:0; height:0; border-top:14px solid transparent;
                  border-bottom:14px solid transparent; border-left:24px solid white;
                  margin-left:5px;"></div>
    </div>
  </div>
</a>

**Video analisis terminal (`terminal_analyse.py`):**

*Visualisasi 4 panel sinyal kendali fase terminal: altitude, camera error (ex/ey), attitude pesawat, dan control surfaces selama 26 detik tracking aktif. Akurasi 93.9%, mean FPS 29.4.*

<a href="https://www.youtube.com/watch?v=wGvmdkjbiSc" target="_blank">
  <div style="position:relative; display:inline-block;">
    <img src="https://img.youtube.com/vi/wGvmdkjbiSc/maxresdefault.jpg"
         alt="Drone Kamikaze Satria — Analisis Fase Terminal terminal_analyse.py" width="640"/>
    <div style="position:absolute; top:50%; left:50%; transform:translate(-50%,-50%);
                width:68px; height:48px; background:rgba(255,0,0,0.85); border-radius:12px;
                display:flex; align-items:center; justify-content:center; pointer-events:none;">
      <div style="width:0; height:0; border-top:14px solid transparent;
                  border-bottom:14px solid transparent; border-left:24px solid white;
                  margin-left:5px;"></div>
    </div>
  </div>
</a>

**Grafik analisis fase terminal:**

![Terminal Analysis Plot](terminal_analysis_plot.png)

**Keterangan grafik (4 panel):**
1. Altitude / Groundspeed / Throttle vs waktu
2. Camera error (errorx, errory) vs waktu — area abu = lock hilang
3. Attitude pesawat (pitch, roll, nav_pitch) vs waktu
4. Control surfaces (elevator, aileron) vs waktu

**Penanda pada grafik:**
- Garis cyan (`:`) — titik jarak terdekat ke target

**Deskripsi manuver (tracking_kiri.csv):**

Seeker pertama kali mengunci target saat drone berada di ketinggian **59.5 m** di atas target dengan jarak horizontal **970.8 m** dan kecepatan **88.3 km/h**. Begitu lock diperoleh pada t+0.1 s, mode TRACKING aktif dan sistem PID mulai mengarahkan drone menukik ke arah target. Drone menjalani descent rata-rata **1.65 m/s** dengan puncak descent mencapai **26.22 m/s** saat fase terminal — menunjukkan manuver menukik tajam mendekati target. Total penurunan ketinggian selama fase tracking adalah **57.0 m**.

Dari pertama mendeteksi hingga titik terdekat (hit), waktu yang dibutuhkan adalah **35.9 detik** (t+0.1 s → t+35.9 s). Saat menabrak target drone memiliki kecepatan **101.9 km/h** (28.3 m/s) pada ketinggian **2.4 m** di atas target. Rata-rata pitch pesawat selama tracking adalah **-3.9°** (nav_pitch: -4.2°).

Seeker mempertahankan lock dengan akurasi **97.7%** (603 dari 617 frame) dengan throughput rata-rata **16.8 FPS**.

**Hasil:** Drone menabrak target pada kecepatan **101.9 km/h**. Akurasi pelacakan objek warna **97.7%** sepanjang fase terminal.

---

## 9. Perbandingan Hasil Pengujian: Empat Run (Kiri & Kanan, 60m & 80m)

Empat sesi tracking dianalisis menggunakan `terminal_analyse.py`. Semua sesi berhasil menabrak target dalam simulasi HITL.

| Metrik | Kiri (60m) | Kanan (60m) | Kiri (80m) | Kanan (80m) |
|---|---|---|---|---|
| Durasi fase terminal | 36.2 s (617 rows) | 34.6 s (701 rows) | 23.0 s (678 rows) | 21.4 s (637 rows) |
| Alt di atas target saat lock on | 59.5 m | 58.3 m | 76.8 m | 77.8 m |
| Jarak lock on | 970.8 m | 919.3 m | 774.5 m | 705.5 m |
| Akurasi deteksi dan tracking (%) | 97.7% (603/617) | 97.7% (685/701) | 97.8% (663/678) | 96.5% (615/637) |
| Kecepatan nabrak | 101.9 km/h (28.3 m/s) | 102.2 km/h (28.4 m/s) | 108.6 km/h (30.2 m/s) | 110.5 km/h (30.7 m/s) |
| Jarak terdekat (hit) | 5.0 m | 9.4 m | 6.9 m | 9.1 m |
| Ketinggian saat hit | 2.4 m | 2.7 m | 1.4 m | 1.7 m |
| Mean descent | 1.65 m/s | 1.66 m/s | 3.19 m/s | 3.47 m/s |
| Peak descent | 26.22 m/s | 31.22 m/s | 60.00 m/s | 65.00 m/s |
| Total alt drop | 57.0 m | 55.7 m | 75.4 m | 76.1 m |
| Mean pitch (locked) | -3.9° | -4.1° | 0.6° | -0.1° |
| Mean nav_pitch (locked) | -4.2° | -4.2° | 0.3° | -0.4° |
| Menabrak target? | Ya | Ya | Ya | Ya |
| Respon servo | Sesuai | Sesuai | Sesuai | Sesuai |
| Frame rate | 16.8 FPS | 20.2 FPS | 29.5 FPS | 29.8 FPS |

**Catatan:**
- Akurasi tracking konsisten di semua run (96.5–97.8%), menunjukkan sistem deteksi stabil dari berbagai sudut dan ketinggian.
- Kecepatan nabrak meningkat dari ~102 km/h (60m) ke ~109–110 km/h (80m) karena sudut dive lebih curam.
- Durasi fase terminal 80m (~22 s) jauh lebih pendek dari 60m (~35 s) — sudut depresi lebih besar menghasilkan ey_raw lebih besar sejak awal lock sehingga PID pitch lebih agresif.
- Peak descent 80m (60–65 m/s) jauh lebih tinggi dari 60m (26–31 m/s), menunjukkan manuver menukik yang jauh lebih tajam.
- Mean pitch 60m sekitar -4° (bias dive aktif), sedangkan 80m mendekati 0° — ey_raw besar dari ketinggian tinggi menghasilkan koreksi PID yang mengimbangi bias offset sehingga rata-rata pitch mendekati nol meski drone tetap menukik.

---

## 10. Analisis Fase Terminal dari Ketinggian 80m

Pengujian ulang dilakukan dari ketinggian cruise yang lebih tinggi (~80m di atas target) untuk mengevaluasi perbedaan karakteristik pendekatan dibanding sesi sebelumnya (~60m). Dua run dianalisis: `tracking_kiri_80m.csv` dan `tracking_kanan_80m.csv`.

**Output ringkasan (`tracking_kiri_80m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 23.0 s  (678 rows)
  Target locked   : 663 rows  (97.8%)
  Track lost      : 15 rows  (2.2%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 76.8 m
  Speed           : 105.7 km/h
  Distance        : 774.5 m

  ── Nearest point (hit) ──
  Time            : t+22.8 s
  Distance        : 6.9 m
  Speed at hit    : 108.6 km/h  (30.2 m/s)
  Alt at hit      : 1.4 m

  ── Descent ──
  Mean descent    : 3.19 m/s
  Peak descent    : 60.00 m/s
  Total alt drop  : 75.4 m

  ── Pitch (locked rows only) ──
  Mean pitch      : 0.6 deg
  Mean nav_pitch  : 0.3 deg
───────────────────────────────────────────────────────
```

**Output ringkasan (`tracking_kanan_80m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 21.4 s  (637 rows)
  Target locked   : 615 rows  (96.5%)
  Track lost      : 22 rows  (3.5%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 77.8 m
  Speed           : 104.6 km/h
  Distance        : 705.5 m

  ── Nearest point (hit) ──
  Time            : t+21.1 s
  Distance        : 9.1 m
  Speed at hit    : 110.5 km/h  (30.7 m/s)
  Alt at hit      : 1.7 m

  ── Descent ──
  Mean descent    : 3.47 m/s
  Peak descent    : 65.00 m/s
  Total alt drop  : 76.1 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -0.1 deg
  Mean nav_pitch  : -0.4 deg
───────────────────────────────────────────────────────
```

**Deskripsi manuver (tracking_kiri_80m.csv):**

Seeker langsung mengunci target pada t+0.0 s dari ketinggian **76.8 m** di atas target, jarak horizontal **774.5 m**, kecepatan **105.7 km/h**. Dengan sudut depresi yang lebih besar dari 80m dibanding 60m, ey_raw lebih besar sejak awal sehingga PID pitch mendapat sinyal koreksi lebih kuat. Drone menjalani descent rata-rata **3.19 m/s** — hampir dua kali lipat dibanding sesi 60m — dengan puncak descent **60.00 m/s** saat fase terminal. Total penurunan ketinggian **75.4 m** dalam **22.8 detik**. Kecepatan saat menabrak **108.6 km/h** pada ketinggian **1.4 m** di atas target.

**Catatan:**
- Dari 80m, durasi fase terminal jauh lebih pendek (~22 s vs ~35 s) karena sudut depresi lebih besar mendorong PID pitch lebih agresif sejak awal lock.
- Peak descent 60–65 m/s menunjukkan dive tajam mendekati terminal; nilai ini jauh lebih tinggi dari sesi 60m (26–31 m/s).
- Mean pitch mendekati 0° pada sesi 80m (vs -4° pada 60m) — pada ketinggian lebih tinggi, ey_raw besar menghasilkan koreksi positif yang mengimbangi bias offset, menghasilkan pitch rata-rata mendekati 0° meski drone aktif menukik.
- Kecepatan nabrak lebih tinggi (~109 km/h vs ~102 km/h) karena dive lebih tajam.

**Hasil:** Kedua sesi 80m berhasil menabrak target. Akurasi tracking 97.8% (kiri) dan 96.5% (kanan).

---

## 11. Kendala dan Solusi

| No | Kendala | Solusi |
|---|---|---|
| 1 | Rekaman video menyebabkan hang pada main loop | Ganti OpenCV VideoWriter dengan FFmpeg subprocess pipe; write ke stdin non-blocking |
| 2 | Webcam tidak terdeteksi pada index 0 | Cek `ls /dev/video*` dan sesuaikan `--source` |
| 3 | TRACKING_MESSAGE tidak diterima Pixhawk | Verifikasi dialect `ardupilotmega` terload di mavutil; pastikan UDP port 14560 sesuai |
| 4 | Seeker masuk TRACKING sebelum waktunya | Tambahkan gate: `in_auto AND on_last_wp AND close_enough` sebelum transisi |
| 5 | FPS tidak stabil saat recording dimulai | Tambahkan warmup 30 frame sebelum membuka VideoWriter |

---

## 12. Rencana Tindak Lanjut

| Prioritas | Kegiatan |
|---|---|
| Tinggi | Kalibrasi TRK_PITCH_OFFSET, TRK_ROLL_P/I/D, TRK_PTCH_P/I/D terhadap respons pesawat |
| Sedang | Pindahkan seeker ke Raspberry Pi (on-board) dan uji latency MAVLink via serial |
| Sedang | Uji multi-run dari berbagai sudut pendekatan untuk evaluasi konsistensi |
| Rendah | Integrasi HUD pitch/yaw overlay dengan data telemetri live di terminal_analyse.py |

---

## Ringkasan Kegiatan

| No | Kegiatan | Hasil |
|---|---|---|
| 1 | Setup repositori `drone-seeker` dan review struktur modul | ✅ Selesai |
| 2 | Konfigurasi PPP tunnel Pixhawk–laptop via TELEM2 USB-UART | ✅ Selesai |
| 3 | Setup MAVProxy — forward MAVLink ke QGC dan drone-seeker (UDP 14560) | ✅ Selesai |
| 4 | Konfigurasi webcam sebagai input seeker mengarah ke layar X-Plane | ✅ Selesai |
| 5 | Verifikasi pipeline deteksi dan tracking objek pink — CamShift + Kalman | ✅ Selesai |
| 6 | Pengujian manajemen mode otomatis: AUTO → TRACKING (mode 27) | ✅ Selesai |
| 7 | Verifikasi pengiriman `TRACKING_MESSAGE` (ID 11045) ke firmware ArduPlane | ✅ Selesai |
| 8 | Logging CSV telemetri 13 kolom selama fase TRACKING aktif | ✅ Selesai |
| 9 | Analisis fase terminal dengan `terminal_analyse.py` (60m) — kiri & kanan | ✅ Selesai |
| 10 | Analisis fase terminal dari ketinggian 80m — kiri & kanan | ✅ Selesai |
| 11 | Simulasi HITL end-to-end: takeoff → cruise → terminal — drone menabrak target | ✅ **Berhasil** |

*Logbook ditulis oleh: Muhammad Ihsan Fahriansyah & Musa El Hanafi*
