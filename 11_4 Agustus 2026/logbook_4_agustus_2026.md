# Logbook Kegiatan — 4 Agustus 2026

| | |
|---|---|
| **Penelitian** | Sistem Kendali Drone Kamikaze Berbasis Deteksi Objek Warna dalam Simulasi HITL |
| **Tim** | Musa El Hanafi & Muhammad Ihsan Fahriansyah |
| **Lokasi** | Lab Komputer SMA Swasta Alfa Centauri, Kota Bandung |
| **Hari/Tanggal** | Selasa, 4 Agustus 2026 |

---

Kegiatan hari ini adalah **uji ulang fase terminal** dengan protokol yang sama seperti sesi 8 Mei 2026, tetapi pada dua kondisi yang berbeda secara mendasar:

1. **Seeker berjalan on-board di Raspberry Pi**, bukan lagi di laptop — realisasi rencana tindak lanjut prioritas sedang dari logbook 8 Mei
2. **Histogram warna hasil fine-tuning berbasis ground truth** (`pink_histogram.txt`, 2 Agustus 2026) menggantikan histogram hand-picked

Enam run diuji: kiri dan kanan, masing-masing dari ketinggian cruise ~50 m, ~80 m, dan ~100 m di atas target. Seluruhnya dianalisis dengan `terminal_analyse.py`, script yang sama seperti 8 Mei, sehingga angkanya dapat dibandingkan langsung.

**Hasil utama:** akurasi lock terburuk naik dari **90,7% → 96,2%**, dengan empat dari enam run mempertahankan lock **100%** sepanjang fase terminal. Peningkatan ini diperoleh justru saat throughput turun dari 24,7 FPS ke 18,4 FPS akibat perpindahan ke perangkat on-board — menunjukkan kualitas histogram lebih menentukan daripada frame rate.

---

## 1. Perubahan Konfigurasi Sejak 8 Mei

| Aspek | 8 Mei 2026 | 4 Agustus 2026 |
|---|---|---|
| Lokasi eksekusi seeker | Laptop (bersama X-Plane) | **Raspberry Pi on-board** |
| Input kamera | Webcam mengarah ke layar X-Plane | Sama |
| Histogram warna | Hand-picked satu ROI | **`pink_histogram.txt` — refit ground truth** |
| `gauss_sigma` | 1,0 (default) | **2,0** |
| Ketinggian uji | 60 m / 80 m / 100 m | **50 m** / 80 m / 100 m |
| Rekaman video | Hanya beranotasi | Beranotasi **+ raw** (tanpa overlay) |
| Link ke Pixhawk | PPP dari laptop | PPP dari Raspberry Pi (`ppp0`, 10.0.0.1 ↔ 10.0.0.2) |

Perpindahan ke Raspberry Pi mengubah topologi jaringan: Pi memegang link PPP ke Pixhawk sekaligus meneruskan data X-Plane ke laptop lewat DNAT, sehingga tidak ada host yang perlu mengetahui subnet seberang.

---

## 2. Histogram Warna dari Fine-tuning 2 Agustus

Histogram yang dipakai pada seluruh run adalah **`pink_histogram.txt`**, hasil fine-tuning berbasis ground truth yang didokumentasikan di [logbook 2 Agustus 2026](../10_2%20Agustus%202026/logbook_2_agustus_2026.md).

| Properti | Seed (8 Mei) | Refit (`pink_histogram.txt`) |
|---|---|---|
| Sumber sampel | 1 ROI di 1 frame | 85 kotak GT dari klip training |
| Piksel disampling | 307 | 42 846 |
| Mean / std hue | 166,4 / 9,71 | **164,3 / 1,68** |
| Bins aktif | 12 raw / 8 efektif | 29 raw / **7 efektif** |
| Recall di holdout | 0,685 | **0,924** |
| Precision di holdout | 0,677 | **0,924** |
| Combined FP+FN | 28 | **5** |

Sesi 2 Agustus merekomendasikan refit ini untuk deployment dengan `--gauss-sigma 2`. Uji hari ini adalah validasi rekomendasi tersebut pada penerbangan HITL sesungguhnya, bukan lagi pada klip rekaman.

---

## 3. Sumber Data dan Pemotongan ke Fase Terminal

Setiap run menghasilkan empat artefak: video beranotasi, video raw, CSV telemetri, dan log profil pipeline.

