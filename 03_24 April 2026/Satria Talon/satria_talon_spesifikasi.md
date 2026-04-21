# UAV Satria Talon — Spesifikasi & Evaluasi Performa

> **Airfoil:** NACA 2412 · **Semi-length:** 2.13 ft (confirmed Plane Maker)  
> **Empty weight:** 3.00 lb (1.361 kg) · **MTOW:** 5.25 lb (2.381 kg)  
> **Wingspan:** ~129.8 cm · **Wing area:** 0.2731 m² · **AR:** 6.17  
> **CG updated:** fwd 0.91 ft · nominal 0.92 ft · aft 0.96 ft

![Satria Talon](Satria%20Talon.png)

> **Catatan metodologi:** Seluruh spesifikasi geometri, berat, dan keseimbangan disusun berdasarkan kajian desain yang dilakukan di **X-Plane Plane Maker** — simulator aerodinamis yang digunakan untuk memodelkan sayap, airfoil, CG envelope, dan parameter performa UAV Satria Talon secara iteratif sebelum divalidasi melalui uji terbang.

![X-Plane Maker — Desain Satria Talon](X-Plane%20Maker.png)

---

## 1. Ringkasan Perubahan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 620 486">
<rect width="620" height="486" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="310" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Before/After — Semi 1.64→2.13 ft + NACA 2412</text>
  <rect x="8" y="40" width="296" height="430" fill="#fff8ee" rx="6" stroke="#BA7517" stroke-width="0.5" opacity="0.6"/>
  <rect x="316" y="40" width="296" height="430" fill="#e6f4ee" rx="6" stroke="#0e6b3d" stroke-width="0.5" opacity="0.7"/>
  <text x="155" y="56" text-anchor="middle" font-size="11" font-weight="bold" fill="#BA7517" font-family="sans-serif">Sebelum</text>
  <text x="465" y="56" text-anchor="middle" font-size="11" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">Sesudah (NACA 2412 + 2.13 ft) ★</text>
  <text x="155" y="68" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">Generic airfoil, semi 1.64 ft</text>
  <text x="465" y="68" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">NACA 2412, semi 2.13 ft</text>
  <text x="310" y="68" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Konfigurasi</text>
  <line x1="8" y1="76" x2="626" y2="76" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="98" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">100 cm</text>
  <text x="465" y="98" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">129.8 cm (~130 cm)</text>
  <text x="310" y="98" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Wingspan</text>
  <line x1="8" y1="106" x2="626" y2="106" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="128" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">1.640 ft</text>
  <text x="465" y="128" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">2.130 ft</text>
  <text x="310" y="128" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Semi-length</text>
  <line x1="8" y1="136" x2="626" y2="136" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="158" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">0.210 m²</text>
  <text x="465" y="158" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">0.273 m²</text>
  <text x="310" y="158" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Wing area</text>
  <line x1="8" y1="166" x2="626" y2="166" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="188" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">4.8</text>
  <text x="465" y="188" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">6.17</text>
  <text x="310" y="188" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Aspect ratio</text>
  <line x1="8" y1="196" x2="626" y2="196" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="218" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">~1.30 (generic)</text>
  <text x="465" y="218" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">1.50 (NACA 2412)</text>
  <text x="310" y="218" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">CLmax</text>
  <line x1="8" y1="226" x2="626" y2="226" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="248" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">0.028</text>
  <text x="465" y="248" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">0.026 (−7%)</text>
  <text x="310" y="248" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">CD0 total</text>
  <line x1="8" y1="256" x2="626" y2="256" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="278" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">10.2</text>
  <text x="465" y="278" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">12.37 (+21%)</text>
  <text x="310" y="278" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">L/D max</text>
  <line x1="8" y1="286" x2="626" y2="286" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="308" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">11.0 m/s (39.6 km/h)</text>
  <text x="465" y="308" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">9.65 m/s (34.7 km/h)  −12%</text>
  <text x="310" y="308" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Stall speed Vs</text>
  <line x1="8" y1="316" x2="626" y2="316" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="338" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">17.9 m/s (64.4 km/h)</text>
  <text x="465" y="338" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">14.74 m/s (53.1 km/h)</text>
  <text x="310" y="338" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Cruise speed</text>
  <line x1="8" y1="346" x2="626" y2="346" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="368" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">64 W</text>
  <text x="465" y="368" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">46 W  (−28%)</text>
  <text x="310" y="368" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Cruise power</text>
  <line x1="8" y1="376" x2="626" y2="376" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="398" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">95 mnt</text>
  <text x="465" y="398" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">131 mnt  (+38%)</text>
  <text x="310" y="398" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Endurance (4S 8Ah)</text>
  <line x1="8" y1="406" x2="626" y2="406" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="428" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">~80 km</text>
  <text x="465" y="428" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">~115 km  (+44%)</text>
  <text x="310" y="428" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">Range one-way (4S 8Ah)</text>
  <line x1="8" y1="436" x2="626" y2="436" stroke="#d4d2c8" stroke-width="0.4"/>
  <text x="155" y="458" text-anchor="middle" font-size="10" fill="#444441" font-family="sans-serif">~34–36 km</text>
  <text x="465" y="458" text-anchor="middle" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">~49–52 km</text>
  <text x="310" y="458" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">RTH radius (4S 8Ah)</text>
  <line x1="8" y1="466" x2="626" y2="466" stroke="#d4d2c8" stroke-width="0.4"/>
