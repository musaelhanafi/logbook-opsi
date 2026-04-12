# Logbook Kegiatan — 17 April 2026

| | |
|---|---|
| **Penelitian** | Sistem Kendali Drone Kamikaze Berbasis Deteksi Objek Warna dalam Simulasi HITL |
| **Tim** | Musa El Hanafi & Muhammad Ihsan Fahriansyah |
| **Lokasi** | Lab Komputer SMA Swasta Alfa Centauri, Kota Bandung |
| **Hari/Tanggal** | Kamis, 17 April 2026 |

---

## Arsitektur Sistem

Sebelum memulai setup environment, dipelajari arsitektur lengkap sistem drone kamikaze yang terdiri dari dua subsistem utama.

### Gambaran Umum

Sistem terdiri dari dua repo yang bekerja bersama:

| Repo | Peran |
|---|---|
| **drone-seeker** | Pelacak target hot-pink berbasis Python + kamera, berjalan di companion PC |
| **drone-kamikaze** | Firmware ArduPlane custom untuk Pixhawk, mengeksekusi kendali terbang |

### Arsitektur HITL

HITL (Hardware-in-the-Loop) menggunakan Pixhawk v2 (fmuv3) yang menjalankan firmware ArduPlane custom. X-Plane menyediakan model fisika penerbangan; Pixhawk menjalankan kode autopilot nyata. Injeksi sensor dan output aktuator ditangani sepenuhnya **di dalam firmware** via SITL XPlane backend — tidak memerlukan bridge script atau MAVProxy.

![HITL Architecture Diagram](chart_02_initial_architecture.png)

![HITL Physical Layout](chart_00_physical_layout.png)

**Aliran data:**

| Arah | Jalur | Konten |
|---|---|---|
| X-Plane → Pixhawk | UDP → PPP (TELEM2) | DATA@ rows (IMU, GPS, airspeed, attitude) |
| Pixhawk → X-Plane | PPP (TELEM2) → UDP | DREF packets (yoke ratios, throttle) |
| QGC ↔ Pixhawk | USB (SERIAL0) | MAVLink2 telemetry, parameter, misi |
| RC Transmitter → Pixhawk | 2.4 GHz radio + SBUS/PPM | Input stick RC |

**SIM_XPlane backend** (`SIM_XPlane.cpp`) berjalan di Pixhawk dan:
- Mendecode DATA@ rows masuk → populate `SIMState` (injeksi sensor)
- Membaca `input.servos[]` tiap siklus → mengirim DREF packets ke X-Plane
- Menggunakan `xplane_plane.json` (embedded di firmware ROMFS) untuk memetakan servo channel ke DREF X-Plane

**Koneksi fisik:**

| Kabel | Dari | Ke |
|---|---|---|
| USB-A → micro-B | Laptop | Pixhawk USB (SERIAL0) |
| USB–UART adapter | Laptop (pppd) | Pixhawk TELEM2 (SERIAL2) @ 115200 baud |

X-Plane dan QGC berjalan di laptop yang sama.

**DREF mapping (`xplane_plane.json`):**

| Channel | DREF | Tipe |
|---|---|---|
| CH1 (aileron) | `sim/joystick/yoke_roll_ratio` | angle (−1…+1) |
| CH2 (elevator) | `sim/joystick/yoke_pitch_ratio` | angle_neg (inverted) |
| CH3 (throttle) | `sim/flightmodel/engine/ENGN_thro_use[0]` | range (0…1) |
| CH4 (rudder) | `sim/joystick/yoke_heading_ratio` | angle (−1…+1) |

---

## Instruksi Setup HITL (Prosedur)

Prosedur lengkap menjalankan sesi HITL ArduPlane fmuv3-hil + X-Plane 11/12.

### Langkah 1 — Konfigurasi Jaringan X-Plane

X-Plane harus mengirim data sensor DATA@ langsung ke alamat PPP Pixhawk dan menerima perintah DREF kembali. Konfigurasi sekali di X-Plane (tersimpan otomatis):

**Settings → Net Connections → Data:**

| Field | Nilai |
|---|---|
| Send data to IP | `10.0.0.2` |
| Send data port | `49001` |
| Receive commands port | `49000` |

Aktifkan DATA@ rows berikut (**Settings → Data Output**, centang "Send data over the net"):

