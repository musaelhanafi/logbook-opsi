# Logbook Kegiatan — 17 April 2026

| | |
|---|---|
| **Penelitian** | Sistem Kendali Drone Kamikaze Berbasis Deteksi Objek Warna dalam Simulasi HITL |
| **Tim** | Musa El Hanafi & Muhammad Ihsan Fahriansyah |
| **Lokasi** | Lab Komputer SMA Swasta Alfa Centauri, Kota Bandung |
| **Hari/Tanggal** | Kamis, 17 April 2026 |

---

## 1. Implementasi Board Config HITL — fmuv3-hil, fmuv3-hil-plane, x86-hil

**Kegiatan:**
Membuat tiga konfigurasi board baru di firmware drone-kamikaze untuk mendukung mode HITL (Hardware-in-the-Loop) dengan X-Plane sebagai physics engine.

### A. fmuv3-hil (Pixhawk — Flying Wing Elevon)

**File:** `libraries/AP_HAL_ChibiOS/hwdef/fmuv3-hil/hwdef.dat` dan `defaults.parm`

Konfigurasi untuk Pixhawk (fmuv3) dengan koneksi PPP over TELEM2 ke laptop yang menjalankan X-Plane. Digunakan untuk flying wing (elevon).

**Parameter utama `defaults.parm`:**

| Parameter | Nilai | Keterangan |
|---|---|---|
| `AHRS_EKF_TYPE` | 2 | EKF2 (sesuai keterbatasan STM32F427) |
| `EK2_ENABLE` | 1 | EKF2 aktif |
| `EK3_ENABLE` | 0 | EKF3 nonaktif |
| `GPS1_TYPE` | 100 | SITL GPS |
| `ARSPD_TYPE` | 100 | SITL airspeed |
| `NET_ENABLE` | 1 | PPP networking aktif |
| `SERIAL2_PROTOCOL` | 48 | PPP protocol di TELEM2 |
| `SERIAL2_BAUD` | 115 | 115200 baud |
| `NET_OPTIONS` | 64 | PPP options |
| `SIM_OPOS_LAT` | −6.897434 | Bandara WICC — Bandung |
| `SIM_OPOS_LNG` | 107.566887 | |
| `SIM_OPOS_ALT` | 744.0 | AMSL (m) |

### B. fmuv3-hil-plane (Pixhawk — Fixed Wing Konvensional)

**File:** `libraries/AP_HAL_ChibiOS/hwdef/fmuv3-hil-plane/hwdef.dat` dan `defaults.parm`

Sama dengan fmuv3-hil tetapi menggunakan `xplane_plane.json` (aileron/elevator/throttle/rudder terpisah).

**Tambahan `defaults.parm`:**

| Parameter | Nilai | Keterangan |
|---|---|---|
| `SERVO1_FUNCTION` | 4 | Aileron |
| `SERVO2_FUNCTION` | 19 | Elevator |
| `SERVO3_FUNCTION` | 70 | Throttle |
| `SERVO4_FUNCTION` | 21 | Rudder |

### C. x86-hil (SITL Binary — Laptop/x86)

**File:** `libraries/AP_HAL_SITL/hwdef/x86-hil/hwdef.dat` dan `defaults.parm`

Konfigurasi untuk menjalankan ArduPlane sebagai SITL binary di laptop yang sama dengan X-Plane. Tidak memerlukan PPP — koneksi UDP langsung.

---

## 2. Implementasi Mode TRACKING (Mode 27)

**Kegiatan:**
Mengimplementasikan flight mode baru `ModeTracking` (mode nomor 27) di ArduPlane drone-kamikaze untuk tracking target menggunakan error piksel dari seeker.

**File yang dimodifikasi/dibuat:**

