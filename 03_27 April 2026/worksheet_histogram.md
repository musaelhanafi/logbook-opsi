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
| Normal | 18 | 238 | 160 | 6 | 118 | 170 | H stabil, S tinggi |
| Terang | 16 | 178 | 238 | 45 | 185 | 230 | V naik drastis, S turun |
| Bayangan | 17 | 240 | 88 | 12 | 68 | 98 | V turun, H relatif stabil |

**Catatan:** Rentang H oranye di OpenCV: 10–25. Bandingkan stabilitas H antara oranye dan merah.

---

## 3. Warna Kuning

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | 30 | 225 | 185 | 4 | 182 | 180 | H stabil, S dan V sedang |
| Terang | 28 | 168 | 246 | 38 | 242 | 240 | S turun signifikan, V hampir max |
| Bayangan | 29 | 222 | 100 | 8 | 98 | 96 | V turun, S tetap tinggi |

**Catatan:** Rentang H kuning di OpenCV: 25–35. Amati apakah S turun saat terkena cahaya terang langsung.

---

## 4. Warna Hijau

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | 62 | 248 | 175 | 5 | 172 | 6 | H stabil meski rentang lebar |
| Terang | 60 | 192 | 244 | 22 | 242 | 28 | S turun, V naik, H tetap |
| Bayangan | 63 | 245 | 88 | 7 | 88 | 8 | V turun drastis, S stabil |

**Catatan:** Rentang H hijau di OpenCV: 35–85. Hijau memiliki rentang H terluas — amati apakah H tetap stabil.

---

## 5. Warna Biru

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | 120| 255| 200| 203| 0| 0| |
| Terang | 120| 255| 249| 255| 0| 0| |
| Bayangan | 120| 255| 210| 217| 1| 0| |

**Catatan:** Rentang H biru di OpenCV: 100–130. Bandingkan perubahan channel B (BGR) antara kondisi terang dan bayangan.

---

## 6. Warna Ungu / Magenta

| Kondisi Cahaya | Mean H | Mean S | Mean V | Mean B | Mean G | Mean R | Keterangan |
|---|---|---|---|---|---|---|---|
| Normal | 148 | 220 | 165 | 145 | 10 | 150 | H stabil, B dan R dominan |
| Terang | 145 | 165 | 238 | 195 | 52 | 200 | S turun, V naik, G ikut naik |
| Bayangan | 150 | 218 | 92 | 80 | 8 | 85 | V turun drastis, H sedikit naik |

**Catatan:** Rentang H ungu/magenta di OpenCV: 130–170. Amati apakah warna ini lebih sensitif terhadap perubahan pencahayaan dibanding warna lain.

---

## Tabel Ringkasan — Stabilitas Hue Antar Kondisi

Isi setelah semua pengamatan selesai. Hitung selisih Mean H antara kondisi terang dan bayangan.

| Warna | Mean H Normal | Mean H Terang | Mean H Bayangan | ΔH (Terang−Normal) | ΔH (Bayangan−Normal) |
|---|---|---|---|---|---|
| Merah | 15 | 12 | 10 | −3 | −5 |
| Oranye | 18 | 16 | 17 | −2 | −1 |
| Kuning | 30 | 28 | 29 | −2 | −1 |
| Hijau | 62 | 60 | 63 | −2 | +1 |
| Biru | 120 | 120 | 120 | 0 | 0 |
| Ungu | 148 | 145 | 150 | −3 | +2 |

---

## Tabel Ringkasan — Perubahan Saturasi (S) dan Value (V)

| Warna | S Normal | S Terang | S Bayangan | V Normal | V Terang | V Bayangan |
|---|---|---|---|---|---|---|
| Merah | 233 | 166 | 235 | 82 | 242 | 91 |
| Oranye | 238 | 178 | 240 | 160 | 238 | 88 |
| Kuning | 225 | 168 | 222 | 185 | 246 | 100 |
| Hijau | 248 | 192 | 245 | 175 | 244 | 88 |
| Biru | 255 | 255 | 255 | 200 | 249 | 210 |
| Ungu | 220 | 165 | 218 | 165 | 238 | 92 |

---

## Pertanyaan Analisis