| Row # | Nama | Digunakan untuk |
|---|---|---|
| 1 | Frame rate / sim time | Timing |
| 3 | Speeds | IAS → sensor airspeed |
| 4 | G-load | Akselerasi body-frame → IMU |
| 16 | Angular velocities | Roll/pitch/yaw rates → gyro |
| 17 | Pitch, roll, heading | Attitude → EKF |
| 20 | Lat, lon, altitude | Posisi GPS |
| 21 | Loc, vel, dist | Kecepatan NED → GPS velocity |

### Langkah 2 — Start PPP Tunnel

Hubungkan USB–UART adapter ke port TELEM2 Pixhawk. Cari nama device, lalu jalankan `pppd`:

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
| `10.0.0.1` | Laptop (sisi X-Plane) |
| `10.0.0.2` | Pixhawk |

Biarkan terminal ini tetap terbuka. Setelah Pixhawk boot dan firmware menginisialisasi PPP interface, `pppd` akan mencetak `local IP address 10.0.0.1`.

> **Penjelasan flag pppd:**
> - `asyncmap 0` — tidak ada escaping karakter kontrol (~20% penghematan bandwidth di 115200)
> - `novj` — nonaktifkan VJ TCP header compression (mengurangi latensi)
> - `nopcomp noaccomp` — nonaktifkan kompresi PPP header (framing lebih sederhana)
> - `lcp-echo-interval 0` — nonaktifkan LCP keepalive (firmware tidak membalas LCP Echo-Request; tanpa ini pppd putus dengan "Peer not responding" setelah ~12 detik)

### Langkah 3 — Hubungkan QGroundControl

Colokkan USB Pixhawk ke laptop. Buka QGroundControl — akan auto-connect via USB di 921600 baud (SERIAL0).

Harus terlihat:
- Vehicle connected (ArduPlane)
- Parameters loaded
- Flight mode (mis. MANUAL)

### Langkah 3b — Membuat Flight Plan di QGroundControl

Flight plan (misi) berisi urutan perintah yang akan dieksekusi otomatis oleh ArduPlane dalam mode AUTO. Berikut prosedur lengkap membuat flight plan di QGC:

**Membuka Plan View:**

1. Di toolbar atas QGC, klik ikon **Plan** (ikon peta dengan waypoint). Tampilan beralih ke peta top-down dengan vehicle position ditandai.
2. Pastikan posisi GPS vehicle sudah muncul di peta (EKF harus sudah konvergen). Jika peta masih kosong, tunggu hingga GPS fix muncul di status bar.

**Menambahkan Takeoff Waypoint:**

1. Klik **"+ Waypoint"** di toolbar kiri, lalu klik posisi runway di peta — ini akan menjadi WP1. Ubah type-nya:
   - Klik WP1 di daftar waypoint (panel kiri) → ubah command dari **Waypoint** menjadi **Takeoff**
   - Set **Min. Pitch**: `15°` (sudut climb minimum saat takeoff)
   - Set **Altitude**: ketinggian target setelah takeoff, misalnya `100 m` (AGL, relatif terhadap home)
2. Takeoff command wajib menjadi waypoint pertama (WP1). ArduPlane tidak akan memasuki mode AUTO jika WP1 bukan Takeoff atau jika misi kosong.

**Menambahkan Waypoint Navigasi:**

1. Klik **"+ Waypoint"** lagi → klik titik di peta untuk WP2, WP3, dst.
2. Untuk setiap waypoint, atur:
   - **Altitude**: ketinggian jelajah, misalnya `150 m`
   - **Acceptance Radius**: jarak (meter) dari waypoint agar dianggap "tercapai", default `25 m` cukup untuk sim
   - **Hold Time**: waktu (detik) untuk berputar di atas waypoint sebelum lanjut (set `0` untuk langsung lanjut)
3. Waypoint dieksekusi secara berurutan dari WP1 → WP2 → WP3 → dst.

**Menambahkan Perintah Akhir (Opsional):**

| Perintah | Fungsi |
|---|---|
| **LOITER_UNLIM** | Berputar tak terbatas di koordinat tersebut hingga mode diganti manual |
| **RETURN_TO_LAUNCH** | Terbang balik ke home point dan land otomatis |
| **LAND** | Pendaratan otomatis di koordinat yang ditentukan |

Untuk skenario pengujian awal, tambahkan **LOITER_UNLIM** sebagai waypoint terakhir agar vehicle tidak hilang jika misi selesai.