| File | Perubahan |
|---|---|
| `ArduPlane/mode_tracking.cpp` | Implementasi PID roll/pitch + Kalman filter throttle |
| `ArduPlane/mode.h` | Tambah `TRACKING = 27` di enum dan class `ModeTracking` |
| `ArduPlane/Plane.h` | Tambah `friend class ModeTracking`, `ModeTracking mode_tracking`, `TrackingState` struct |
| `ArduPlane/control_modes.cpp` | Tambah case `TRACKING` |
| `ArduPlane/GCS_MAVLink_Plane.cpp` | Handler `TRACKING_MESSAGE`, PID streaming |
| `ArduPlane/Parameters.h` / `.cpp` | 22 parameter tracking (PID, timeout, target, Kalman) |
| `ArduPlane/GCS_Plane.cpp` | Fix `-Wswitch`: tambah case `TRACKING` |
| `ArduPlane/events.cpp` | Fix `-Wswitch`: tambah case `TRACKING` di short & long failsafe |

### Parameter Mode Tracking

| Parameter | Default | Keterangan |
|---|---|---|
| `TRK_ROLL_P` | 200.0 | Roll PID — P gain |
| `TRK_ROLL_I` | 10.0 | Roll PID — I gain |
| `TRK_ROLL_D` | 5.0 | Roll PID — D gain |
| `TRK_PTCH_P` | 100.0 | Pitch PID — P gain |
| `TRK_PTCH_I` | 500.0 | Pitch PID — I gain |
| `TRK_MAX_DEG` | — | Batas defleksi roll/pitch (deg) |
| `TRK_DBAND_DEG` | — | Deadband error (deg) |
| `TRK_PTCH_OFS` | — | Pitch offset dari horizon (deg) |
| `TRK_TIMEOUT_MS` | — | Timeout sinyal tracking (ms) |
| `TRK_TERM_ALT` | — | Altitude terminal dive (m) |
| `TRK_TERM_PTCH` | — | Pitch angle terminal dive (deg) |
| `TRK_APP_SPD` | — | Target approach speed (m/s) |
| `TRK_SETTLE_S` | — | Waktu stable lock sebelum terminal (s) |
| `TRK_TGT_LAT` | −6.897368 | Latitude target (decimal deg) |
| `TRK_TGT_LON` | 107.566560 | Longitude target (decimal deg) |
| `TRK_TGT_ALT` | 744.0 | Altitude target AMSL (m) |
| `TRK_THR_LEAD` | — | Throttle feed-forward lead |
| `TRK_KF_Q` | — | Kalman process noise |
| `TRK_KF_R` | — | Kalman measurement noise |
| `TRK_THR_P` | 10.0 | Throttle PID — P gain |
| `TRK_THR_I` | 2.0 | Throttle PID — I gain |

---

## 3. Implementasi MAVLink TRACKING_MESSAGE (ID 11045)

**Kegiatan:**
Menambahkan custom MAVLink message `TRACKING_MESSAGE` untuk menerima error piksel dari Python seeker ke ArduPlane.

**Spesifikasi pesan:**

| Field | Tipe | Keterangan |
|---|---|---|
| `time_usec` | uint64 | Timestamp (µs) |
| `errorx` | float | Error horizontal (rad) |
| `errory` | float | Error vertikal (rad) |

**Handler:** `GCS_MAVLink_Plane::handle_tracking_message()` menyimpan ke `plane.tracking_state` yang dibaca oleh `ModeTracking::update()`.

---

## 4. File xplane_elevon.json

**Kegiatan:**
Membuat file DREF map baru untuk flying wing (elevon) yang digunakan oleh board x86-hil dan fmuv3-hil.

**File:** `Tools/autotest/models/xplane_elevon.json`

**Prinsip kerja:**
SIM_XPlane.cpp melakukan demix servo sebelum mengirim ke X-Plane:

| DRef X-Plane | Tipe | Formula (SIM_XPlane.cpp) |
|---|---|---|
| `sim/joystick/yoke_roll_ratio` | `elevon_aileron` | `(CH1_left − CH2_right) / 1000` |
| `sim/joystick/yoke_pitch_ratio` | `elevon_elevator` | `(CH1_left + CH2_right − 3000) / 1000 + 0.5` |
| `sim/flightmodel/engine/ENGN_thro_use[0]` | `range` | `(CH3 − 1000) / 1000` |

**Channel mapping:**