| Run | Video (s) | Baris CSV (setelah cut) |
|---|---:|---:|
| Kiri 50 m | 27,2 | 563 |
| Kanan 50 m | 24,6 | 463 |
| Kiri 80 m | 21,9 | 436 |
| Kanan 80 m | 26,2 | 475 |
| Kiri 100 m | 22,2 | 436 |
| Kanan 100 m | 26,6 | 469 |

**Kasus khusus `kanan_100m`.** Rekaman ini semula memuat satu sirkuit penuh sepanjang 101,7 detik: ekor run sebelumnya, lalu misi mengulang dari WP2, menjauh ke 1,27 km melewati WP3 dan WP4, baru kemudian berbalik dan masuk fase terminal. Data dipotong ke fase terminal saja, dimulai tepat saat mode beralih `AUTO:4 → TRACKING:4`.

Titik potong ditentukan lewat pembacaan HUD frame demi frame dan diverifikasi silang dengan CSV:

- frame 1648 masih `AUTO:4`, frame 1650 sudah `TRACKING:4`, keduanya pada `dist 0.743 km`
- baris pertama CSV fase terminal: `t = 950,796 s`, `dist_m = 743,5`

`terminal_analyse.py` kemudian melaporkan jarak lock **743,5 m** untuk run ini — dua metode independen menunjuk momen yang sama.

**Catatan tentang berkas `.log`.** Log profil pipeline dari Raspberry Pi berstempel 27 Juli 2026 karena RTC Pi tidak tersinkronisasi. Stempel ini diabaikan. Sebagai konsekuensinya log tidak dapat dipotong per fase — isinya jam dinding RTC sementara CSV memakai `timestamp_s` waktu misi, dan tidak ada jangkar di antara keduanya. Seluruh analisis di bawah bersumber dari CSV, yang tidak terpengaruh.

---

## 4. Analisis Fase Terminal dengan terminal_analyse.py

**Perintah:**

```bash
python3 script/terminal_analyse.py tracking_kanan_100m.csv
```

**Output ringkasan (`tracking_kanan_100m.csv`):**

```
───────────────────────────────────────────────────────
  File duration   : 29.6 s  (469 rows)
  Mean FPS        : 15.8  (wall-clock, from timestamps)
  Target locked   : 451 rows  (96.2%)
  Track lost      : 18 rows  (3.8%)

  ── First track acquisition ──
  Time            : t+0.0 s
  Alt above target: 81.2 m
  Speed           : 87.1 km/h
  Distance        : 743.5 m

  ── Nearest point (hit) ──
  Time            : t+28.3 s
  Distance        : 4.8 m
  Speed at hit    : 110.3 km/h  (30.6 m/s)
  Alt at hit      : 5.5 m

  ── Descent ──
  Mean descent    : 3.12 m/s
  Peak descent    : 29.74 m/s
  Total alt drop  : 75.7 m

  ── Pitch (locked rows only) ──
  Mean pitch      : -9.5 deg
  Mean nav_pitch  : -10.3 deg
───────────────────────────────────────────────────────
```

**Grafik analisis fase terminal — Kanan 100 m:**

![Terminal Analysis Kanan 100m](terminal_analysis_kanan_100m.png)

**Keterangan grafik (4 panel):**
1. Altitude / Groundspeed / Throttle vs waktu
2. Camera error (errorx, errory) vs waktu — area abu = lock hilang
3. Attitude pesawat (pitch, roll, nav_pitch) vs waktu
4. Control surfaces (elevator, aileron) vs waktu

**Penanda:** garis cyan (`:`) — titik jarak terdekat ke target.

Pada run ini seluruh kehilangan lock (18 baris, 3,8%) terkonsentrasi di **8 detik pertama** saat error kamera masih besar (|errorx| ≈ 0,75). Setelah error mengecil di bawah 0,2 pada detik ke-13, tracking stabil tanpa putus sampai impact.

---

## 5. Perbandingan Hasil Pengujian: Enam Run