**Upload Misi ke Vehicle:**

1. Setelah semua waypoint ditambahkan, klik tombol **Upload** (ikon panah ke atas, di toolbar kanan panel waypoint).
2. QGC mengirim misi via MAVLink ke Pixhawk dan menyimpannya di flash. Konfirmasi muncul: **"Mission uploaded"**.
3. Kembali ke **Fly View** (ikon pesawat di toolbar atas) — waypoint akan terlihat tergambar di peta.

**Verifikasi Misi:**

| Item | Yang Harus Terlihat |
|---|---|
| Jumlah waypoint | Sesuai jumlah WP yang dibuat |
| WP1 | Bertipe Takeoff |
| Altitude setiap WP | Sesuai yang diset (bukan 0) |
| Garis penghubung | Jalur misi tergambar di peta dari WP1 ke WP terakhir |

> **Catatan:** Altitude di QGC default relatif terhadap **home point** (AGL). Home point di-set otomatis saat vehicle pertama kali mendapat GPS fix dan di-arm. Pastikan X-Plane sudah di-unpause dan GPS lock sudah tercapai sebelum arm agar home point benar.

### Langkah 4 — Unpause X-Plane

Tekan **P** (atau klik tombol pause) di X-Plane untuk memulai simulasi.

Setelah di-unpause:
- Pixhawk mulai menerima DATA@ rows via PPP dan melakukan injeksi sensor
- EKF menginisialisasi (GPS fix terlihat di QGC dalam beberapa detik)
- DREF packets kontrol permukaan mengalir dari Pixhawk ke X-Plane pada ~25 Hz

**Verifikasi di QGC:**
- Posisi GPS sesuai lokasi pesawat di X-Plane
- Attitude (roll/pitch/heading) sesuai cockpit X-Plane
- Airspeed berubah sesuai kecepatan di X-Plane

### Langkah 5 — Arm dan Terbang

Nyalakan RC transmitter, konfirmasi RC receiver menampilkan link. Arm via QGC atau urutan arming RC transmitter.

### Parameter Kunci (`defaults.parm`)

| Parameter | Nilai | Tujuan |
|---|---|---|
| `GPS1_TYPE` | 100 | SITL GPS backend (baca dari SIMState / X-Plane) |
| `ARSPD_TYPE` | 100 | SITL airspeed backend |
| `AHRS_EKF_TYPE` | 2 | EKF2 (stabil di STM32F427 dengan SITL backend) |
| `BRD_SAFETY_DEFLT` | 0 | Tidak ada safety switch di simulasi |
| `ARMING_SKIPCHK` | -1 | Skip semua pre-arm checks |
| `THR_FAILSAFE` | 0 | Nonaktifkan RC/throttle failsafe |
| `RC_OVERRIDE_TIME` | -1 | Tidak ada timeout pada RC_CHANNELS_OVERRIDE |
| `SERIAL0_PROTOCOL` | 2 | USB = MAVLink2 (QGC) |
| `SERIAL2_PROTOCOL` | 48 | TELEM2 = PPP |
| `SERIAL2_BAUD` | 115 | 115200 baud untuk PPP |
| `NET_ENABLE` | 1 | Aktifkan lwIP networking |
| `NET_OPTIONS` | 64 | Nonaktifkan batas PPP LCP echo |
| `SCHED_LOOP_RATE` | 50 | 50 Hz mencegah watchdog di STM32F427 |
| `SIM_OH_MASK` | 255 | Teruskan semua servo channel melalui SITL |
| `TKOFF_THR_MINACC` | 0 | Tidak ada cek akselerasi sebelum throttle-up |
| `TKOFF_THR_MINSPD` | 0 | Tidak ada cek kecepatan GPS sebelum throttle-up |
| `GROUND_STEER_ALT` | 5 | Ground steering aktif di bawah 5 m AGL |

### Troubleshooting