| Channel | Servo | Keterangan |
|---|---|---|
| `channel: 1` | SERVO1 | Left elevon (CH1) |
| `channel2: 2` | SERVO2 | Right elevon (CH2) |
| `channel: 3` | SERVO3 | Throttle |

---

## 5. Konfigurasi Parameter SITL X-Plane (x86-hil)

**Kegiatan:**
Verifikasi dan dokumentasi seluruh parameter ArduPilot yang relevan untuk konfigurasi SITL dengan X-Plane backend.

---

### 5.1 Parameter X-Plane Spesifik

| Parameter | Default | Keterangan |
|---|---|---|
| `SIM_XP_BIND_PORT` | 0 → 49001 | Port UDP yang didengarkan ArduPilot dari X-Plane. 0 = gunakan default 49001. Menimpa port dari argument `--model xplane:ip:port`. |

---

### 5.2 Parameter yang Di-set Otomatis oleh Constructor SIM_XPlane

Constructor `XPlane::XPlane()` memanggil `AP_Param::set_default_by_name()` untuk nilai-nilai berikut. Dapat ditimpa di `defaults.parm`.

| Parameter | Default Constructor | Nilai Rekomendasi | Keterangan |
|---|---|---|---|
| `AHRS_EKF_TYPE` | **10** (SIM/direct) | **10** | Attitude langsung dari X-Plane. Jangan ubah ke 3 (EKF3) karena menyebabkan compass tidak sinkron. |
| `GPS1_TYPE` | 100 | 100 | SITL GPS backend |
| `INS_GYR_CAL` | 0 (skip) | 0 | Skip kalibrasi gyro saat startup |
| `SERVO5_FUNCTION` | 3 (flaps) | sesuai kebutuhan | ArduPlane: default flaps di channel 5 |
| `SERVO5_MIN` | 1000 | 1000 | |
| `SERVO5_MAX` | 2000 | 2000 | |

---

### 5.3 Parameter Home / Origin

Harus disesuaikan dengan posisi pesawat di X-Plane. Jika tidak di-set, EKF tidak akan konvergen (GPS menunjuk 0°N 0°E).

| Parameter | Nilai (WICC Bandung) | Keterangan |
|---|---|---|
| `SIM_OPOS_LAT` | −6.897434 | Latitude startup (decimal deg) |
| `SIM_OPOS_LNG` | 107.566887 | Longitude startup (decimal deg) |
| `SIM_OPOS_ALT` | 744.0 | Altitude AMSL (m) |
| `SIM_OPOS_HDG` | 108.0 | Heading startup (0–360°) |

---

### 5.4 Parameter Sensor Backend

| Parameter | Nilai | Keterangan |
|---|---|---|
| `GPS1_TYPE` | 100 | SITL GPS — diisi dari X-Plane frame `LatLonAlt` + `LocVelDistTraveled` |
| `ARSPD_TYPE` | 100 | SITL airspeed — dari X-Plane frame `Speed` |

**Compass — tidak ada `COMPASS_TYPE`:**
Di binary SITL, `AP_Compass_SITL` dibuat otomatis untuk setiap `SIM_MAGx_DEVID` yang bernilai **non-nol** (default ada 7 compass phantom). Cukup aktifkan satu.

| Parameter | Nilai | Keterangan |
|---|---|---|
| `COMPASS_USE` | 1 | Gunakan compass 1 |
| `COMPASS_USE2` | 0 | Nonaktifkan compass 2 |
| `COMPASS_USE3` | 0 | Nonaktifkan compass 3 |
| `SIM_MAG1_DEVID` | 97539 | Non-nol = compass 1 aktif (default) |
| `SIM_MAG2_DEVID` | **0** | Nol = tidak membuat instance compass 2 |
| `SIM_MAG3_DEVID` | **0** | Nol = tidak membuat instance compass 3 |

> **Catatan teknis:** Compass SITL membaca dari `sitl->state.bodyMagField` yang dihitung oleh `update_mag_field_bf()` menggunakan DCM dari X-Plane dan model medan magnet bumi (WMM) di posisi simulasi. Dengan `AHRS_EKF_TYPE 10`, compass **tidak** digunakan untuk estimasi heading — heading langsung dari `fdm.quaternion` X-Plane.