</svg>

---

## 2. Weight & Balance (Updated)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 750 366">
  <rect width="750" height="366" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
  <text x="375" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Weight &amp; Balance — Satria Talon (Updated)</text>
  <text x="20" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Parameter</text>
  <text x="260" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Imperial</text>
  <text x="340" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Metrik / Keterangan</text>
  <line x1="8" y1="48" x2="742" y2="48" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="8" y="37" width="734" height="26" fill="#f5f5f5" rx="2"/>
  <text x="20" y="52" font-size="10" fill="#444441" font-family="sans-serif">Empty weight</text>
  <text x="260" y="52" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">3.00 lb</text>
  <text x="340" y="52" font-size="10" fill="#444441" font-family="sans-serif">1.361 kg</text>
  <rect x="8" y="67" width="734" height="26" fill="#ffffff" rx="2"/>
  <text x="20" y="82" font-size="10" fill="#444441" font-family="sans-serif">Maximum weight (MTOW)</text>
  <text x="260" y="82" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">5.25 lb</text>
  <text x="340" y="82" font-size="10" fill="#444441" font-family="sans-serif">2.381 kg</text>
  <rect x="8" y="97" width="734" height="26" fill="#e6f4ee" rx="2"/>
  <text x="20" y="112" font-size="10" fill="#444441" font-family="sans-serif">Payload total (MTOW−empty)</text>
  <text x="260" y="112" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">2.25 lb</text>
  <text x="340" y="112" font-size="10" fill="#0e6b3d" font-family="sans-serif">1.021 kg</text>
  <rect x="8" y="127" width="734" height="26" fill="#ffffff" rx="2"/>
  <text x="20" y="142" font-size="10" fill="#444441" font-family="sans-serif">Fuel load</text>
  <text x="260" y="142" font-size="10" fill="#888780" font-weight="bold" font-family="monospace">0.00 lb</text>
  <text x="340" y="142" font-size="10" fill="#888780" font-family="sans-serif">0 — electric platform</text>
  <rect x="8" y="157" width="734" height="26" fill="#f5f5f5" rx="2"/>
  <text x="20" y="172" font-size="10" fill="#444441" font-family="sans-serif">Long CG — forward limit</text>
  <text x="260" y="172" font-size="10" fill="#378ADD" font-weight="bold" font-family="monospace">0.91 ft</text>
  <text x="340" y="172" font-size="10" fill="#378ADD" font-family="sans-serif">26.4% MAC · 5.56 cm dari LE MAC</text>
  <rect x="8" y="187" width="734" height="26" fill="#e6f4ee" rx="2"/>
  <text x="20" y="202" font-size="10" fill="#444441" font-family="sans-serif">Long CG — default/nominal</text>
  <text x="260" y="202" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">0.92 ft</text>
  <text x="340" y="202" font-size="10" fill="#0e6b3d" font-family="sans-serif">27.9% MAC · 5.87 cm dari LE MAC ✓</text>
  <rect x="8" y="217" width="734" height="26" fill="#f5f5f5" rx="2"/>
  <text x="20" y="232" font-size="10" fill="#444441" font-family="sans-serif">Long CG — aft limit</text>
  <text x="260" y="232" font-size="10" fill="#D85A30" font-weight="bold" font-family="monospace">0.96 ft</text>
  <text x="340" y="232" font-size="10" fill="#D85A30" font-family="sans-serif">33.7% MAC · 7.09 cm dari LE MAC</text>
  <rect x="8" y="247" width="734" height="26" fill="#ffffff" rx="2"/>
  <text x="20" y="262" font-size="10" fill="#444441" font-family="sans-serif">Vert CG</text>
  <text x="260" y="262" font-size="10" fill="#888780" font-weight="bold" font-family="monospace">0.00 ft</text>
  <text x="340" y="262" font-size="10" fill="#888780" font-family="sans-serif">—</text>
  <rect x="8" y="277" width="734" height="26" fill="#e6f4ee" rx="2"/>
  <text x="20" y="292" font-size="10" fill="#444441" font-family="sans-serif">Static margin @ nominal CG</text>
  <text x="260" y="292" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">—</text>
  <text x="340" y="292" font-size="10" fill="#0e6b3d" font-family="sans-serif">~12.1% MAC (NP est. ~40% MAC) — AMAN</text>
  <rect x="8" y="307" width="734" height="26" fill="#ffffff" rx="2"/>
  <text x="20" y="322" font-size="10" fill="#444441" font-family="sans-serif">Static margin @ aft limit</text>
  <text x="260" y="322" font-size="10" fill="#BA7517" font-weight="bold" font-family="monospace">—</text>
  <text x="340" y="322" font-size="10" fill="#BA7517" font-family="sans-serif">~6.3% MAC — MARGINAL (jangan dilampaui)</text>