| Gejala | Kemungkinan Penyebab | Solusi |
|---|---|---|
| pppd "Peer not responding" | LCP echo tidak dinonaktifkan | Tambahkan `lcp-echo-interval 0` ke perintah pppd |
| pppd terhubung tapi X-Plane tidak dapat data | IP salah di konfigurasi jaringan X-Plane | Set send IP ke `10.0.0.2`, port `49001` |
| QGC tidak menampilkan GPS | EKF belum konvergen | Cek parameter `SIM_OPOS_*` sesuai lokasi X-Plane; pastikan X-Plane di-unpause |
| Kontrol tidak bergerak di X-Plane | Override DREFs timeout | Firmware mengirim ulang overrides otomatis setiap ~1 detik |
| Throttle tetap 0 saat arm | RANGE DREFs dinolkan saat disarm | Ini by design — arm dulu baru throttle |
| "Waiting for RC" / tidak bisa arm | Failsafe aktif | Verifikasi `THR_FAILSAFE 0` sudah ter-load; reset params jika perlu |
| Takeoff tidak mulai di AUTO | Throttle gate tidak terbuka | Verifikasi `TKOFF_THR_MINSPD 0`, `TKOFF_THR_MINACC 0` |
| Build gagal `redefinition of 'param_union'` | Spurious MAVLink headers di source tree | Jalankan `python3 fix_mavlink_headers.py` lalu `./waf distclean && ./waf configure --board fmuv3-hil && ./waf plane` |

---

## 1. Instalasi Git

**Kegiatan:**
Instalasi Git pada laptop yang digunakan sebagai build machine untuk firmware ArduPilot.

**Langkah:**
1. Download Git dari https://git-scm.com/download/win
2. Jalankan installer → pada bagian **"Adjusting your PATH environment"**, pilih **"Git from the command line and also from 3rd-party software"**
3. Pilihan lain biarkan default → klik Next hingga selesai
4. Verifikasi di Command Prompt:
   ```
   git --version
   ```

**Hasil:** Git berhasil terinstal dan dapat diakses dari terminal.

---

## 2. Pendaftaran Akun GitHub

**Kegiatan:**
Membuat akun GitHub untuk menyimpan repositori firmware drone-kamikaze dan logbook penelitian.

**Langkah:**
1. Buka https://github.com
2. Klik **"Sign up"** → masukkan email, password, dan username
3. Verifikasi email melalui link konfirmasi
4. Generate SSH key dan daftarkan ke GitHub:
   ```
   ssh-keygen -t ed25519 -C "email@gmail.com"
   cat ~/.ssh/id_ed25519.pub
   ```
   Salin output → GitHub → Settings → SSH Keys → New SSH Key → Paste → Save
5. Verifikasi koneksi SSH:
   ```
   ssh -T git@github.com
   ```

**Hasil:** Akun GitHub berhasil dibuat dan SSH key terdaftar.

---

## 3. Clone Repositori ArduPilot

**Kegiatan:**
Clone repositori ArduPilot resmi dari GitHub sebagai basis pengembangan firmware drone-kamikaze.

**Perintah:**
```
git clone https://github.com/ArduPilot/ardupilot.git
cd ardupilot
git submodule update --init --recursive
```

**Catatan:** Proses `submodule update` memakan waktu ±10–15 menit tergantung koneksi internet karena submodul MAVLink, ChibiOS, dan lainnya berukuran besar.

**Hasil:** Repositori ArduPilot berhasil di-clone lengkap dengan seluruh submodul.

---

## 4. Konfigurasi Environment Build & Kompilasi Firmware fmuv3 Standar

**Kegiatan:**
Konfigurasi build environment menggunakan WAF build system ArduPilot dan kompilasi firmware ArduPlane standar untuk board fmuv3 (Pixhawk 2.4.8).

**Langkah:**
1. Install dependensi Python yang diperlukan:
   ```
   pip install empy==3.3.4 pexpect pymavlink future
   ```
2. Konfigurasi board fmuv3:
   ```
   ./waf configure --board fmuv3
   ```
3. Kompilasi firmware ArduPlane:
   ```
   ./waf plane
   ```

**Output:** File firmware `arduplane.apj` tersimpan di folder `build/fmuv3/bin/`.

**Hasil:** Firmware ArduPlane berhasil dikompilasi untuk board fmuv3 tanpa error.

---

## 5. Upload Firmware ke Pixhawk 2.4.8

**Kegiatan:**
Upload firmware ArduPlane hasil kompilasi ke Pixhawk 2.4.8 menggunakan QGroundControl.

**Langkah:**
1. Hubungkan Pixhawk ke laptop via kabel USB
2. Buka QGroundControl → **Vehicle Setup** → **Firmware**
3. Pilih **Custom firmware** → arahkan ke file `arduplane.apj` hasil kompilasi
4. Klik OK → QGroundControl meng-upload firmware secara otomatis
5. Pixhawk reboot otomatis setelah upload selesai