---

### 5.5 Parameter AHRS / EKF

| Parameter | Nilai | Keterangan |
|---|---|---|
| `AHRS_EKF_TYPE` | **10** | **SIM backend** — attitude dari `fdm.quaternion` X-Plane, zero-lag. |
| `EK3_ENABLE` | 1 | EKF3 tetap aktif (untuk terrain, odometry) |
| `EK2_ENABLE` | 0 | EKF2 nonaktif |
| `EK3_SRC1_YAW` | 2 | *Hanya jika `AHRS_EKF_TYPE 3`*: gunakan GPS velocity untuk estimasi yaw bukan compass |

**Mengapa `AHRS_EKF_TYPE 10`:**

```
X-Plane PitchRollHeading
  → dcm.from_euler(roll, pitch, yaw)      [SIM_XPlane.cpp]
  → sitl->state.quaternion               [update_position()]
  → fdm.quaternion → yaw_rad             [AP_AHRS_SIM::get_results()]
  → AHRS yaw  ← yang dipakai HUD & navigasi
```

Dengan `AHRS_EKF_TYPE 3` (EKF3), heading harus konvergen melalui fusi gyro + compass — dapat lag atau diverge dari heading X-Plane. Constructor `SIM_XPlane` sendiri mengomentari: *"XPlane sensor data is not good enough for EKF. Use fake EKF by default."*

---

### 5.6 Parameter Kontrol Simulasi

| Parameter | Nilai | Keterangan |
|---|---|---|
| `SIM_SPEEDUP` | **1** | Wajib 1 — X-Plane berjalan real-time |
| `SIM_OH_MASK` | 255 (fmuv3) / 0 (x86) | Bitmask channel servo yang diteruskan ke hardware fisik |
| `SIM_RC_FAIL` | 0 | 0=normal, 1=simulasi RC loss |

---

### 5.7 Parameter Angin / Lingkungan (Opsional)

X-Plane juga punya pengaturan angin sendiri. Jika keduanya aktif, efeknya terjumlah.

| Parameter | Default | Keterangan |
|---|---|---|
| `SIM_WIND_SPD` | 0 | Kecepatan angin simulasi (m/s) |
| `SIM_WIND_DIR` | 180 | Arah angin datang (0–360°) |
| `SIM_WIND_TURB` | 0 | Turbulensi angin (m/s) |
| `SIM_WIND_TC` | 5 | Time constant perubahan angin (s) |
| `SIM_BATT_VOLTAGE` | 12.6 | Tegangan baterai simulasi (V) |
| `SIM_BATT_CAP_AH` | 0 | Kapasitas baterai simulasi (Ah), 0 = unlimited |

---

### 5.8 Parameter Noise / Fault Compass (Untuk Uji Fault Detection)

| Parameter | Default | Keterangan |
|---|---|---|
| `SIM_MAG_RND` | 0 | Faktor noise magnetometer |
| `SIM_MAG1_OFS` | 0,0,0 | Offset hard-iron compass 1 (mGauss) |
| `SIM_MAG1_ORIENT` | 0 | Orientasi compass 1 (enum Rotation) |
| `SIM_MAG1_FAIL` | 0 | 0=normal, 1=no data, 2=frozen |
| `SIM_MAG1_SCALING` | 1.0 | Faktor skala compass 1 |

---

### 5.9 Ringkasan defaults.parm x86-hil