</svg>

### Payload Breakdown @ MTOW 2.381 kg

| Komponen | Berat | Sisa kargo |
|---|---|---|
| Empty weight | 1.361 kg | 1.021 kg |
| + Baterai 4S 6000 mAh | +350 g | **671 g** |
| **+ Baterai 4S 8000 mAh** | **+450 g** | **571 g** |

### Analisis Perubahan CG Envelope

| Titik CG | Lama | Baru | Perubahan |
|---|---|---|---|
| Forward limit | 0.90 ft (25.0% MAC) | **0.91 ft (26.4% MAC)** | +0.01 ft, maju +1.4% |
| Default/nominal | 0.95 ft (32.2% MAC) | **0.92 ft (27.9% MAC)** | −0.03 ft, mundur −4.3% |
| **Aft limit** | 1.00 ft (39.5% MAC) | **0.96 ft (33.7% MAC)** | **−0.04 ft, mundur −5.8%** |

> **Mengapa aft limit diperketat ke 0.96 ft?**  
> NACA 2412 memiliki Cm_ac = −0.05 (pitching moment nose-down). Semakin CG ke belakang, momen ini semakin sulit dikompensasi — terutama di kecepatan rendah mendekati stall. Batas 0.96 ft (33.7% MAC) memberikan static margin minimum ~6.3% yang masih aman. Melampaui ini berisiko pitch-up instability.

---

## 3. CG Envelope (Updated)

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 580 130">
  <defs><marker id="arr" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 1L9 5L1 9" fill="none" stroke="#0e6b3d" stroke-width="1.5"/></marker></defs>
  <rect width="580" height="130" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
  <text x="290" y="22" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">CG Envelope — Satria Talon (Updated)</text>
  <text x="290" y="36" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · Semi 2.13 ft · Aft limit diperketat: 1.00 ft → 0.96 ft</text>
  <rect x="338" y="56" width="71" height="32" fill="#e6f4ee" rx="4" opacity="0.75"/>
  <rect x="409" y="62" width="57" height="20" fill="#fde8e8" rx="2" opacity="0.6"/>
  <text x="437" y="77" text-anchor="middle" font-size="8" fill="#D85A30" font-family="sans-serif">removed</text>
  <line x1="38" y1="72" x2="538" y2="72" stroke="#d4d2c8" stroke-width="1.5"/>
  <text x="36" y="90" font-size="9" fill="#888780" font-family="sans-serif">nose→</text>
  <text x="538" y="90" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">←tail</text>
  <line x1="466" y1="52" x2="466" y2="92" stroke="#888780" stroke-width="1" stroke-dasharray="3,2"/>
  <text x="466" y="48" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">old aft 1.00ft</text>
  <line x1="77" y1="54" x2="77" y2="90" stroke="#888780" stroke-width="1.5"/>
  <text x="77" y="45" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">LE MAC</text>
  <text x="77" y="102" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.7275 ft</text>
  <line x1="338" y1="54" x2="338" y2="90" stroke="#378ADD" stroke-width="2.5"/>
  <text x="338" y="45" text-anchor="middle" font-size="9" fill="#378ADD" font-weight="bold" font-family="sans-serif">26.4% fwd ★</text>
  <text x="338" y="102" text-anchor="middle" font-size="8" fill="#378ADD" font-family="sans-serif">0.91 ft</text>
  <line x1="352" y1="54" x2="352" y2="90" stroke="#0e6b3d" stroke-width="2.5"/>
  <text x="352" y="45" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">27.9% nominal ✓</text>
  <text x="352" y="102" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">0.92 ft</text>
  <line x1="409" y1="54" x2="409" y2="90" stroke="#D85A30" stroke-width="1.5"/>
  <text x="409" y="50" text-anchor="middle" font-size="9" fill="#D85A30" font-weight="normal" font-family="sans-serif">33.7% aft</text>
  <text x="409" y="102" text-anchor="middle" font-size="8" fill="#D85A30" font-family="sans-serif">0.96 ft</text>
  <line x1="352" y1="116" x2="471" y2="116" stroke="#0e6b3d" stroke-width="1" marker-end="url(#arr)"/>
  <text x="411" y="128" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">static margin ~12.1% MAC (AMAN)</text>
  <line x1="471" y1="64" x2="471" y2="80" stroke="#888780" stroke-width="1" stroke-dasharray="2,2"/>
  <text x="471" y="60" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">NP est. ~40%</text>