**Hasil:** Firmware berhasil di-upload ke Pixhawk 2.4.8.

---

## 6. Verifikasi Boot via QGroundControl

**Kegiatan:**
Verifikasi bahwa Pixhawk berhasil boot dengan firmware ArduPlane yang baru diupload.

**Langkah:**
1. Setelah upload, Pixhawk reboot otomatis dan terhubung kembali ke QGroundControl
2. Cek vehicle summary: firmware version, board type, dan status sensor
3. Verifikasi tidak ada critical error di message log QGC
4. Cek deteksi sensor: IMU, barometer, dan compass

**Hasil:** Pixhawk berhasil boot dengan ArduPlane. QGroundControl menampilkan status normal — sensor IMU dan barometer terdeteksi tanpa error.

---

## 7. Fork Repositori ArduPilot → drone-kamikaze

**Kegiatan:**
Fork repositori ArduPilot ke akun GitHub pribadi sebagai basis pengembangan firmware custom drone-kamikaze.

**Langkah:**
1. Buka https://github.com/ArduPilot/ardupilot
2. Klik **"Fork"** → pilih akun `musaelhanafi` sebagai owner → klik **Create fork**
3. Repositori fork tersedia di https://github.com/musaelhanafi/drone-kamikaze
4. Update remote pada repositori lokal:
   ```
   git remote rename origin upstream
   git remote add origin git@github.com:musaelhanafi/drone-kamikaze.git
   git push -u origin main
   ```

**Hasil:** Fork berhasil. Repositori drone-kamikaze tersedia di https://github.com/musaelhanafi/drone-kamikaze.

---

## 8. Modifikasi Konfigurasi Board fmuv3 untuk HITL Mode

**Kegiatan:**
Membuat konfigurasi board baru `fmuv3-hil` di firmware drone-kamikaze untuk mendukung mode HITL (Hardware-in-the-Loop) dengan X-Plane sebagai physics engine. Koneksi menggunakan PPP tunnel via TELEM2.

**File yang dibuat:**

| File | Keterangan |
|---|---|
| `libraries/AP_HAL_ChibiOS/hwdef/fmuv3-hil/hwdef.dat` | Definisi hardware board |
| `libraries/AP_HAL_ChibiOS/hwdef/fmuv3-hil/defaults.parm` | Parameter default HITL |

**Parameter utama `defaults.parm`:**

| Parameter | Nilai | Keterangan |
|---|---|---|
| `AHRS_EKF_TYPE` | 2 | EKF2 (sesuai keterbatasan STM32F427) |
| `EK2_ENABLE` | 1 | EKF2 aktif |
| `EK3_ENABLE` | 0 | EKF3 nonaktif |
| `GPS1_TYPE` | 100 | SITL GPS (data dari X-Plane) |
| `ARSPD_TYPE` | 100 | SITL airspeed (data dari X-Plane) |
| `NET_ENABLE` | 1 | PPP networking aktif |
| `SERIAL2_PROTOCOL` | 48 | PPP protocol di TELEM2 |
| `SERIAL2_BAUD` | 115 | 115200 baud |
| `NET_OPTIONS` | 64 | PPP options |
| `SIM_OPOS_LAT` | −6.897434 | Home position — Bandara WICC Bandung |
| `SIM_OPOS_LNG` | 107.566887 | |
| `SIM_OPOS_ALT` | 744.0 | Altitude AMSL (m) |

**Prinsip kerja HITL:**
- X-Plane menjalankan fisika penerbangan dan mengirim data sensor (IMU, GPS, airspeed) ke ArduPilot via PPP tunnel
- ArduPilot menjalankan algoritma kendali (EKF, PID) menggunakan data sensor dari X-Plane
- Output servo ArduPilot dikirim kembali ke X-Plane sebagai DREF packets untuk menggerakkan permukaan kontrol FX-61

**Hasil:** Konfigurasi board fmuv3-hil berhasil dibuat.

---

## 9. Kompilasi Firmware fmuv3-hil & Upload ke Pixhawk

**Kegiatan:**
Kompilasi firmware ArduPlane dengan konfigurasi board fmuv3-hil dan upload ke Pixhawk.

**Kompilasi:**
```
./waf configure --board fmuv3-hil
./waf plane
```