```
# AHRS
AHRS_EKF_TYPE  10
EK3_ENABLE      1
EK2_ENABLE      0

# Sensor backends
GPS1_TYPE     100
ARSPD_TYPE    100

# Compass
COMPASS_USE     1
COMPASS_USE2    0
COMPASS_USE3    0
SIM_MAG2_DEVID  0
SIM_MAG3_DEVID  0

# Home position (WICC Bandung)
SIM_OPOS_LAT   -6.897434
SIM_OPOS_LNG  107.566887
SIM_OPOS_ALT  744.0
SIM_OPOS_HDG  108.0

# Simulasi
SIM_SPEEDUP     1
SIM_OH_MASK     0     # x86: tidak ada hardware output

# RC
THR_FAILSAFE    0
RC_OVERRIDE_TIME -1

# Arming
BRD_SAFETY_DEFLT 0
ARMING_SKIPCHK  -1
ARMING_REQUIRE   1

# Takeoff
TKOFF_THR_MINACC 0
TKOFF_THR_MINSPD 0
TKOFF_ROTATE_SPD 12

# X-Plane bind port (opsional — jika ingin ganti dari 49001)
# SIM_XP_BIND_PORT 49001
```

---

## 6. Manual Fix & Autotune FX-61 — Minimasi Pitch Jitter

**Kegiatan:**
Melakukan perbaikan parameter manual untuk mengurangi pitch jitter pada FX-61 Phantom sebelum menjalankan Autotune ArduPlane. Urutan ini penting — Autotune tidak dapat bekerja optimal jika pitch jitter belum diminimasi secara manual terlebih dahulu.

---

### 6.1 Root Cause Pitch Jitter pada FX-61

Pitch jitter pada flying wing seperti FX-61 umumnya disebabkan oleh kombinasi faktor berikut:

| Penyebab | Parameter ArduPlane | Dampak |
|---|---|---|
| Gain PID pitch terlalu tinggi | `PTCH_RATE_P`, `PTCH_RATE_D` | Osilasi cepat di axis pitch |
| TECS terlalu agresif | `TECS_PTCH_DAMP`, `TECS_TIME_CONST` | Hunting panjang saat altitude hold |
| Vibrasi motor masuk ke gyro | `INS_HNTCH_ENABLE` | Noise frekuensi tinggi di sensor |
| Filter gyro kurang kuat | `INS_GYRO_FILTER` | Noise tidak tersaring |
| Respon elevon terlalu sensitif | `MIXING_GAIN` | Over-correction tiap frame |

---

### 6.2 Manual Fix (Lakukan Sebelum Autotune)

Set parameter berikut via QGroundControl **sebelum** terbang Autotune. Masuk ke **Vehicle Setup → Parameters**, cari nama parameter, ubah nilainya.

#### Step A — TECS (Paling Berpengaruh untuk Pitch Hunting)

| Parameter | Nilai Lama | **Nilai Baru** | Alasan |
|---|---|---|---|
| `TECS_PTCH_DAMP` | 0.0 | **0.30** | Tambah damping pitch di TECS |
| `TECS_TIME_CONST` | 5.0 | **7.0** | Perlambat respon TECS untuk flying wing |
| `TECS_THR_DAMP` | 0.1 | **0.50** | Damping throttle agar tidak fight pitch |
| `TECS_VERT_ACC` | 7.0 | **6.0** | Kurangi akselerasi vertikal maksimum |

#### Step B — Pitch Rate PID (Turunkan Gain Awal)

| Parameter | Nilai Lama | **Nilai Baru** | Alasan |
|---|---|---|---|
| `PTCH_RATE_P` | 0.10 | **0.07** | Turunkan P untuk kurangi osilasi |
| `PTCH_RATE_I` | 0.10 | **0.08** | Turunkan I agar tidak windup |
| `PTCH_RATE_D` | 0.001 | **0.002** | Naikkan D sedikit untuk damping |
| `PTCH_RATE_FF` | 0.0 | **0.18** | Tambah feedforward untuk respon halus |
| `PTCH_RATE_FLTE` | 0.0 | **2.0** | Filter error pitch — kunci anti-jitter |
| `PTCH_RATE_FLTD` | 0.0 | **10.0** | Filter derivative pitch |

#### Step C — Pitch Attitude Controller

| Parameter | Nilai Lama | **Nilai Baru** | Alasan |
|---|---|---|---|
| `PTCH2SRV_TCONST` | 0.5 | **0.60** | Perlambat respon attitude pitch |
| `PTCH2SRV_P` | 1.0 | **0.90** | Turunkan P attitude |
| `PTCH2SRV_D` | 0.0 | **0.06** | Tambah D untuk damping |