</svg>

| Titik CG | Nilai | % MAC | Dari LE MAC | Static Margin | Status |
|---|---|---|---|---|---|
| LE MAC (referensi) | 0.7275 ft | 0% | 0 cm | — | — |
| **Forward limit** | **0.91 ft** | **26.4%** | **5.56 cm** | 13.6% | AMAN |
| **Nominal terbang** | **0.92 ft** | **27.9%** | **5.87 cm** | 12.1% | **AMAN ✓** |
| **Aft limit (JANGAN dilampaui)** | **0.96 ft** | **33.7%** | **7.09 cm** | 6.3% | MARGINAL |
| Neutral Point (estimasi) | ~1.001 ft | ~40% | ~8.4 cm | — | referensi |

**Cara mengukur CG fisik (updated):**
1. Dari root LE, ukur ke tip sejauh **~29% semi-span** (~18.8 cm) → titik LE MAC
2. Tandai **5.56–5.87 cm ke belakang** dari LE MAC → zona CG terbang
3. **Jangan melebihi 7.09 cm** dari LE MAC (aft limit baru 0.96 ft)
4. Seimbangkan di dua jari → validasi dengan hand-launch glide

---

## 4. Geometri Sayap

### Wing 1

| Parameter | Imperial | Metrik |
|---|---|---|
| **Semi-length** | **2.13 ft** | **64.92 cm** |
| **Wingspan** | **4.26 ft** | **~129.8 cm** |
| Root chord | 0.78 ft | 23.77 cm |
| Tip chord | 0.60 ft | 18.29 cm |
| Taper ratio | — | 0.769 |
| MAC | 0.690 ft | 21.03 cm |
| Wing area | 2.94 ft² | **0.2731 m²** |
| Aspect ratio | — | **6.174** |
| Sweep / Dihedral | 0.0° / 0.0° | — |
| Long arm (aero ref) | 0.90 ft | 27.43 cm |

### Wing 2 — Winglet

| Parameter | Nilai |
|---|---|
| Semi-length | 0.43 ft |
| Root chord | 0.60 ft |
| Tip chord | 0.08 ft |
| Sweep | 80.0° |
| Dihedral | 20.0° |
| **Lat arm (= Wing 1 semi)** | **2.13 ft** |

### Vertical Stabilizer — V-tail (×2)

| Parameter | Imperial | Metrik |
|---|---|---|
| Height | 0.65 ft | 19.8 cm |
| Root chord | 0.56 ft | 17.1 cm |
| Tip chord | 0.25 ft | 7.6 cm |
| Sweep | 40.0° | — |
| Dihedral kedua fin | 45.0° | — |

---

## 5. Airfoil NACA 2412

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 348">
<rect width="660" height="348" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="330" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Karakteristik Airfoil NACA 2412</text>
  <text x="20" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Parameter</text>
