# Worksheet Pengamatan Histogram Warna

| | |
|---|---|
| **Nama** | |
| **Tanggal** | 27 April 2026 |
| **Tools** | `app_histogram.py` — pilih ROI dengan klik+drag, kunci dengan `l` |

---

## Petunjuk Pengisian

1. Jalankan `app_histogram.py`
2. Arahkan kamera ke objek berwarna target
3. Klik dan drag untuk memilih ROI pada objek
4. Tekan `l` untuk mengunci ROI
5. Catat nilai **mean** tiap channel dari window *Histogram HSV* dan *Histogram BGR*
6. Ulangi untuk setiap kondisi cahaya: **normal → terang → bayangan**
7. Isi kolom **Keterangan** dengan observasi kualitatif (misal: "H stabil", "S turun signifikan")

---

## 1. Warna Merah

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | 15|233 |82 | 7| 12|83 | |
| Terang | 12| 166| 242| 63| 106| 216| |
| Bayangan |10 |235 | 91|22 |15 | 91| |

**Kesimpulan:** Nilai H tidak berubah banyak terhadap perubahan intensitas cahaya

---

## 2. Warna Oranye

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | | | | | | | |
| Terang | | | | | | | |
| Bayangan | | | | | | | |

**Catatan:** Rentang H oranye di OpenCV: 10–25. Bandingkan stabilitas H antara oranye dan merah.

---

## 3. Warna Kuning

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | | | | | | | |
| Terang | | | | | | | |
| Bayangan | | | | | | | |

**Catatan:** Rentang H kuning di OpenCV: 25–35. Amati apakah S turun saat terkena cahaya terang langsung.

---

## 4. Warna Hijau

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | | | | | | | |
| Terang | | | | | | | |
| Bayangan | | | | | | | |

**Catatan:** Rentang H hijau di OpenCV: 35–85. Hijau memiliki rentang H terluas — amati apakah H tetap stabil.

---

## 5. Warna Biru

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | | | | | | | |
| Terang | | | | | | | |
| Bayangan | | | | | | | |

**Catatan:** Rentang H biru di OpenCV: 100–130. Bandingkan perubahan channel B (BGR) antara kondisi terang dan bayangan.

---

## 6. Warna Ungu / Magenta

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | | | | | | | |
| Terang | | | | | | | |
| Bayangan | | | | | | | |

**Catatan:** Rentang H ungu/magenta di OpenCV: 130–170. Amati apakah warna ini lebih sensitif terhadap perubahan pencahayaan dibanding warna lain.

---

## Tabel Ringkasan — Stabilitas Hue Antar Kondisi

Isi setelah semua pengamatan selesai. Hitung selisih Mean H antara kondisi terang dan bayangan.

| Warna | Mean H Normal | Mean H Terang | Mean H Bayangan | ΔH (Terang−Normal) | ΔH (Bayangan−Normal) |
|---|---|---|---|---|---|
| Merah | | | | | |
| Oranye | | | | | |
| Kuning | | | | | |
| Hijau | | | | | |
| Biru | | | | | |
| Ungu | | | | | |

---

## Tabel Ringkasan — Perubahan Saturasi (S) dan Value (V)

| Warna | S Normal | S Terang | S Bayangan | V Normal | V Terang | V Bayangan |
|---|---|---|---|---|---|---|
| Merah | | | | | | |
| Oranye | | | | | | |
| Kuning | | | | | | |
| Hijau | | | | | | |
| Biru | | | | | | |
| Ungu | | | | | | |

---

## Pertanyaan Analisis

**1.** Channel mana (H, S, atau V) yang paling stabil terhadap perubahan kondisi cahaya? Jelaskan mengapa.

> _Jawaban:_

---

**2.** Saat kondisi **terang**, apa yang terjadi pada nilai S dan V? Apakah polanya konsisten untuk semua warna?

> _Jawaban:_

---

**3.** Saat kondisi **bayangan**, apa yang terjadi pada nilai V? Apakah H tetap bisa digunakan sebagai referensi deteksi?

> _Jawaban:_

---

**4.** Berdasarkan pengamatan ini, warna mana yang paling mudah dideteksi secara konsisten di ketiga kondisi cahaya? Mengapa?

> _Jawaban:_

---

**5.** Jika ingin membuat sistem deteksi warna yang robust terhadap perubahan pencahayaan, nilai batas (lower/upper) channel mana yang sebaiknya diberi toleransi lebih lebar?

> _Jawaban:_

---

*Worksheet — Pengamatan Histogram Warna | 27 April 2026 | Penelitian OPSI 2026 — SMA Swasta Alfa Centauri*