#### Step D — Notch Filter (Vibrasi Motor)

| Parameter | Nilai | Keterangan |
|---|---|---|
| `INS_HNTCH_ENABLE` | **1** | Aktifkan harmonic notch filter |
| `INS_HNTCH_FREQ` | **100** | Estimasi frekuensi motor FX-61 (8–9 in prop) |
| `INS_HNTCH_BW` | **50** | Bandwidth filter = setengah frekuensi |
| `INS_HNTCH_ATT` | **40** | Atenuasi 40 dB |
| `INS_HNTCH_MODE` | **1** | Mode throttle-based (tanpa ESC telemetry) |
| `INS_HNTCH_HMNCS` | **3** | Filter harmonik 1 dan 2 |

#### Step E — Filter Gyro

| Parameter | Nilai Lama | **Nilai Baru** | Alasan |
|---|---|---|---|
| `INS_GYRO_FILTER` | 20 | **15** | Filter lebih kuat untuk FX-61 yang ringan |
| `INS_ACCEL_FILTER` | 20 | **15** | Filter akselerometer |

#### Step F — Elevon & Airspeed

| Parameter | Nilai Lama | **Nilai Baru** | Alasan |
|---|---|---|---|
| `MIXING_GAIN` | 0.5 | **0.45** | Kurangi sensitivitas elevon |
| `ARSPD_FBW_MIN` | 9 | **11** | Batas airspeed minimum (m/s) |
| `ARSPD_FBW_MAX` | 22 | **22** | Batas airspeed maksimum (m/s) |
| `TRIM_ARSPD_CM` | 1500 | **1500** | Kecepatan cruise target (cm/s) |
| `STALL_PREVENTION` | 0 | **1** | Aktifkan stall prevention |

---

### 6.3 Verifikasi Manual Fix (Test Flight Pertama)

Setelah semua parameter di-set, lakukan test flight singkat dalam mode FBWA **sebelum** Autotune:

**Langkah:**

1. Terbangkan FX-61 dalam mode **FBWA** di ketinggian aman (>100 m AGL)
2. Lepas stick — biarkan pesawat terbang level tanpa input
3. Observasi selama 30 detik:

| Yang Diobservasi | Kondisi Buruk (jitter) | Kondisi Baik (siap autotune) |
|---|---|---|
| Gerak pitch | Osilasi terus-menerus | Stabil atau osilasi sangat kecil |
| Gerak roll | Hunting kiri-kanan | Level stabil |
| Throttle | Naik-turun konstan | Relatif konstan |
| Altitude | Berfluktuasi >5 m | Stabil dalam ±3 m |

4. Jika masih jitter berat: turunkan `PTCH_RATE_P` sebesar 0.01 per iterasi hingga stabil
5. Jika sudah stabil: lanjut ke langkah Autotune (6.4)

> **Catatan:** Jangan jalankan Autotune jika jitter masih parah — Autotune akan menghasilkan gain yang salah karena mengidentifikasi osilasi buatan sebagai respon sistem yang valid.

---

### Pra-langkah: Konfigurasi Channel 5 RC — MANUAL / STABILIZE / AUTOTUNE

Sebelum menjalankan Autotune, pastikan RC channel 5 sudah dikonfigurasi sebagai 3-position flight mode switch. Ini memungkinkan pilot switch antar mode secara fisik dari transmitter tanpa menyentuh QGC.

#### A. Set Flight Mode Channel

| Parameter | Nilai | Keterangan |
|---|---|---|
| `FLTMODE_CH` | **5** | Channel RC yang digunakan untuk flight mode switch |

#### B. Mapping 3-Position Switch ke Flight Mode

ArduPlane memetakan 6 slot mode (`FLTMODE1`–`FLTMODE6`) ke rentang PWM channel 5. Untuk switch 3-posisi (PWM ≈ 1000 / 1500 / 2000), set pasangan slot berikut:

| Slot | Parameter | Nilai | Mode | Rentang PWM |
|---|---|---|---|---|
| Posisi 1 (bawah) | `FLTMODE1` | **0** | MANUAL | 1000 – 1230 |
| | `FLTMODE2` | **0** | MANUAL | 1231 – 1360 |
| Posisi 2 (tengah) | `FLTMODE3` | **2** | STABILIZE | 1361 – 1490 |
| | `FLTMODE4` | **2** | STABILIZE | 1491 – 1620 |
| Posisi 3 (atas) | `FLTMODE5` | **8** | AUTOTUNE | 1621 – 1749 |
| | `FLTMODE6` | **8** | AUTOTUNE | 1750 – 2000 |

> **Kode mode ArduPlane:** MANUAL = 0, STABILIZE = 2, AUTOTUNE = 8.

#### C. Langkah Set di QGroundControl

1. Buka **Vehicle Setup → Parameters**
2. Cari dan set `FLTMODE_CH = 5`
3. Set `FLTMODE1` s.d. `FLTMODE6` sesuai tabel di atas
4. Reboot Pixhawk
5. Verifikasi di **QGC Fly View → Flight Mode indicator**: gerakkan switch transmitter, pastikan mode berganti sesuai posisi

#### D. Verifikasi di Lapangan (Sebelum Arm)

| Posisi Switch | Mode yang Harus Muncul di QGC |
|---|---|
| Bawah | MANUAL |
| Tengah | STABILIZE |
| Atas | AUTOTUNE |

> **Penting:** Pastikan switch berada di posisi **MANUAL** atau **STABILIZE** saat arm. Jangan arm dalam kondisi AUTOTUNE — ArduPlane akan menolak arm jika `ARMING_REQUIRE = 1` dan mode tidak mendukung takeoff manual.

---

### 6.4 Menjalankan Autotune

Setelah manual fix berhasil menstabilkan pitch, jalankan Autotune untuk mendapatkan gain optimal secara otomatis.

**Parameter Autotune:**

| Parameter | Nilai | Keterangan |
|---|---|---|
| `AUTOTUNE_LEVEL` | **6** | Agresivitas tuning 1–10, nilai 6 sesuai untuk flying wing |
| `AUTOTUNE_OPTIONS` | **0** | Tune semua axis (roll + pitch) |

**Langkah Autotune:**

1. Set `AUTOTUNE_LEVEL = 6` di QGroundControl Parameters
2. Terbangkan FX-61 dalam mode **FBWA** — naik ke ketinggian aman minimal **150 m AGL**
3. Pastikan area terbang cukup luas (radius >200 m) karena Autotune akan melakukan manuver otomatis
4. Switch mode ke **AUTOTUNE** via QGroundControl:
   - QGC Fly View → dropdown flight mode → pilih **AUTOTUNE**
5. ArduPlane mulai melakukan manuver identifikasi secara otomatis:

   | Fase | Yang Terjadi |
   |---|---|
   | Roll sweep | Pesawat melakukan roll kiri-kanan berulang untuk identifikasi gain roll |
   | Pitch sweep | Pesawat melakukan pitch up-down berulang untuk identifikasi gain pitch |
   | Konvergensi | Gain diperhalus — manuver semakin kecil amplitudonya |

6. Monitor di QGC — Autotune selesai ditandai dengan:
   - Alert di QGC: **"Autotune complete"**
   - Manuver otomatis berhenti
   - Pesawat kembali ke attitude normal FBWA
7. **Jangan langsung land** — setelah alert muncul, biarkan pesawat terbang dalam AUTOTUNE mode selama 30 detik lagi untuk stabilisasi
8. Switch kembali ke **FBWA** — lakukan test flight singkat untuk verifikasi respon
9. Jika respon terasa baik: land dan simpan parameter

**Menyimpan hasil Autotune:**

```
QGroundControl → Vehicle Setup → Parameters
→ Tools (ikon titik tiga) → Save to file
→ Simpan sebagai: FX61_autotune_result.params
```

Atau simpan ke Pixhawk permanen:

```
Parameters → Tools → Save to Vehicle (permanent)
```