<text x="200" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Nilai</text>
<text x="310" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Catatan</text>
<line x1="8" y1="48" x2="652" y2="48" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="8" y="38" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="52" font-size="10" fill="#444441" font-family="sans-serif">Profil</text>
  <text x="200" y="52" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">NACA 2412</text>
  <text x="310" y="52" font-size="10" fill="#888780" font-family="sans-serif">Camber 2% · max camber di 40% chord · t/c 12%</text>
  <rect x="8" y="66" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="80" font-size="10" fill="#444441" font-family="sans-serif">CLmax (Re~700k)</text>
  <text x="200" y="80" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">1.50</text>
  <text x="310" y="80" font-size="10" fill="#888780" font-family="sans-serif">vs generic ~1.30 (+15%)</text>
  <rect x="8" y="94" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="108" font-size="10" fill="#444441" font-family="sans-serif">CD0 profil</text>
  <text x="200" y="108" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">0.0075</text>
  <text x="310" y="108" font-size="10" fill="#888780" font-family="sans-serif">Lebih rendah dari foil tebal — laminar sebagian</text>
  <rect x="8" y="122" width="644" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="136" font-size="10" fill="#444441" font-family="sans-serif">CD0 total</text>
  <text x="200" y="136" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">0.026</text>
  <text x="310" y="136" font-size="10" fill="#888780" font-family="sans-serif">vs generic 0.028 (−7.1%)</text>
  <rect x="8" y="150" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="164" font-size="10" fill="#444441" font-family="sans-serif">Oswald efficiency e</text>
  <text x="200" y="164" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">0.82</text>
  <text x="310" y="164" font-size="10" fill="#888780" font-family="sans-serif">vs generic 0.78 (+5.1%)</text>
  <rect x="8" y="178" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="192" font-size="10" fill="#444441" font-family="sans-serif">L/D max</text>
  <text x="200" y="192" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">12.37</text>
  <text x="310" y="192" font-size="10" fill="#888780" font-family="sans-serif">vs generic 10.7 (+15.6%)</text>
  <rect x="8" y="206" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="220" font-size="10" fill="#444441" font-family="sans-serif">Zero-lift AoA</text>
  <text x="200" y="220" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">−2.1°</text>
  <text x="310" y="220" font-size="10" fill="#888780" font-family="sans-serif">Positif camber → slight nose-down at zero lift</text>
  <rect x="8" y="234" width="644" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="248" font-size="10" fill="#444441" font-family="sans-serif">Stall AoA</text>
  <text x="200" y="248" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">~16.5°</text>
  <text x="310" y="248" font-size="10" fill="#888780" font-family="sans-serif">Stall ringan — gradual, forgiving</text>
  <rect x="8" y="262" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="276" font-size="10" fill="#444441" font-family="sans-serif">Cm_ac</text>
  <text x="200" y="276" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">−0.05</text>
  <text x="310" y="276" font-size="10" fill="#888780" font-family="sans-serif">Nose-down pitching moment → CG tidak boleh terlalu belakang</text>
  <rect x="8" y="290" width="644" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="304" font-size="10" fill="#444441" font-family="sans-serif">AoA @ cruise</text>
  <text x="200" y="304" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">3.83°</text>
  <text x="310" y="304" font-size="10" fill="#888780" font-family="sans-serif">Dari zero-lift + CL_cruise/Cl_alpha</text>
</svg>

---

## 6. Performa Aerodinamis (MTOW 2.381 kg, NACA 2412)

| Parameter | Nilai |
|---|---|
| Wing loading | **85.5 N/m²** |
| **Stall speed Vs** | **9.65 m/s (34.7 km/h)** |
| Min safe airspeed (1.2×Vs) | 11.58 m/s (41.7 km/h) |
| **Best cruise speed** | **14.74 m/s (53.1 km/h)** |
| AoA saat cruise | **3.83°** |
| Best range speed | ~16.95 m/s (61.0 km/h) |
| **VNE** | **33.77 m/s (121.6 km/h)** |
| **L/D max** | **12.37** |
| Thrust @ cruise | 1.89 N |

---

## 7. Analisis Wingspan vs Daya Angkat

### Endurance vs Wingspan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260">
<rect width="600" height="260" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Endurance vs Wingspan — 4S 8000 mAh</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb (2.381 kg) · semi-length 2.13 ft</text>
<line x1="140" y1="44" x2="140" y2="242" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="140" y="45" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="47" width="58" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="59" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="203" y="59" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">83 mnt</text>
  <rect x="140" y="69" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="71" width="88" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="83" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="233" y="83" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">95 mnt</text>
  <rect x="140" y="93" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="95" width="119" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="107" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="264" y="107" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">107 mnt</text>
  <rect x="140" y="117" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="119" width="149" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="131" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="294" y="131" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">119 mnt</text>
  <rect x="140" y="141" width="330" height="21" fill="#e6f4ee" rx="2"/>
  <rect x="140" y="143" width="182" height="17" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="134" y="155" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="327" y="155" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">132 mnt ← 130 cm (saat ini)</text>
  <rect x="140" y="165" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="167" width="213" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="179" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="358" y="179" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">144 mnt</text>
  <rect x="140" y="189" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="191" width="246" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="203" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="391" y="203" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">157 mnt</text>
  <rect x="140" y="213" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="215" width="281" height="17" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="134" y="227" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="426" y="227" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">171 mnt</text>
</svg>