| Metrik | Kiri 50m | Kanan 50m | Kiri 80m | Kanan 80m | Kiri 100m | Kanan 100m | **Rata-rata** |
|---|---|---|---|---|---|---|---|
| Durasi fase terminal | 27,1 s (563) | 24,0 s (463) | 21,2 s (436) | 29,0 s (475) | 24,2 s (436) | 29,6 s (469) | **25,9 s (474)** |
| Akurasi lock | **100,0%** | **100,0%** | **100,0%** | 96,2% | **100,0%** | 96,2% | **98,7%** |
| Frame rate | 20,7 FPS | 19,2 FPS | 20,5 FPS | 16,3 FPS | 18,0 FPS | 15,8 FPS | **18,4 FPS** |
| Alt saat lock | 51,0 m | 50,6 m | 68,5 m | 74,2 m | 82,3 m | 81,2 m | **68,0 m** |
| Jarak saat lock | 694,6 m | 581,9 m | 578,5 m | 742,7 m | 617,9 m | 743,5 m | **659,9 m** |
| Waktu lock → hit | 27,1 s | 22,6 s | 21,2 s | 29,0 s | 22,1 s | 28,3 s | **25,1 s** |
| Jarak terdekat | 11,1 m | 6,2 m | 13,6 m | 10,3 m | 14,9 m | **4,8 m** | **10,2 m** |
| Kecepatan saat hit | 96,0 km/h | 99,4 km/h | 107,7 km/h | 107,2 km/h | 109,6 km/h | 110,3 km/h | **105,0 km/h** |
| Ketinggian saat hit | 4,5 m | 6,1 m | 6,9 m | 0,1 m | 3,2 m | 5,5 m | **4,4 m** |
| Mean descent | 1,56 m/s | 1,87 m/s | 2,67 m/s | 2,80 m/s | 3,36 m/s | 3,12 m/s | **2,56 m/s** |
| Peak descent | 18,44 m/s | 20,88 m/s | 23,95 m/s | 30,56 m/s | 33,41 m/s | 29,74 m/s | **26,16 m/s** |
| Total alt drop | 46,5 m | 44,5 m | 61,7 m | 74,1 m | 79,0 m | 75,7 m | **63,6 m** |
| Mean pitch (locked) | −6,2° | −6,4° | −8,5° | −8,8° | −10,0° | −9,5° | **−8,2°** |

**Catatan:**

- **Akurasi lock naik seiring ketinggian yang lebih rendah.** Keempat run dengan FPS ≥ 18 mempertahankan lock 100%. Dua run yang kehilangan lock (96,2%) justru yang FPS-nya terendah — 16,3 dan 15,8. Korelasi ini konsisten dengan kehilangan lock akibat pipeline melambat, bukan akibat geometri pendekatan.
- **Kecepatan saat hit meningkat monoton terhadap ketinggian lock:** ~96–99 km/h (50 m) → ~107 km/h (80 m) → ~110 km/h (100 m). Konsisten dengan dive lebih curam dari ketinggian lebih tinggi.
- **Mean pitch mengikuti pola yang sama:** −6,2°/−6,4° (50 m) → −8,5°/−8,8° (80 m) → −10,0°/−9,5° (100 m).
- **Total alt drop mendekati ketinggian lock awal** di semua run (46,5 m dari 51,0 m; 74,1 m dari 74,2 m; 75,7 m dari 81,2 m) — drone berhasil menukik ke hampir permukaan.
- **`kanan_80m` menabrak pada ketinggian 0,1 m**, praktis di permukaan tanah, sementara run lain 3,2–6,9 m. Bila target memiliki ketinggian fisik, angka ini berarti pesawat lewat di bawahnya.
- **Dua run melampaui kriteria hit 10 m** yang dipakai pada sesi 8 Mei: kiri 80 m (13,6 m) dan kiri 100 m (14,9 m). Keduanya perlu konfirmasi visual dari rekaman sebelum dinyatakan sebagai hit yang setara.

---

## 6. Perbandingan dengan Sesi 8 Mei 2026

| Metrik | 8 Mei (laptop, seed) | 4 Agustus (Pi, refit) | Perubahan |
|---|---|---|---|
| Akurasi lock — rata-rata | 97,3% | **98,7%** | naik tipis |
| Akurasi lock — **terburuk** | 90,7% | **96,2%** | **naik 5,5 poin** |
| Run dengan lock 100% | 3 dari 6 | **4 dari 6** | naik |
| Frame rate rata-rata | 24,7 FPS | 18,4 FPS | **turun 6,3 FPS** |
| Jarak lock rata-rata | 942,2 m | 659,9 m | turun |
| Jarak terdekat rata-rata | 5,8 m | 10,2 m | naik (lebih jauh) |
| Kecepatan hit rata-rata | 96,5 km/h | 105,0 km/h | naik |

**Interpretasi:**