**Upload:**
Sama seperti langkah 5, menggunakan QGroundControl dengan file `arduplane.apj` hasil kompilasi fmuv3-hil.

**Hasil:** Firmware fmuv3-hil berhasil dikompilasi tanpa error dan di-upload ke Pixhawk.

---

## 10. Verifikasi Data X-Plane Terkirim ke Pixhawk

**Kegiatan:**
Verifikasi bahwa data sensor dari X-Plane berhasil diterima oleh Pixhawk melalui koneksi PPP over TELEM2.

**Langkah:**
1. Jalankan X-Plane dengan plugin HITL aktif
2. Hubungkan Pixhawk ke laptop via TELEM2 (USB-UART bridge)
3. Setup koneksi PPP antara laptop dan Pixhawk
4. Cek log ArduPlane di QGroundControl — verifikasi:
   - GPS lock diperoleh dari data X-Plane
   - Data IMU bergerak sesuai manuver di X-Plane
   - Airspeed berubah sesuai kecepatan di X-Plane

**Hasil:** Data X-Plane berhasil diterima Pixhawk. GPS lock tercapai, data IMU responsif terhadap pergerakan di X-Plane.

---

## 11. Menerbangkan FX-61 di X-Plane

**Kegiatan:**
Uji terbang FX-61 Phantom di X-Plane dalam mode HITL dengan Pixhawk sebagai flight controller aktif.

**Skenario:**
1. Spawn FX-61 di threshold runway 11 WICC Bandung
2. Arm Pixhawk via QGroundControl
3. Set mode MANUAL
4. Takeoff dan uji manuver dasar: roll, pitch, climb, descent
5. Observasi sinkronisasi respons servo fisik FX-61 dengan tampilan X-Plane

**Hasil:** FX-61 berhasil diterbangkan dalam mode HITL. Respons kontrol normal — input RC menggerakkan permukaan kontrol di X-Plane secara real-time melalui Pixhawk.

---

## 12. Autotune

**Kegiatan:**
Menjalankan fitur Autotune ArduPlane pada FX-61 di X-Plane untuk mendapatkan gain PID roll dan pitch yang optimal secara otomatis.

**Langkah:**
1. Set parameter awal:
   - `AUTOTUNE_LEVEL = 6` (agresivitas tuning sedang)
2. Terbangkan FX-61 dalam mode FBWA (Fly By Wire A)
3. Aktifkan mode AUTOTUNE via QGroundControl
4. ArduPilot melakukan manuver otomatis untuk mengidentifikasi gain PID optimal
5. Tunggu konvergensi — QGC menampilkan alert **"Autotune complete"**
6. Save parameter hasil autotune ke Pixhawk

**Hasil:** Autotune berhasil dijalankan. Gain PID roll dan pitch berhasil diidentifikasi dan disimpan.

---

## 13. Autotakeoff dan Navigasi Waypoint (Mode AUTO)

**Kegiatan:**
Menguji kemampuan FX-61 untuk melakukan takeoff otomatis dan mengikuti flight plan waypoint yang sudah diupload ke Pixhawk, menggunakan mode AUTO ArduPlane dalam simulasi HITL.

**Prasyarat:**
- Misi sudah dibuat dan diupload ke Pixhawk via QGC (lihat Langkah 3b)
- HITL aktif: X-Plane berjalan, PPP tunnel aktif, GPS lock tercapai
- Parameter TKOFF sudah benar (`TKOFF_THR_MINSPD 0`, `TKOFF_THR_MINACC 0`)

**Parameter tambahan yang perlu diverifikasi:**

| Parameter | Nilai | Tujuan |
|---|---|---|
| `TKOFF_THR_MINACC` | `0` | Tidak ada cek akselerasi minimum sebelum throttle-up |
| `TKOFF_THR_MINSPD` | `0` | Tidak ada cek kecepatan GPS sebelum throttle-up |
| `TKOFF_ALT` | `100` | Altitude target takeoff (m AGL) — sesuaikan dengan WP1 di misi |
| `RTL_ALTITUDE` | `150` | Altitude Return-to-Launch jika dipicu (m AGL) |
| `CRUISE_SPEED` | `20` | Kecepatan jelajah menuju waypoint (m/s) |
| `WP_RADIUS` | `25` | Jarak acceptance radius waypoint (m) |
| `WP_LOITER_RAD` | `80` | Radius loiter saat mode LOITER (m) |
| `ARMING_REQUIRE` | `1` | Vehicle harus di-arm sebelum AUTO bisa berjalan |