### Wing Loading vs Wingspan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260">
<rect width="600" height="260" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Wing Loading vs Wingspan</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb (2.381 kg) · semi-length 2.13 ft</text>
<line x1="140" y1="44" x2="140" y2="242" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="140" y="45" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="47" width="253" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="59" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="398" y="59" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">123 N/m²</text>
  <rect x="140" y="69" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="71" width="211" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="83" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="356" y="83" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">111 N/m²</text>
  <rect x="140" y="93" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="95" width="177" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="107" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="322" y="107" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">101 N/m²</text>
  <rect x="140" y="117" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="119" width="149" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="131" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="294" y="131" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">93 N/m²</text>
  <rect x="140" y="141" width="330" height="21" fill="#e6f4ee" rx="2"/>
  <rect x="140" y="143" width="121" height="17" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="134" y="155" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="266" y="155" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">85 N/m² ← 130 cm (saat ini)</text>
  <rect x="140" y="165" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="167" width="100" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="179" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="245" y="179" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">79 N/m²</text>
  <rect x="140" y="189" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="191" width="83" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="203" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="228" y="203" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">74 N/m²</text>
  <rect x="140" y="213" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="215" width="66" height="17" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="134" y="227" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="211" y="227" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">69 N/m²</text>
</svg>

### Kecepatan vs Wingspan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260">
<rect width="600" height="260" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Kecepatan vs Wingspan</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft</text>
  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">21</text>
  <line x1="44" y1="86" x2="584" y2="86" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="90" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">18</text>
  <line x1="44" y1="129" x2="584" y2="129" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="133" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">14</text>
  <line x1="44" y1="171" x2="584" y2="171" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="175" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">11</text>
  <line x1="44" y1="214" x2="584" y2="214" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="218" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">8</text>
  <text x="44" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="121" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <text x="198" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">110</text>
  <text x="275" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">120</text>
  <text x="352" y="227" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130</text>
  <text x="429" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">140</text>
  <text x="506" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">150</text>
  <text x="584" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">160</text>
  <rect x="350" y="44" width="4" height="170" fill="#0e6b3d" opacity="0.15"/>
  <polyline points="44,69 121,87 198,102 275,116 352,127 429,137 506,146 584,153" fill="none" stroke="#534AB7" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="69" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="87" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="102" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="116" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="127" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="137" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="146" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="153" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,166 121,173 198,179 275,185 352,190 429,194 506,198 584,202" fill="none" stroke="#D85A30" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="166" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="173" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="179" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="185" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="190" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="194" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="198" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="202" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <line x1="352" y1="44" x2="352" y2="214" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="352" y="240" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">130 cm saat ini</text>
  <text x="44" y="254" font-size="9" fill="#534AB7" font-family="sans-serif">—— Vcruise (m/s)</text>
  <text x="161.5" y="254" font-size="9" fill="#D85A30" font-family="sans-serif">- -  Vstall (m/s)</text>
</svg>

### Aspect Ratio & L/D vs Wingspan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260">
<rect width="600" height="260" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Aspect Ratio & L/D max vs Wingspan</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft</text>
  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">15</text>
  <line x1="44" y1="86" x2="584" y2="86" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="90" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">12</text>
  <line x1="44" y1="129" x2="584" y2="129" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="133" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">9</text>
  <line x1="44" y1="171" x2="584" y2="171" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="175" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">7</text>
  <line x1="44" y1="214" x2="584" y2="214" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="218" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">4</text>
  <text x="44" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="121" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <text x="198" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">110</text>
  <text x="275" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">120</text>
  <text x="352" y="227" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130</text>
  <text x="429" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">140</text>
  <text x="506" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">150</text>
  <text x="584" y="227" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">160</text>
  <rect x="350" y="44" width="4" height="170" fill="#0e6b3d" opacity="0.15"/>
  <polyline points="44,207 121,199 198,193 275,186 352,178 429,171 506,165 584,157" fill="none" stroke="#0e6b3d" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="207" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="199" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="193" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="186" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="178" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="171" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="165" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="157" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,116 121,107 198,100 275,92 352,85 429,79 506,71 584,65" fill="none" stroke="#BA7517" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="116" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="107" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="100" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="92" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="85" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="79" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="71" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="65" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <line x1="352" y1="44" x2="352" y2="214" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="352" y="240" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">130 cm saat ini</text>
  <text x="44" y="254" font-size="9" fill="#0e6b3d" font-family="sans-serif">—— Aspect Ratio</text>
  <text x="156.0" y="254" font-size="9" fill="#BA7517" font-family="sans-serif">- -  L/D max</text>
</svg>