**1.** Channel mana (H, S, atau V) yang paling stabil terhadap perubahan kondisi cahaya? Jelaskan mengapa.

> **Jawaban:** Channel **H (Hue)** paling stabil. Dari tabel ringkasan, ΔH antara kondisi terang dan bayangan hanya berkisar 0–5, sedangkan V bisa berubah hingga 160 (contoh: Merah V=82 → 242 di kondisi terang). Hal ini karena Hue merepresentasikan "jenis" warna murni yang bersifat angular pada roda warna dan tidak bergantung pada intensitas cahaya. Sebaliknya, V merepresentasikan kecerahan dan S merepresentasikan kejernihan — keduanya langsung dipengaruhi oleh jumlah cahaya yang diterima.

---

**2.** Saat kondisi **terang**, apa yang terjadi pada nilai S dan V? Apakah polanya konsisten untuk semua warna?

> **Jawaban:** Saat kondisi terang, nilai **V naik mendekati maksimum (240–249)** karena sensor kamera menerima lebih banyak cahaya, sedangkan nilai **S turun** karena cahaya berlebih membuat warna tampak lebih "pucat" atau *washed out*. Pola ini konsisten untuk hampir semua warna — Merah (S: 233→166), Oranye (238→178), Kuning (225→168), Hijau (248→192), Ungu (220→165). Pengecualian terjadi pada **Biru**, di mana S tetap 255 di semua kondisi, kemungkinan karena objek yang digunakan berwarna biru murni yang sangat jenuh sehingga saturasi tidak berubah meski terpapar cahaya terang.

---

**3.** Saat kondisi **bayangan**, apa yang terjadi pada nilai V? Apakah H tetap bisa digunakan sebagai referensi deteksi?

> **Jawaban:** Saat kondisi bayangan, nilai **V turun drastis** (Merah: 82→91 hanya sedikit, tetapi Oranye: 160→88, Hijau: 175→88, Ungu: 165→92). Ini karena berkurangnya cahaya yang memantul dari permukaan objek. **H tetap bisa digunakan sebagai referensi deteksi** — nilai H di kondisi bayangan hampir sama dengan kondisi normal (ΔH ≤ 5 untuk semua warna). Oleh karena itu, thresholding berbasis H di ruang warna HSV tetap efektif meski pencahayaan berubah, asalkan batas V diperlonggar ke arah nilai rendah.

---

**4.** Berdasarkan pengamatan ini, warna mana yang paling mudah dideteksi secara konsisten di ketiga kondisi cahaya? Mengapa?

> **Jawaban:** **Biru** paling mudah dideteksi secara konsisten. H-nya tidak berubah sama sekali (tetap 120) di ketiga kondisi, dan S-nya juga tetap 255 — artinya tidak ada ambiguitas pada identifikasi warna. Perubahan hanya terjadi pada V (200→249→210), yang mudah diatasi dengan rentang threshold V yang sedikit lebih lebar. **Hijau** dan **Oranye** relatif stabil di H, tetapi perubahan V-nya lebih besar sehingga perlu toleransi lebih.

---

**5.** Jika ingin membuat sistem deteksi warna yang robust terhadap perubahan pencahayaan, nilai batas (lower/upper) channel mana yang sebaiknya diberi toleransi lebih lebar?

> **Jawaban:** Channel **V (Value)** harus diberi toleransi paling lebar, karena perubahannya paling ekstrem (hingga ±160 unit). Batas bawah V harus diturunkan untuk mengakomodasi kondisi bayangan, dan batas atas dinaikkan mendekati 255 untuk kondisi terang. Channel **S (Saturation)** juga perlu toleransi yang cukup karena turun saat kondisi terang (batas bawah S diturunkan sekitar 60–80 unit). Channel **H (Hue)** cukup diberi toleransi kecil (±5–10 unit) karena sudah terbukti paling stabil. Implementasi praktisnya: gunakan `lower = [H−10, 80, 40]` dan `upper = [H+10, 255, 255]` untuk deteksi yang robust.

---

*Worksheet — Pengamatan Histogram Warna | 27 April 2026 | Penelitian OPSI 2026 — SMA Swasta Alfa Centauri*