**Langkah eksekusi:**

1. **Verifikasi misi di Fly View** — Pastikan jalur waypoint tergambar di peta QGC. Cek jumlah waypoint dan WP1 bertipe Takeoff.

2. **Set mode ke AUTO** — Di QGC Fly View, klik dropdown flight mode → pilih **AUTO**. Pixhawk beralih ke AUTO dan langsung siap mengeksekusi misi saat di-arm.

3. **Arm vehicle** — Klik tombol **Arm** di QGC (atau gunakan urutan arm RC transmitter). Setelah arm:
   - Throttle naik otomatis ke nilai takeoff
   - Permukaan kontrol aktif
   - X-Plane: FX-61 mulai berakselerasi di runway

4. **Takeoff otomatis** — ArduPlane mengeksekusi WP1 (Takeoff command):
   - Throttle full, ground steering aktif hingga airspeed tercapai
   - Saat airspeed > stall speed, ArduPlane rotate dan climb menuju altitude WP1
   - Selama climb: aileron/elevator dikontrol penuh oleh autopilot
   - Verifikasi di QGC: altitude bar naik, mode tetap AUTO, WP aktif menunjuk WP1

5. **Transisi ke navigasi waypoint** — Setelah altitude WP1 tercapai, ArduPlane otomatis beralih ke WP2:
   - Autopilot mengatur heading menuju koordinat WP2
   - Altitude dijaga sesuai nilai yang diset di setiap waypoint
   - Di QGC: indikator waypoint aktif bergeser ke WP2, garis jalur terbang terlihat di peta

6. **Monitoring selama misi:**

| Yang Dimonitor | Di Mana | Nilai Normal |
|---|---|---|
| Flight mode | QGC status bar | AUTO (tidak berubah) |
| Waypoint aktif | QGC Fly View peta | Nomor WP bertambah seiring misi berjalan |
| Altitude | QGC altitude indicator | Sesuai altitude WP yang sedang dituju |
| Airspeed | QGC speed indicator | Sekitar nilai `CRUISE_SPEED` |
| Cross-track error | QGC attitude widget | Kecil — pesawat tidak menyimpang jauh dari jalur |

7. **Akhir misi** — Jika waypoint terakhir adalah LOITER_UNLIM, FX-61 akan berputar di titik tersebut tanpa batas. Untuk mengakhiri:
   - Ganti mode ke **MANUAL** atau **FBWA** dari QGC untuk ambil alih kendali
   - Atau ganti ke **RTL** untuk kembali ke home dan land otomatis

**Hasil:** FX-61 berhasil melakukan autotakeoff dari runway WICC Bandung dan mengikuti seluruh waypoint yang diprogram, dengan Pixhawk sebagai flight controller aktif melalui HITL. Mode AUTO berjalan penuh tanpa intervensi manual.

---

## Ringkasan Kegiatan

| No | Kegiatan | Status |
|---|---|---|
| 1 | Instalasi Git | ✅ Selesai |
| 2 | Pendaftaran akun GitHub | ✅ Selesai |
| 3 | Clone repositori ArduPilot dari GitHub | ✅ Selesai |
| 4 | Konfigurasi environment build & kompilasi firmware fmuv3 standar | ✅ Selesai |
| 5 | Upload firmware ke Pixhawk 2.4.8 | ✅ Selesai |
| 6 | Verifikasi boot via QGroundControl | ✅ Selesai |
| 7 | Fork repositori ArduPilot → drone-kamikaze | ✅ Selesai |
| 8 | Modifikasi konfigurasi board fmuv3-hil untuk HITL mode | ✅ Selesai |
| 9 | Kompilasi firmware fmuv3-hil & upload ke Pixhawk | ✅ Selesai |
| 10 | Verifikasi data X-Plane terkirim ke Pixhawk | ✅ Selesai |
| 11 | Menerbangkan FX-61 di X-Plane | ✅ Selesai |
| 12 | Autotune | ✅ Selesai |
| 13 | Autotakeoff dan navigasi waypoint (mode AUTO) | ✅ Selesai |

---

*Logbook dibuat: 17 April 2026 | Penelitian OPSI 2026 — SMA Swasta Alfa Centauri*