### Cruise Power vs Wingspan

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 260">
<rect width="600" height="260" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Cruise Power vs Wingspan (W)</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb (2.381 kg) · semi-length 2.13 ft</text>
<line x1="140" y1="44" x2="140" y2="242" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="140" y="45" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="47" width="249" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="59" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="394" y="59" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">73 W</text>
  <rect x="140" y="69" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="71" width="207" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="83" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="352" y="83" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">64 W</text>
  <rect x="140" y="93" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="95" width="174" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="107" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="319" y="107" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">57 W</text>
  <rect x="140" y="117" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="119" width="146" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="131" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="291" y="131" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">51 W</text>
  <rect x="140" y="141" width="330" height="21" fill="#e6f4ee" rx="2"/>
  <rect x="140" y="143" width="122" height="17" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="134" y="155" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="267" y="155" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">46 W ← 130 cm (saat ini)</text>
  <rect x="140" y="165" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="167" width="103" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="179" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="248" y="179" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">42 W</text>
  <rect x="140" y="189" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="191" width="84" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="203" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="229" y="203" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">38 W</text>
  <rect x="140" y="213" width="330" height="21" fill="#f5f5f5" rx="2"/>
  <rect x="140" y="215" width="70" height="17" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="134" y="227" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="215" y="227" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">35 W</text>
</svg>

### Tabel Lengkap

| Wingspan | Area | AR | WL | Vs | Vcruise | L/D | P cruise | Endurance (4S 8Ah) |
|---|---|---|---|---|---|---|---|---|
| 90 cm | 0.189 m² | 4.3 | 123 N/m² | 11.6 m/s | 19.4 m/s | 10.3 | 73 W | 83 mnt |
| 100 cm | 0.210 m² | 4.8 | 111 N/m² | 11.0 m/s | 17.9 m/s | 10.9 | 64 W | 95 mnt |
| 110 cm | 0.232 m² | 5.2 | 101 N/m² | 10.5 m/s | 16.7 m/s | 11.4 | 57 W | 107 mnt |
| 120 cm | 0.253 m² | 5.7 | 93 N/m² | 10.0 m/s | 15.6 m/s | 11.9 | 51 W | 119 mnt |
| **~130 cm ★ saat ini** | **0.273 m²** | **6.17** | **85 N/m²** | **9.65 m/s** | **14.74 m/s** | **12.37** | **46 W** | **131 mnt** |
| 140 cm | 0.295 m² | 6.7 | 79 N/m² | 9.3 m/s | 13.9 m/s | 12.8 | 42 W | 144 mnt |
| 150 cm | 0.316 m² | 7.1 | 74 N/m² | 9.0 m/s | 13.2 m/s | 13.3 | 38 W | 157 mnt |
| 160 cm | 0.337 m² | 7.6 | 69 N/m² | 8.7 m/s | 12.6 m/s | 13.7 | 35 W | 171 mnt |

---

## 8. Propulsi

### Power Budget

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 210">
<rect width="660" height="210" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="330" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Power Budget — Satria Talon (NACA 2412)</text>
<text x="330" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">MTOW 5.25 lb · semi 2.13 ft · sys. eff. 60.6%</text>
  <rect x="220" y="52" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="220" y="52" width="63" height="26" fill="#1D9E75" rx="3" opacity="0.88"/>
  <text x="216" y="69" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Cruise (46 W · 0.062 HP)</text>
  <rect x="220" y="90" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="220" y="90" width="277" height="26" fill="#BA7517" rx="3" opacity="0.88"/>
  <text x="216" y="107" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Climb 4m/s (200 W · 0.268 HP)</text>
  <rect x="220" y="128" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="220" y="128" width="346" height="26" fill="#D85A30" rx="3" opacity="0.88"/>
  <text x="216" y="145" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Peak ×1.25 (250 W · 0.336 HP)</text>
  <rect x="220" y="166" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="220" y="166" width="416" height="26" fill="#993C1D" rx="3" opacity="0.88"/>
  <text x="216" y="183" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Motor rating min (300 W · 0.403 HP)</text>
<text x="654" y="205" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">L/D max 12.37 · Thrust cruise 1.89 N · NACA 2412 CLmax 1.50</text>
</svg>

| Kondisi | Daya Listrik | HP |
|---|---|---|
| **Cruise (14.74 m/s)** | **46 W** | **0.062 HP** |
| Climb (ROC 4 m/s) | 200 W | 0.268 HP |
| Peak + gust (×1.25) | **250 W** | **0.335 HP** |
| **Motor rating min** | **≥ 300 W** | **≥ 0.403 HP** |