Nilai yang paling bermakna bukan rata-rata akurasi (97,3% → 98,7%, selisih kecil) melainkan **akurasi terburuk**. Pada 8 Mei run terlemah kehilangan lock 9,3%; sekarang yang terlemah hanya 3,8%. Sebaran menyempit — inilah yang diharapkan dari histogram yang di-refit dari 85 kotak ground truth alih-alih satu ROI tunggal, dan sejalan dengan turunnya kasus *combined FP+FN* dari 28 ke 5 pada evaluasi 2 Agustus.

Peningkatan ini diperoleh **sambil kehilangan 6,3 FPS** karena beban pindah ke Raspberry Pi. Artinya kualitas model warna lebih menentukan hasil daripada throughput, setidaknya pada rentang 15–25 FPS.

Dua metrik yang memburuk perlu dicatat jujur. **Jarak lock rata-rata turun** dari 942 m ke 660 m — target dikunci lebih dekat, kemungkinan karena pita hue refit yang jauh lebih sempit (σ 9,71 → 1,68) menuntut warna target lebih dominan di frame sebelum lock terjadi. **Jarak terdekat rata-rata memburuk** dari 5,8 m ke 10,2 m; sebagian disebabkan dua run kiri yang meleset 13–15 m, sementara run terbaik hari ini (kanan 100 m, 4,8 m) justru lebih akurat dari run terbaik 8 Mei (3,6 m tercatat pada kiri 80 m).

---

## 7. Kendala dan Solusi

| No | Kendala | Solusi |
|---|---|---|
| 1 | RTC Raspberry Pi tidak tersinkronisasi — log berstempel 27 Juli | Stempel diabaikan; seluruh analisis memakai `timestamp_s` dari CSV |
| 2 | `kanan_100m` merekam satu sirkuit penuh, bukan fase terminal saja | Dipotong pada transisi `AUTO → TRACKING`, diverifikasi silang HUD ↔ CSV |
| 3 | Metadata fps video (21,97) tidak sama dengan capture sebenarnya (15–22) | Durasi dihitung dari `timestamp_s` CSV, bukan dari metadata video |
| 4 | Log profil tidak punya basis waktu bersama dengan CSV | Tidak dipotong; ditandai sebagai artefak diagnostik, bukan data analisis |
| 5 | Throughput turun setelah pindah ke Raspberry Pi | Diterima — akurasi lock tetap membaik; optimasi ditunda ke iterasi berikutnya |

---

## 8. Rencana Tindak Lanjut

| Prioritas | Kegiatan |
|---|---|
| Tinggi | Konfirmasi visual dua run kiri (80 m dan 100 m) yang jarak terdekatnya 13,6 m dan 14,9 m |
| Tinggi | Periksa rekaman `kanan_80m` — hit pada ketinggian 0,1 m, kemungkinan lewat di bawah target |
| Tinggi | Sinkronisasi RTC Raspberry Pi (NTP atau modul RTC) agar log punya stempel waktu yang berguna |
| Sedang | Profil ulang pipeline di Raspberry Pi untuk mengembalikan throughput ke ≥ 20 FPS |
| Sedang | Uji `--combined-penalty 3.0` pada fine-tuning berikutnya untuk menekan sisa kasus misdirection |
| Rendah | Selaraskan metadata fps video dengan capture sebenarnya saat menulis rekaman |

---

## Ringkasan Kegiatan

| No | Kegiatan | Hasil |
|---|---|---|
| 1 | Deploy seeker on-board ke Raspberry Pi + link PPP ke Pixhawk | ✅ Selesai |
| 2 | Deploy histogram hasil fine-tuning `pink_histogram.txt` dengan `gauss_sigma=2` | ✅ Selesai |
| 3 | Uji terminal 6 run: kiri & kanan × 50 m, 80 m, 100 m | ✅ 6 run terekam |
| 4 | Rekaman ganda per run — video beranotasi + raw tanpa overlay | ✅ 12 video |
| 5 | Pemotongan `kanan_100m` ke fase terminal (verifikasi silang HUD ↔ CSV) | ✅ Selesai |
| 6 | Analisis `terminal_analyse.py` untuk keenam run | ✅ 6 plot + ringkasan |
| 7 | Perbandingan langsung terhadap sesi 8 Mei 2026 | ✅ Akurasi terburuk 90,7% → 96,2% |
| 8 | Validasi rekomendasi deployment dari sesi 2 Agustus pada penerbangan HITL | ✅ **Terkonfirmasi** |

*Logbook ditulis oleh: Muhammad Ihsan Fahriansyah & Musa El Hanafi*