---

### 6.5 Verifikasi Post-Autotune

Setelah Autotune selesai, cek nilai gain hasil tuning:

| Parameter | Range Normal FX-61 | Jika Diluar Range |
|---|---|---|
| `PTCH_RATE_P` | 0.05 – 0.12 | Ulangi Autotune dengan level lebih rendah |
| `PTCH_RATE_D` | 0.001 – 0.005 | Periksa vibrasi motor |
| `RLL_RATE_P` | 0.05 – 0.15 | Normal untuk flying wing |
| `RLL_RATE_D` | 0.001 – 0.004 | Periksa vibrasi motor |

**Test flight post-autotune:**

1. Terbang dalam mode FBWA — lepas stick, observasi attitude
2. Berikan input pitch mendadak — pesawat harus kembali level dalam 1–2 detik tanpa osilasi
3. Berikan input roll mendadak — respon harus smooth tanpa overshoot berlebihan
4. Aktifkan mode **LOITER** — pesawat harus bisa loiter stabil tanpa pitch hunting

---

### 6.6 Troubleshooting Post-Autotune

| Gejala | Kemungkinan Penyebab | Solusi |
|---|---|---|
| Pitch jitter masih ada | `PTCH_RATE_D` terlalu rendah | Naikkan `PTCH_RATE_D` sebesar 0.001 per iterasi |
| Respon pitch terlalu lambat | `PTCH2SRV_TCONST` terlalu besar | Turunkan dari 0.60 ke 0.55 |
| Osilasi lambat (hunting) | `TECS_TIME_CONST` masih terlalu kecil | Naikkan ke 8.0 atau 9.0 |
| Autotune menghasilkan P sangat tinggi | Vibrasi motor mengganggu identifikasi | Pastikan `INS_HNTCH_ENABLE = 1` dan frekuensi benar |
| Alert "Autotune failed" | Area terbang terlalu sempit | Cari area lebih luas, ulangi |

---

### 6.7 Ringkasan Urutan Lengkap

```
Step A → Set TECS parameters (TECS_PTCH_DAMP, TECS_TIME_CONST)
Step B → Set PTCH_RATE parameters (turunkan P, tambah D dan FLTE)
Step C → Set PTCH2SRV parameters (TCONST, D)
Step D → Aktifkan Notch Filter (INS_HNTCH_ENABLE = 1)
Step E → Turunkan INS_GYRO_FILTER ke 15
Step F → Set MIXING_GAIN dan airspeed limits
          ↓
Test flight FBWA → verifikasi jitter berkurang
          ↓
Set AUTOTUNE_LEVEL = 6
Terbang FBWA → switch ke AUTOTUNE → tunggu "Autotune complete"
          ↓
Test flight post-autotune → verifikasi respon pitch halus
          ↓
Simpan parameter ke file dan ke Pixhawk
```

---

## Ringkasan Kegiatan

| No | Kegiatan | Status |
|---|---|---|
| 1 | Board config HITL: fmuv3-hil, fmuv3-hil-plane, x86-hil | ✅ Selesai |
| 2 | Implementasi ModeTracking (mode 27) + Parameters | ✅ Selesai |
| 3 | Implementasi MAVLink TRACKING_MESSAGE (ID 11045) | ✅ Selesai |
| 4 | File xplane_elevon.json (demix elevon untuk X-Plane) | ✅ Selesai |
| 5 | Fix -Wswitch build error (GCS_Plane.cpp, events.cpp) | ✅ Selesai |
| 6 | Fix AHRS_EKF_TYPE: compass tidak sinkron dengan X-Plane | ✅ Selesai |
| 7 | Konfigurasi compass SITL (SIM_MAGx_DEVID) | ✅ Selesai |
| 8 | Dokumentasi seluruh parameter SITL X-Plane | ✅ Selesai |
| 9 | Manual fix parameter + Autotune FX-61 (minimasi pitch jitter) | ✅ Selesai |

---

*Logbook dibuat: 17 April 2026 | Penelitian OPSI 2026 — SMA Swasta Alfa Centauri*