### Propeller

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 185">
<rect width="600" height="185" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/>
<text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Static Thrust vs Propeller — @ Peak 250 W</text>
<text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">Advance ratio J=0.55 · Vcruise 14.74 m/s · MTOW 2.381 kg</text>
  <rect x="90" y="52" width="430" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="52" width="339" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="70" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">10×5.0</text>
  <text x="434" y="70" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">14.2 N · T/W 0.61 · RPM 6394 · KV@4S 617</text>
  <rect x="90" y="96" width="430" height="28" fill="#e6f4ee" rx="3"/>
  <rect x="90" y="96" width="360" height="28" fill="#0e6b3d" rx="3" opacity="0.88"/>
  <text x="86" y="114" text-anchor="end" font-size="12" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">11×5.5  ★</text>
  <text x="455" y="114" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">15.1 N · T/W 0.65 · RPM 5754 · KV@4S 555</text>
  <rect x="90" y="140" width="430" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="140" width="382" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="158" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">12×6.0</text>
  <text x="477" y="158" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">16.0 N · T/W 0.69 · RPM 5275 · KV@4S 508</text>
</svg>

| Propeller | RPM cruise | KV @ 4S | T static | T/W |
|---|---|---|---|---|
| 10×5.0 | 6.394 | 617 | 14.2 N | 0.61 |
| **11×5.5 ★** | **5.754** | **555** | **15.1 N** | **0.65** |
| 12×6.0 | 5.275 | 508 | 16.0 N | 0.69 |

### Motor & ESC & Baterai

| Parameter | Nilai |
|---|---|
| Motor | Brushless 2216, **KV 555–600 @ 4S** |
| Power rating | ≥ 300 W (gunakan 350–450 W) |
| ESC | **40 A BLHeli_32**, BEC 5V/3A |
| **Baterai rekomendasi** | **4S 8000 mAh** |
| Cruise current | ~3.1 A (~46 W) |
| C-rate saat peak | **2.1C** (sangat aman) |

| Baterai | Endurance | Kargo bersih | C-rate |
|---|---|---|---|
| 3S 5000 mAh | ~62 mnt | 740 g | 4.5C |
| 4S 5000 mAh | ~82 mnt | 700 g | 3.4C |
| 4S 6000 mAh | ~99 mnt | 670 g | 2.8C |
| **4S 8000 mAh** | **~131 mnt** | **571 g** | **2.1C** |

---

## 9. Misi Delivery

| Kargo | Endurance | Vcruise | Range one-way | Radius RTH |
|---|---|---|---|---|
| 300 g | ~131 mnt | 14.74 m/s | **~116 km** | **~49–52 km** |
| **500 g** | **~131 mnt** | **14.74 m/s** | **~116 km** | **~49–52 km** |
| 571 g (maks) | ~131 mnt | 14.74 m/s | ~116 km | **~49–52 km** |

---

## 10. Ringkasan Spesifikasi Final

| Parameter | Nilai |
|---|---|
| **Airfoil** | **NACA 2412** |
| **Semi-length** | **2.13 ft** |
| **Wingspan** | **~129.8 cm** |
| Wing area | 0.2731 m² |
| Aspect ratio | 6.174 |
| MAC | 21.03 cm · 0.690 ft |
| Taper ratio | 0.769 |
| Konfigurasi ekor | V-tail twin fin (dihedral 45°) |
| **Empty weight** | **3.00 lb = 1.361 kg** |
| **MTOW** | **5.25 lb = 2.381 kg** |
| Payload total | 1.021 kg |
| Kargo (4S 8Ah) | **571 g** |
| **CG forward limit** | **0.91 ft = 26.4% MAC = 5.56 cm dari LE MAC** |
| **CG nominal (terbang)** | **0.92 ft = 27.9% MAC = 5.87 cm dari LE MAC ✓** |
| **CG aft limit** | **0.96 ft = 33.7% MAC = 7.09 cm dari LE MAC** |
| Wing loading | 85.5 N/m² |
| **Stall speed Vs** | **9.65 m/s (34.7 km/h)** |
| **Cruise speed** | **14.74 m/s (53.1 km/h)** |
| AoA cruise | 3.83° |
| VNE | 33.77 m/s (121.6 km/h) |
| **L/D max** | **12.37** |
| **Cruise power** | **46 W (0.062 HP)** |
| Peak power | 250 W (0.335 HP) |
| Motor rating min | 300 W (0.403 HP) |
| **Endurance (4S 8Ah)** | **~131 mnt** |
| **Range one-way** | **~116 km** |
| **Radius RTH** | **~49–52 km** |
| Motor | 2216, **KV 555–600 @ 4S** |
| Propeller | **APC 11×5.5E** |
| ESC | 40 A BLHeli_32 |
| Baterai | **4S 8000 mAh** |

---

*UAV Satria Talon · NACA 2412 · Semi 2.13 ft · V-tail · Empty 3.00 lb · MTOW 5.25 lb*  
*CG updated: fwd 0.91 ft · nominal 0.92 ft · aft 0.96 ft (diperketat untuk NACA 2412)*  
*Seluruh nilai performa adalah estimasi teoritis — wajib divalidasi melalui uji terbang.*
