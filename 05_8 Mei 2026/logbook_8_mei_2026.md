# Logbook Kegiatan — 8 Mei 2026

| | |
|---|---|
| **Penelitian** | Sistem Kendali Drone Kamikaze Berbasis Deteksi Objek Warna dalam Simulasi HITL |
| **Tim** | Musa El Hanafi & Muhammad Ihsan Fahriansyah |
| **Lokasi** | Lab Komputer SMA Swasta Alfa Centauri, Kota Bandung |
| **Hari/Tanggal** | Jumat, 8 Mei 2026 |

---

![Foto Setup Seeker Unit](Foto Setup Seeker Unit.jpeg)

![Pengujian Seeker](Pengujian Seeker.jpeg)

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

[![Drone Kamikaze Satria — Auto Takeoff HITL Simulasi X-Plane](thumbnail_yt_takeoff.png)](https://www.youtube.com/watch?v=kMWYlDaOB6g)

*Drone Kamikaze Satria lepas landas secara otonom dari WP 0, mengikuti waypoint misi hingga ketinggian cruise. Direkam dari sudut FPV kamera seeker pada sesi HITL 8 Mei 2026.*

Setelah seeker aktif, sistem memerintahkan Pixhawk masuk ke mode AUTO. Pixhawk mengeksekusi misi waypoint mulai dari WP 0 (takeoff). Pada fase ini ArduPlane mengontrol throttle, pitch, dan roll untuk mencapai ketinggian misi secara mandiri. Di simulasi HITL, X-Plane mensimulasikan fisika pesawat dan ArduPlane merespons seolah-olah pesawat sungguhan. Rekaman video takeoff dimulai otomatis saat drone melewati WP 1.

**Fase 2 — Cruise (Mengikuti Waypoint)**

Setelah mencapai ketinggian jelajah, drone terbang mengikuti jalur waypoint yang telah diprogram di QGroundControl dalam mode AUTO. Sistem menunggu hingga dua kondisi terpenuhi sekaligus: drone berada di **waypoint terakhir** dan jarak ke target kira-kira ≤ **1000 m**.

**Fase 3 — Terminal (Seeker Aktif)**

Saat kondisi fase terminal terpenuhi dan target terkunci oleh kamera, seeker memerintahkan Pixhawk (Flight Controller) beralih ke mode **TRACKING (custom mode 27)**. Pada fase ini kendali penuh diserahkan ke sistem seeker. PID roll mengarahkan pesawat secara lateral mengikuti errorx, sementara PID pitch menukikkan hidung pesawat ke bawah mengikuti errory. Drone menukik tajam menuju target — pada pengujian ini puncak kecepatan vertikal mencapai **-29 hingga -59 m/s** bergantung ketinggian cruise dan trajektori tiap run. Apabila lock target hilang lebih dari 10 frame berturut-turut, sistem kembali ke mode AUTO untuk mencegah drone kehilangan arah dan kembali melakukan pelacakan saat objek terdeteksi kembali.

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
python3 terminal_analyse.py tracking_kiri_60m.csv
```

**Output ringkasan (`tracking_kiri_60m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 31.5 s  (647 rows)
  Target locked   : 587 rows  (90.7%)
  Track lost      : 60 rows  (9.3%)

  ── First track acquisition ──
  Time            : t+0.2 s
  Alt above target: 59.3 m
  Speed           : 88.6 km/h
  Distance        : 872.8 m

  ── Nearest point (hit) ──
  Time            : t+31.2 s
  Distance        : 7.5 m
  Speed at hit    : 109.3 km/h  (30.4 m/s)
  Alt at hit      : 4.0 m

  ── Descent ──
  Mean descent    : 1.82 m/s
  Peak descent    : 34.65 m/s
  Total alt drop  : 55.3 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -4.6 deg
  Mean nav_pitch  : -4.8 deg
───────────────────────────────────────────────────────
```

**Screenshot sesaat sebelum menabrak target:**

![Sesaat sebelum menabrak target](sesaat_sebelum_nabrak_target.png)

**Video Drone Kamikaze Satria — Fase Terminal: Deteksi, Tracking, dan Hit Target (HITL Simulasi X-Plane)**

*Seeker mendeteksi dan mengunci objek target berwarna pink, mode TRACKING aktif, drone menukik dan menabrak target pada kecepatan 109 km/h. Akurasi tracking 90.7% — HITL 8 Mei 2026.*

[![Drone Kamikaze Satria — Fase Terminal HITL Simulasi X-Plane](thumbnail_yt_terminal.png)](https://youtu.be/oXJA1Vcrbvw)

**Video analisis terminal (`terminal_analyse.py`):**

*Visualisasi 4 panel sinyal kendali fase terminal: altitude, camera error (ex/ey), attitude pesawat, dan control surfaces — `tracking_kanan_100m.csv`. Durasi 31.3 s, akurasi 100.0%, mean FPS 25.4.*

[![Drone Kamikaze Satria — Analisis Fase Terminal terminal_analyse.py](thumbnail_yt_analyse.png)](https://www.youtube.com/watch?v=wGvmdkjbiSc)

**Grafik analisis fase terminal:**

![Terminal Analysis Plot](terminal_analysis_plot.png)

**Keterangan grafik (4 panel):**
1. Altitude / Groundspeed / Throttle vs waktu
2. Camera error (errorx, errory) vs waktu — area abu = lock hilang
3. Attitude pesawat (pitch, roll, nav_pitch) vs waktu
4. Control surfaces (elevator, aileron) vs waktu

**Penanda pada grafik:**
- Garis cyan (`:`) — titik jarak terdekat ke target

**Deskripsi manuver (tracking_kiri_60m.csv):**

Seeker pertama kali mengunci target saat drone berada di ketinggian **59.3 m** di atas target dengan jarak horizontal **872.8 m** dan kecepatan **88.6 km/h**. Begitu lock diperoleh pada t+0.2 s, mode TRACKING aktif dan sistem PID mulai mengarahkan drone menukik ke arah target. Drone menjalani descent rata-rata **1.82 m/s** dengan puncak descent mencapai **34.65 m/s** saat fase terminal — menunjukkan manuver menukik tajam mendekati target. Total penurunan ketinggian selama fase tracking adalah **55.3 m**.

Dari pertama mendeteksi hingga titik terdekat (hit), waktu yang dibutuhkan adalah **31.2 detik** (t+0.2 s → t+31.2 s). Saat menabrak target drone memiliki kecepatan **109.3 km/h** (30.4 m/s) pada ketinggian **4.0 m** di atas target. Rata-rata pitch pesawat selama tracking adalah **-4.6°** (nav_pitch: -4.8°).

Seeker mempertahankan lock dengan akurasi **90.7%** (587 dari 647 frame) dengan throughput rata-rata **21.3 FPS**.

**Hasil:** Drone menabrak target pada kecepatan **109.3 km/h**. Akurasi pelacakan objek warna **90.7%** sepanjang fase terminal.

---

## 9. Perbandingan Hasil Pengujian: Enam Run (Kiri & Kanan, 60m, 80m & 100m)

Enam sesi tracking dianalisis menggunakan `terminal_analyse.py`. Semua sesi berhasil menabrak target dalam simulasi HITL.

| Metrik | Kiri (60m) | Kanan (60m) | Kiri (80m) | Kanan (80m) | Kiri (100m) | Kanan (100m) | **Rata-rata** |
|---|---|---|---|---|---|---|---|
| Durasi fase terminal | 31.5 s (647 rows) | 34.2 s (874 rows) | 33.3 s (874 rows) | 32.8 s (843 rows) | 32.3 s (741 rows) | 31.3 s (788 rows) | **32.6 s (795 rows)** |
| Alt di atas target saat lock on | 59.3 m | 58.0 m | 80.5 m | 77.7 m | 99.3 m | 98.1 m | **78.8 m** |
| Jarak lock on | 872.8 m | 963.0 m | 951.8 m | 955.9 m | 954.6 m | 954.8 m | **942.2 m** |
| Akurasi deteksi dan tracking (%) | 90.7% (587/647) | 100.0% (874/874) | 96.7% (845/874) | 100.0% (843/843) | 94.7% (702/741) | 100.0% (788/788) | **97.3% (4639/4767)** |
| Kecepatan nabrak | 109.3 km/h (30.4 m/s) | 16.7 km/h (4.6 m/s) | 113.4 km/h (31.5 m/s) | 110.0 km/h (30.6 m/s) | 116.2 km/h (32.3 m/s) | 113.6 km/h (31.6 m/s) | **96.5 km/h (26.8 m/s)** |
| Jarak terdekat (hit) | 7.5 m | 5.3 m | 3.6 m | 4.5 m | 8.4 m | 5.5 m | **5.8 m** |
| Ketinggian saat hit | 4.0 m | 1.8 m | 3.4 m | 1.6 m | 3.6 m | 1.2 m | **2.6 m** |
| Mean descent | 1.82 m/s | 1.64 m/s | 2.35 m/s | 2.33 m/s | 3.00 m/s | 3.12 m/s | **2.38 m/s** |
| Peak descent | 34.65 m/s | 29.44 m/s | 59.19 m/s | 33.95 m/s | 39.53 m/s | 53.51 m/s | **41.71 m/s** |
| Total alt drop | 55.3 m | 56.3 m | 77.2 m | 76.0 m | 95.7 m | 96.9 m | **76.2 m** |
| Mean pitch (locked) | -4.6° | -3.9° | -5.3° | -5.1° | -6.7° | -6.6° | **-5.4°** |
| Mean nav_pitch (locked) | -4.8° | -4.2° | -5.7° | -5.5° | -7.2° | -7.0° | **-5.7°** |
| Menabrak target? | Ya | Ya | Ya | Ya | Ya | Ya | **Ya (6/6)** |
| Respon servo | Sesuai | Sesuai | Sesuai | Sesuai | Sesuai | Sesuai | **Sesuai** |
| Frame rate | 21.3 FPS | 25.8 FPS | 26.4 FPS | 25.9 FPS | 23.3 FPS | 25.4 FPS | **24.7 FPS** |

**Catatan:**
- Akurasi tracking bervariasi antara 90.7%–100.0%. Run kanan cenderung lebih stabil (100% di 60m dan 80m, 99.7% di 100m); run kiri lebih bervariasi (90.7%–96.7%).
- Kecepatan nabrak meningkat seiring ketinggian lock (run kiri): 109.3 km/h (60m) → 113.4 km/h (80m) → 116.2 km/h (100m), konsisten dengan dive lebih curam dari ketinggian lebih tinggi.
- Run kanan 60m (16.7 km/h) menunjukkan kecepatan hit lebih rendah — disebabkan algoritma cut stage-2 menemukan titik alt_rel_m minimum saat drone sudah hampir menyentuh ground dan hampir berhenti secara vertikal; hit tetap berhasil berdasarkan dist_m ≤ 10 m.
- Mean pitch (locked) semakin negatif seiring ketinggian: ~-4° hingga -5° (60m) → ~-5° (80m) → ~-7° (100m), mencerminkan sudut dive yang semakin curam.
- Total alt drop mendekati ketinggian lock awal: ~55–56 m (60m), ~76–77 m (80m), ~96–98 m (100m) — drone berhasil menukik ke hampir ground level di ketiga kondisi.
- Peak descent bervariasi per run dan tidak monoton terhadap ketinggian; puncak tertinggi pada kiri 80m (59.19 m/s), diikuti kanan 100m (47.30 m/s).

---

## 10. Analisis Fase Terminal dari Ketinggian 80m

Pengujian dari ketinggian cruise **~80m di atas target** untuk mengevaluasi perbedaan karakteristik pendekatan dibanding sesi 60m. Dua run dianalisis: `tracking_kiri_80m.csv` dan `tracking_kanan_80m.csv`.

**Output ringkasan (`tracking_kiri_80m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 33.3 s  (874 rows)
  Target locked   : 845 rows  (96.7%)
  Track lost      : 29 rows  (3.3%)

  ── First track acquisition ──
  Time            : t+0.1 s
  Alt above target: 80.5 m
  Speed           : 88.1 km/h
  Distance        : 951.8 m

  ── Nearest point (hit) ──
  Time            : t+33.0 s
  Distance        : 3.6 m
  Speed at hit    : 113.4 km/h  (31.5 m/s)
  Alt at hit      : 3.4 m

  ── Descent ──
  Mean descent    : 2.35 m/s
  Peak descent    : 59.19 m/s
  Total alt drop  : 77.2 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -5.3 deg
  Mean nav_pitch  : -5.7 deg
───────────────────────────────────────────────────────
```

**Output ringkasan (`tracking_kanan_80m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 32.8 s  (843 rows)
  Target locked   : 843 rows  (100.0%)
  Track lost      : 0 rows  (0.0%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 77.7 m
  Speed           : 89.7 km/h
  Distance        : 955.9 m

  ── Nearest point (hit) ──
  Time            : t+32.5 s
  Distance        : 4.5 m
  Speed at hit    : 110.0 km/h  (30.6 m/s)
  Alt at hit      : 1.6 m

  ── Descent ──
  Mean descent    : 2.33 m/s
  Peak descent    : 33.95 m/s
  Total alt drop  : 76.0 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -5.1 deg
  Mean nav_pitch  : -5.5 deg
───────────────────────────────────────────────────────
```

**Deskripsi manuver (tracking_kiri_80m.csv):**

Seeker mengunci target pada t+0.1 s dari ketinggian **80.5 m** di atas target, jarak horizontal **951.8 m**, kecepatan **88.1 km/h**. Drone menjalani descent rata-rata **2.35 m/s** dengan puncak descent **59.19 m/s** saat fase terminal. Total penurunan ketinggian **77.2 m** dalam **33.0 detik**. Kecepatan saat menabrak **113.4 km/h** pada ketinggian **3.4 m** di atas target. Mean pitch **-5.3°** (nav_pitch: -5.7°) — lebih negatif dibanding sesi 60m, mencerminkan sudut dive yang lebih curam.

**Catatan:**
- Durasi fase terminal dari 80m (~33 s) serupa dengan 60m (~31–34 s); perbedaan terbesar terlihat pada mean descent dan total alt drop, bukan pada durasi.
- Peak descent kiri 80m (59.19 m/s) jauh lebih tinggi dari kanan 80m (33.95 m/s) — variasi ini mencerminkan perbedaan trajektori dive per run.
- Mean pitch -5.3°/-5.1° (80m) lebih negatif dari -4.6°/-3.9° (60m), konsisten dengan sudut depresi yang sedikit lebih besar dari ketinggian lebih tinggi.
- Kecepatan nabrak 80m (~110–113 km/h) lebih tinggi dari 60m (~109 km/h kiri; kanan 60m anomali).

**Hasil:** Kedua sesi 80m berhasil menabrak target. Akurasi tracking 96.7% (kiri) dan 100.0% (kanan).

---

## 11. Analisis Fase Terminal dari Ketinggian 100m

Pengujian dari ketinggian cruise **~100m di atas target** — ketinggian tertinggi yang diuji — untuk mengevaluasi karakteristik pendekatan dari sudut depresi terbesar. Dua run dianalisis: `tracking_kiri_100m.csv` dan `tracking_kanan_100m.csv`.

**Output ringkasan (`tracking_kiri_100m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 32.3 s  (741 rows)
  Target locked   : 702 rows  (94.7%)
  Track lost      : 39 rows  (5.3%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 99.3 m
  Speed           : 89.7 km/h
  Distance        : 954.6 m

  ── Nearest point (hit) ──
  Time            : t+32.0 s
  Distance        : 8.4 m
  Speed at hit    : 116.2 km/h  (32.3 m/s)
  Alt at hit      : 3.6 m

  ── Descent ──
  Mean descent    : 3.00 m/s
  Peak descent    : 39.53 m/s
  Total alt drop  : 95.7 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -6.7 deg
  Mean nav_pitch  : -7.2 deg
───────────────────────────────────────────────────────
```

**Output ringkasan (`tracking_kanan_100m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 31.3 s  (788 rows)
  Target locked   : 788 rows  (100.0%)
  Track lost      : 0 rows  (0.0%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 98.1 m
  Speed           : 90.6 km/h
  Distance        : 954.8 m

  ── Nearest point (hit) ──
  Time            : t+31.0 s
  Distance        : 5.5 m
  Speed at hit    : 113.6 km/h  (31.6 m/s)
  Alt at hit      : 1.2 m

  ── Descent ──
  Mean descent    : 3.12 m/s
  Peak descent    : 53.51 m/s
  Total alt drop  : 96.9 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -6.6 deg
  Mean nav_pitch  : -7.0 deg
───────────────────────────────────────────────────────
```

**Deskripsi manuver (tracking_kiri_100m.csv):**

Seeker langsung mengunci target pada t+0.0 s dari ketinggian **99.3 m** di atas target, jarak horizontal **954.6 m**, kecepatan **89.7 km/h**. Dengan sudut depresi terbesar dari ketiga ketinggian yang diuji, PID pitch menerima sinyal koreksi ey_raw yang lebih besar sejak awal lock. Drone menjalani descent rata-rata **3.00 m/s** dengan puncak descent **39.53 m/s**. Total penurunan ketinggian **95.7 m** dalam **32.0 detik**. Kecepatan saat menabrak **116.2 km/h** (32.3 m/s) pada ketinggian **3.6 m** di atas target. Mean pitch **-6.7°** (nav_pitch: -7.2°) — paling negatif di antara semua sesi, mencerminkan nose-down lebih dalam akibat ey_raw besar dari ketinggian 100m.

**Catatan:**
- Mean descent 100m (~3.0–3.1 m/s) lebih tinggi dari 80m (~2.3 m/s) dan 60m (~1.7 m/s), konsisten dengan peningkatan sudut depresi seiring ketinggian lock.
- Total alt drop ~95–97 m mendekati ketinggian lock awal (~98–99 m) — drone berhasil menukik hingga hampir ground level.
- Kedua run 100m mencapai kecepatan hit normal: kiri **116.2 km/h**, kanan **113.6 km/h** — tertinggi di antara semua run.
- Akurasi tracking kiri 94.7%, kanan 100.0%; run kanan 100m tidak kehilangan lock sekalipun sepanjang 788 frame.

**Hasil:** Kedua sesi 100m berhasil menabrak target. Akurasi tracking 94.7% (kiri) dan 100.0% (kanan). Mean descent tertinggi di antara semua ketinggian yang diuji.

---

## 12. Kendala dan Solusi

| No | Kendala | Solusi |
|---|---|---|
| 1 | Rekaman video menyebabkan hang pada main loop | Ganti OpenCV VideoWriter dengan FFmpeg subprocess pipe; write ke stdin non-blocking |
| 2 | Webcam tidak terdeteksi pada index 0 | Cek `ls /dev/video*` dan sesuaikan `--source` |
| 3 | TRACKING_MESSAGE tidak diterima Pixhawk | Verifikasi dialect `ardupilotmega` terload di mavutil; pastikan UDP port 14560 sesuai |
| 4 | Seeker masuk TRACKING sebelum waktunya | Tambahkan gate: `in_auto AND on_last_wp AND close_enough` sebelum transisi |
| 5 | FPS tidak stabil saat recording dimulai | Tambahkan warmup 30 frame sebelum membuka VideoWriter |

---

## 13. Rencana Tindak Lanjut

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
| 9 | Analisis ulang fase terminal `terminal_analyse.py` (60m) — kiri & kanan | ✅ Selesai |
| 10 | Analisis ulang fase terminal dari ketinggian 80m — kiri & kanan | ✅ Selesai |
| 11 | Analisis fase terminal dari ketinggian 100m — kiri & kanan | ✅ Selesai |
| 12 | Simulasi HITL end-to-end: takeoff → cruise → terminal — drone menabrak target | ✅ **Berhasil** |

*Logbook ditulis oleh: Muhammad Ihsan Fahriansyah & Musa El Hanafi*
