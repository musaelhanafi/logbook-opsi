# UAV Satria Talon — Spesifikasi Lengkap

> **Airfoil:** NACA 2412 · **Semi-length:** 2.13 ft · **Root:** 0.78 ft · **Tip:** 0.60 ft · **Sweep:** 0°  
> **Empty:** 3.00 lb (1.361 kg) · **MTOW:** 5.25 lb (2.381 kg) · **Wingspan:** 129.8 cm  
> **CG:** fwd 0.91 ft · nominal 0.92 ft · aft 0.96 ft

---

## Tentang LE dan MAC

**LE (Leading Edge)** = tepi depan sayap — titik referensi pengukuran CG secara fisik.

**MAC (Mean Aerodynamic Chord)** = chord rata-rata aerodinamis yang mewakili seluruh sayap. Satria Talon:
- MAC berada di **31.0 cm dari CL** (kiri dan kanan), di **47.8% semi-span**
- Panjang MAC = **21.03 cm**
- Karena sweep **0°**, LE lurus sejajar — ukur langsung dari tepi depan sayap

---

## 1. Airfoil NACA 2412

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 660 320"><rect width="660" height="320" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="330" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Karakteristik Airfoil NACA 2412</text>  <text x="20" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Parameter</text>
  <text x="190" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Nilai</text>
  <text x="300" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Catatan</text>
  <line x1="8" y1="48" x2="652" y2="48" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="8" y="38" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="52" font-size="10" fill="#444441" font-family="sans-serif">Profil</text>
  <text x="190" y="52" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">NACA 2412</text>
  <text x="300" y="52" font-size="10" fill="#888780" font-family="sans-serif">Camber 2% · max camber 40% chord · t/c 12%</text>
  <rect x="8" y="66" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="80" font-size="10" fill="#444441" font-family="sans-serif">CLmax (Re~700k)</text>
  <text x="190" y="80" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">1.50</text>
  <text x="300" y="80" font-size="10" fill="#888780" font-family="sans-serif">vs generic ~1.30 (+15%)</text>
  <rect x="8" y="94" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="108" font-size="10" fill="#444441" font-family="sans-serif">CD0 total</text>
  <text x="190" y="108" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">0.026</text>
  <text x="300" y="108" font-size="10" fill="#888780" font-family="sans-serif">Lebih rendah dari foil tebal</text>
  <rect x="8" y="122" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="136" font-size="10" fill="#444441" font-family="sans-serif">Oswald efficiency e</text>
  <text x="190" y="136" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">0.82</text>
  <text x="300" y="136" font-size="10" fill="#888780" font-family="sans-serif">Span efficiency baik</text>
  <rect x="8" y="150" width="644" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="164" font-size="10" fill="#444441" font-family="sans-serif">L/D max</text>
  <text x="190" y="164" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">12.37</text>
  <text x="300" y="164" font-size="10" fill="#888780" font-family="sans-serif">vs generic ~10.2 (+21%)</text>
  <rect x="8" y="178" width="644" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="192" font-size="10" fill="#444441" font-family="sans-serif">Zero-lift AoA</text>
  <text x="190" y="192" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">−2.1°</text>
  <text x="300" y="192" font-size="10" fill="#888780" font-family="sans-serif">Positive camber → slight nose-down at zero lift</text>
  <rect x="8" y="206" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="220" font-size="10" fill="#444441" font-family="sans-serif">Stall AoA</text>
  <text x="190" y="220" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">~16.5°</text>
  <text x="300" y="220" font-size="10" fill="#888780" font-family="sans-serif">Gradual, forgiving — recovery mudah</text>
  <rect x="8" y="234" width="644" height="24" fill="#fff8ee" rx="2"/>
  <text x="20" y="248" font-size="10" fill="#444441" font-family="sans-serif">Cm_ac</text>
  <text x="190" y="248" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">−0.05</text>
  <text x="300" y="248" font-size="10" fill="#888780" font-family="sans-serif">Nose-down pitching moment → CG tidak terlalu belakang</text>
  <rect x="8" y="262" width="644" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="276" font-size="10" fill="#444441" font-family="sans-serif">AoA @ cruise</text>
  <text x="190" y="276" font-size="10" fill="#444441" font-weight="bold" font-family="sans-serif">3.76°</text>
  <text x="300" y="276" font-size="10" fill="#888780" font-family="sans-serif">Dari zero-lift + CL_cruise/Cl_alpha</text></svg>

---

## 2. Weight & Balance

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 745 292"><rect width="745" height="292" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="372" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Weight &amp; Balance — Satria Talon</text>  <text x="20" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Parameter</text>
  <text x="195" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Imperial</text>
  <text x="280" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Keterangan</text>
  <line x1="8" y1="48" x2="738" y2="48" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="8" y="38" width="730" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="52" font-size="10" fill="#444441" font-family="sans-serif">Empty weight</text>
  <text x="195" y="52" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">3.00 lb</text>
  <text x="280" y="52" font-size="10" fill="#444441" font-family="sans-serif">1.361 kg</text>
  <rect x="8" y="66" width="730" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="80" font-size="10" fill="#444441" font-family="sans-serif">Maximum weight (MTOW)</text>
  <text x="195" y="80" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">5.25 lb</text>
  <text x="280" y="80" font-size="10" fill="#444441" font-family="sans-serif">2.381 kg</text>
  <rect x="8" y="94" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="108" font-size="10" fill="#444441" font-family="sans-serif">Payload total</text>
  <text x="195" y="108" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">2.25 lb</text>
  <text x="280" y="108" font-size="10" fill="#0e6b3d" font-family="sans-serif">1.021 kg</text>
  <rect x="8" y="122" width="730" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="136" font-size="10" fill="#444441" font-family="sans-serif">LE MAC dari origin</text>
  <text x="195" y="136" font-size="10" fill="#888780" font-weight="bold" font-family="monospace">0.7275 ft</text>
  <text x="280" y="136" font-size="10" fill="#888780" font-family="sans-serif">22.17 cm</text>
  <rect x="8" y="150" width="730" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="164" font-size="10" fill="#444441" font-family="sans-serif">CG fwd limit</text>
  <text x="195" y="164" font-size="10" fill="#378ADD" font-weight="bold" font-family="monospace">0.91 ft</text>
  <text x="280" y="164" font-size="10" fill="#378ADD" font-family="sans-serif">26.5% MAC · 5.56 cm dari LE MAC</text>
  <rect x="8" y="178" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="192" font-size="10" fill="#444441" font-family="sans-serif">CG nominal ✓</text>
  <text x="195" y="192" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">0.92 ft</text>
  <text x="280" y="192" font-size="10" fill="#0e6b3d" font-family="sans-serif">27.9% MAC · 5.87 cm dari LE MAC</text>
  <rect x="8" y="206" width="730" height="24" fill="#fff8ee" rx="2"/>
  <text x="20" y="220" font-size="10" fill="#444441" font-family="sans-serif">CG aft limit</text>
  <text x="195" y="220" font-size="10" fill="#BA7517" font-weight="bold" font-family="monospace">0.96 ft</text>
  <text x="280" y="220" font-size="10" fill="#BA7517" font-family="sans-serif">33.7% MAC · 7.09 cm dari LE MAC  (SM 6.3%)</text>
  <rect x="8" y="234" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="248" font-size="10" fill="#444441" font-family="sans-serif">SM @ nominal</text>
  <text x="195" y="248" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">—</text>
  <text x="280" y="248" font-size="10" fill="#0e6b3d" font-family="sans-serif">~12.1% MAC (NP est. ~40%) — AMAN ✓</text></svg>

### CG Envelope

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250"><rect width="680" height="250" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="340" y="19" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">CG Envelope — Satria Talon</text><text x="340" y="33" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · Semi 2.13 ft · root 0.78 ft · tip 0.60 ft · MAC 21.03 cm</text>  <rect x="408" y="96" width="75" height="44" fill="#e6f4ee" rx="3" opacity="0.8"/>
  <text x="445" y="123" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">safe zone</text>
  <line x1="50" y1="118" x2="630" y2="118" stroke="#d4d2c8" stroke-width="1.5"/>
  <text x="46" y="123" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">nose</text>
  <text x="634" y="123" text-anchor="start" font-size="9" fill="#888780" font-family="sans-serif">tail</text>
  <line x1="90" y1="114" x2="90" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="90" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.70</text>
  <line x1="165" y1="114" x2="165" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="165" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.75</text>
  <line x1="241" y1="114" x2="241" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="241" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.80</text>
  <line x1="317" y1="114" x2="317" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="317" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.85</text>
  <line x1="392" y1="114" x2="392" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="392" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.90</text>
  <line x1="468" y1="114" x2="468" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="468" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.95</text>
  <line x1="544" y1="114" x2="544" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="544" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">1.00</text>
  <line x1="620" y1="114" x2="620" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="620" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">1.05</text>
  <defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 2L9 5L1 8" fill="none" stroke="#0e6b3d" stroke-width="1.5" stroke-linejoin="round"/></marker></defs>
  <line x1="425" y1="178" x2="547" y2="178" stroke="#0e6b3d" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr)"/>
  <text x="486" y="192" text-anchor="middle" font-size="9" fill="#0e6b3d" font-family="sans-serif">static margin ~12.1% MAC</text>
  <line x1="131" y1="82" x2="131" y2="114" stroke="#888780" stroke-width="1.2"/>
  <text x="131" y="68" text-anchor="middle" font-size="9" fill="#888780" font-family="sans-serif">LE MAC</text>
  <text x="131" y="80" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.7275 ft</text>
  <line x1="408" y1="58" x2="408" y2="114" stroke="#378ADD" stroke-width="1.8"/>
  <text x="408" y="42" text-anchor="middle" font-size="10" font-weight="bold" fill="#378ADD" font-family="sans-serif">fwd limit</text>
  <text x="408" y="55" text-anchor="middle" font-size="8.5" fill="#378ADD" font-family="sans-serif">0.91 ft · 26.5%</text>
  <line x1="423" y1="122" x2="423" y2="126" stroke="#0e6b3d" stroke-width="2.4"/>
  <text x="423" y="130" text-anchor="middle" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">nominal ✓</text>
  <text x="423" y="142" text-anchor="middle" font-size="8.5" fill="#0e6b3d" font-family="sans-serif">0.92 ft · 27.9%</text>
  <line x1="483" y1="82" x2="483" y2="114" stroke="#BA7517" stroke-width="2.0"/>
  <text x="483" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="#BA7517" font-family="sans-serif">aft limit</text>
  <text x="483" y="80" text-anchor="middle" font-size="8.5" fill="#BA7517" font-family="sans-serif">0.96 ft · 33.7%</text>
  <line x1="549" y1="122" x2="549" y2="126" stroke="#888780" stroke-width="1.0"/>
  <text x="549" y="130" text-anchor="middle" font-size="9" fill="#888780" font-family="sans-serif">NP est.</text>
  <text x="549" y="142" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">~40% MAC</text></svg>

| Titik CG | Nilai | % MAC | Dari LE MAC | Static Margin | Status |
|---|---|---|---|---|---|
| LE MAC (ref) | 0.7275 ft | 0% | 0 cm | — | — |
| **CG fwd** | **0.91 ft** | **26.5%** | **5.56 cm** | 13.6% | AMAN |
| **CG nominal ✓** | **0.92 ft** | **27.9%** | **5.87 cm** | 12.1% | **AMAN** |
| CG aft limit | 0.96 ft | 33.7% | 7.09 cm | 6.3% | AMAN |
| NP (estimasi) | ~1.0035 ft | ~40% | ~8.41 cm | — | ref |

### Payload Breakdown

| Komponen | Berat | Sisa |
|---|---|---|
| Empty weight | 1.361 kg | 1.021 kg |
| + Baterai 4S 6000 mAh | +350 g | **671 g** |
| **+ Baterai 4S 8000 mAh** | **+450 g** | **571 g** |

---

## 3. Geometri Sayap

### Wing 1

| Parameter | Imperial | Metrik |
|---|---|---|
| **Semi-length** | **2.13 ft** | **64.92 cm** |
| **Wingspan** | **4.26 ft** | **129.84 cm** |
| **Root chord** | **0.78 ft** | **23.77 cm** |
| **Tip chord** | **0.60 ft** | **18.29 cm** |
| Taper ratio | — | 0.7692 |
| Sweep | 0.0° | — |
| Dihedral | 0.0° | — |
| **MAC** | **0.6900 ft** | **21.03 cm** |
| **Wing area** | **2.939 ft²** | **0.2731 m²** |
| **Aspect ratio** | — | **6.1739** |
| Long arm (aero ref) | 0.90 ft | 27.43 cm |
| Lat arm | 0.19 ft | 5.79 cm |
| Vert arm | 0.25 ft | 7.62 cm |
| Aileron | element 4–8 (outboard ~50% span) | — |

### Wing 2 — Winglet / Strake

| Parameter | Nilai |
|---|---|
| Semi-length | 0.43 ft (13.1 cm) |
| Root chord | 0.60 ft (18.3 cm) |
| Tip chord | 0.08 ft (2.4 cm) |
| Sweep / Dihedral | 80° / 20° |
| Lat arm | 2.13 ft (= Wing 1 semi) |

### Vertical Stabilizer — V-tail (×2)

| Parameter | Nilai |
|---|---|
| Height | 0.65 ft (19.8 cm) |
| Root / Tip chord | 0.56 ft / 0.25 ft |
| Sweep / Dihedral | 40° / 45° |
| Long arm | 2.00 ft (60.96 cm) |
| Elevator + Rudder | aktif el 2–6 → ruddervator |

---

## 4. Titik Seimbang

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 860 530"><rect width="860" height="530" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="430" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#444441" font-family="sans-serif">Titik Seimbang — Satria Talon</text><text x="430" y="36" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">Semi 2.13 ft · Wingspan 129.8 cm · NACA 2412 · root 23.8cm · tip 18.3cm · sweep 0°</text>  <polygon points="320.0,152.0 323.6,152.0 327.1,152.0 330.7,152.0 334.3,152.0 337.9,152.0 341.4,152.0 345.0,152.0 348.6,152.0 352.1,152.0 355.7,152.0 359.3,152.0 362.8,152.0 366.4,152.0 370.0,152.0 373.6,152.0 377.1,152.0 380.7,152.0 384.3,152.0 387.8,152.0 391.4,152.0 395.0,152.0 398.6,152.0 402.1,152.0 405.7,152.0 409.3,152.0 412.8,152.0 416.4,152.0 420.0,152.0 423.6,152.0 427.1,152.0 430.7,152.0 434.3,152.0 437.8,152.0 441.4,152.0 445.0,152.0 448.5,152.0 452.1,152.0 455.7,152.0 459.3,152.0 462.8,152.0 466.4,152.0 470.0,152.0 473.5,152.0 477.1,152.0 480.7,152.0 484.3,152.0 487.8,152.0 491.4,152.0 495.0,152.0 498.5,152.0 502.1,152.0 505.7,152.0 509.2,152.0 512.8,152.0 516.4,152.0 520.0,152.0 523.5,152.0 527.1,152.0 530.7,152.0 534.2,152.0 534.2,212.4 530.7,212.7 527.1,213.0 523.5,213.3 520.0,213.6 516.4,213.9 512.8,214.2 509.2,214.5 505.7,214.8 502.1,215.1 498.5,215.4 495.0,215.7 491.4,216.0 487.8,216.3 484.3,216.6 480.7,216.9 477.1,217.2 473.5,217.5 470.0,217.8 466.4,218.1 462.8,218.4 459.3,218.7 455.7,219.0 452.1,219.3 448.5,219.6 445.0,219.9 441.4,220.2 437.8,220.5 434.3,220.8 430.7,221.1 427.1,221.4 423.6,221.7 420.0,222.0 416.4,222.3 412.8,222.6 409.3,222.9 405.7,223.2 402.1,223.5 398.6,223.8 395.0,224.1 391.4,224.4 387.8,224.7 384.3,225.0 380.7,225.3 377.1,225.6 373.6,225.9 370.0,226.2 366.4,226.5 362.8,226.8 359.3,227.1 355.7,227.4 352.1,227.7 348.6,228.0 345.0,228.3 341.4,228.6 337.9,228.9 334.3,229.2 330.7,229.6 327.1,229.9 323.6,230.2 320.0,230.5" fill="#b8cce0" stroke="#1a4a7a" stroke-width="1.5" opacity="0.85"/>
  <polygon points="320.0,152.0 316.4,152.0 312.9,152.0 309.3,152.0 305.7,152.0 302.1,152.0 298.6,152.0 295.0,152.0 291.4,152.0 287.9,152.0 284.3,152.0 280.7,152.0 277.2,152.0 273.6,152.0 270.0,152.0 266.4,152.0 262.9,152.0 259.3,152.0 255.7,152.0 252.2,152.0 248.6,152.0 245.0,152.0 241.4,152.0 237.9,152.0 234.3,152.0 230.7,152.0 227.2,152.0 223.6,152.0 220.0,152.0 216.4,152.0 212.9,152.0 209.3,152.0 205.7,152.0 202.2,152.0 198.6,152.0 195.0,152.0 191.5,152.0 187.9,152.0 184.3,152.0 180.7,152.0 177.2,152.0 173.6,152.0 170.0,152.0 166.5,152.0 162.9,152.0 159.3,152.0 155.7,152.0 152.2,152.0 148.6,152.0 145.0,152.0 141.5,152.0 137.9,152.0 134.3,152.0 130.8,152.0 127.2,152.0 123.6,152.0 120.0,152.0 116.5,152.0 112.9,152.0 109.3,152.0 105.8,152.0 105.8,212.4 109.3,212.7 112.9,213.0 116.5,213.3 120.0,213.6 123.6,213.9 127.2,214.2 130.8,214.5 134.3,214.8 137.9,215.1 141.5,215.4 145.0,215.7 148.6,216.0 152.2,216.3 155.7,216.6 159.3,216.9 162.9,217.2 166.5,217.5 170.0,217.8 173.6,218.1 177.2,218.4 180.7,218.7 184.3,219.0 187.9,219.3 191.5,219.6 195.0,219.9 198.6,220.2 202.2,220.5 205.7,220.8 209.3,221.1 212.9,221.4 216.4,221.7 220.0,222.0 223.6,222.3 227.2,222.6 230.7,222.9 234.3,223.2 237.9,223.5 241.4,223.8 245.0,224.1 248.6,224.4 252.2,224.7 255.7,225.0 259.3,225.3 262.9,225.6 266.4,225.9 270.0,226.2 273.6,226.5 277.2,226.8 280.7,227.1 284.3,227.4 287.9,227.7 291.4,228.0 295.0,228.3 298.6,228.6 302.1,228.9 305.7,229.2 309.3,229.6 312.9,229.9 316.4,230.2 320.0,230.5" fill="#b8cce0" stroke="#1a4a7a" stroke-width="1.5" opacity="0.85"/>
  <rect x="306" y="157.9" width="28" height="66.7" fill="#c8b888" stroke="#8a7050" stroke-width="1" rx="5" opacity="0.9"/>
  <line x1="320" y1="124" x2="320" y2="242.45551999999998" stroke="#888780" stroke-width="0.6" stroke-dasharray="5,4" opacity="0.4"/>
  <line x1="422.5" y1="152" x2="422.5" y2="221.8" stroke="#1D9E75" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="217.5" y1="152" x2="217.5" y2="221.8" stroke="#1D9E75" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="105.8" y1="170.5" x2="534.2" y2="170.5" stroke="#378ADD" stroke-width="0.9" stroke-dasharray="6,3" opacity="0.55"/>
  <line x1="105.8" y1="171.5" x2="534.2" y2="171.5" stroke="#0e6b3d" stroke-width="1.1" stroke-dasharray="6,3" opacity="0.65"/>
  <circle cx="397.1" cy="170.4" r="7" fill="#ffffff" stroke="#378ADD" stroke-width="2.5"/>
  <circle cx="397.1" cy="170.4" r="2.5" fill="#378ADD"/>
  <circle cx="242.9" cy="170.4" r="7" fill="#ffffff" stroke="#378ADD" stroke-width="2.5"/>
  <circle cx="242.9" cy="170.4" r="2.5" fill="#378ADD"/>
  <circle cx="435.7" cy="171.4" r="8" fill="#ffffff" stroke="#0e6b3d" stroke-width="2.5"/>
  <circle cx="435.7" cy="171.4" r="2.5" fill="#0e6b3d"/>
  <circle cx="204.3" cy="171.4" r="8" fill="#ffffff" stroke="#0e6b3d" stroke-width="2.5"/>
  <circle cx="204.3" cy="171.4" r="2.5" fill="#0e6b3d"/>
  <line x1="397.1" y1="170.4" x2="397.1" y2="132" stroke="#378ADD" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="397.1" y="116" text-anchor="middle" font-size="10" font-weight="bold" fill="#378ADD" font-family="sans-serif">CG fwd (first flight)</text>
  <text x="397.1" y="129" text-anchor="middle" font-size="8.5" fill="#378ADD" font-family="sans-serif">5.56 cm dari LE · 26.5% MAC</text>
  <line x1="435.7" y1="171.4" x2="540.24392" y2="240.6787552" stroke="#0e6b3d" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="544.24392" y="240.6787552" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">CG nominal ✓</text>
  <text x="544.24392" y="253.6787552" font-size="8.5" fill="#0e6b3d" font-family="sans-serif">5.87 cm dari LE · 27.9% MAC</text>
  <text x="412.5" y="182.9" text-anchor="end" font-size="9" fill="#1D9E75" font-family="sans-serif">MAC</text>
  <text x="412.5" y="194.9" text-anchor="end" font-size="8" fill="#1D9E75" font-family="sans-serif">21.0cm</text>
  <line x1="183.53551652173914" y1="152" x2="183.53551652173914" y2="171.5" stroke="#0e6b3d" stroke-width="0.9"/>
  <line x1="179.53551652173914" y1="152" x2="187.53551652173914" y2="152" stroke="#0e6b3d" stroke-width="0.9"/>
  <line x1="179.53551652173914" y1="171.5" x2="187.53551652173914" y2="171.5" stroke="#0e6b3d" stroke-width="0.9"/>
  <text x="177.53551652173914" y="165.7" text-anchor="end" font-size="9" fill="#0e6b3d" font-family="sans-serif">5.87cm</text>
  <text x="229.9" y="158.4" text-anchor="middle" font-size="9" fill="#378ADD" font-family="sans-serif">fwd</text>
  <text x="191.3" y="193.4" text-anchor="middle" font-size="9" fill="#0e6b3d" font-family="sans-serif">nom</text>
  <line x1="105.8" y1="104" x2="534.2" y2="104" stroke="#888780" stroke-width="0.8"/>
  <line x1="105.8" y1="99" x2="105.8" y2="109" stroke="#888780" stroke-width="0.8"/>
  <line x1="534.2" y1="99" x2="534.2" y2="109" stroke="#888780" stroke-width="0.8"/>
  <text x="320" y="96" text-anchor="middle" font-size="11" fill="#888780" font-family="sans-serif">← wingspan 129.8 cm →</text>
  <line x1="67.75608000000003" y1="152" x2="67.75608000000003" y2="230.5" stroke="#888780" stroke-width="0.8"/>
  <line x1="63.756080000000026" y1="152" x2="71.75608000000003" y2="152" stroke="#888780" stroke-width="0.8"/>
  <line x1="63.756080000000026" y1="230.5" x2="71.75608000000003" y2="230.5" stroke="#888780" stroke-width="0.8"/>
  <text x="61.756080000000026" y="195.2" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">root 23.8cm</text>
  <line x1="542.24392" y1="152" x2="542.24392" y2="212.4" stroke="#888780" stroke-width="0.8"/>
  <line x1="538.24392" y1="152" x2="546.24392" y2="152" stroke="#888780" stroke-width="0.8"/>
  <line x1="538.24392" y1="212.4" x2="546.24392" y2="212.4" stroke="#888780" stroke-width="0.8"/>
  <text x="548.24392" y="186.2" font-size="9" fill="#888780" font-family="sans-serif">tip 18.3cm</text>
  <line x1="320" y1="245.7965495652174" x2="422.5" y2="245.7965495652174" stroke="#1D9E75" stroke-width="0.8"/>
  <line x1="320" y1="241.7965495652174" x2="320" y2="249.7965495652174" stroke="#1D9E75" stroke-width="0.8"/>
  <line x1="422.5" y1="241.7965495652174" x2="422.5" y2="249.7965495652174" stroke="#1D9E75" stroke-width="0.8"/>
  <text x="371.2" y="258.7965495652174" text-anchor="middle" font-size="9" fill="#1D9E75" font-family="sans-serif">MAC station: 31.0 cm dari CL</text>
  <text x="300" y="147" text-anchor="end" font-size="9" fill="#1a4a7a" opacity="0.7" font-family="sans-serif">LE</text>
  <text x="300" y="244.5" text-anchor="end" font-size="9" fill="#1a4a7a" opacity="0.7" font-family="sans-serif">TE</text>
  <rect x="28" y="279.7965495652174" width="800" height="90" fill="#e6f4ee" rx="6" stroke="#0e6b3d" stroke-width="0.8"/>
  <text x="44" y="295.7965495652174" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">Cara menyeimbangkan:</text>
  <text x="44" y="309.7965495652174" font-size="9" fill="#444441" font-family="sans-serif">1. Tandai 31.0 cm dari CL di kanan dan kiri → posisi MAC station</text>
  <text x="44" y="323.7965495652174" font-size="9" fill="#444441" font-family="sans-serif">2. Ukur 5.87 cm dari LE di titik tersebut → CG nominal ✓</text>
  <text x="44" y="337.7965495652174" font-size="9" fill="#444441" font-family="sans-serif">3. Tumpukan UAV lengkap di 2 jari simetris pada kedua titik</text>
  <text x="44" y="351.7965495652174" font-size="9" fill="#444441" font-family="sans-serif">4. Hidung turun ringan = CG benar ✓   |   Ekor turun = geser baterai ke depan</text>
  <line x1="498" y1="287.7965495652174" x2="498" y2="363.7965495652174" stroke="#0e6b3d" stroke-width="0.5" opacity="0.4"/>
  <text x="510" y="295.7965495652174" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">Referensi dari LE:</text>
  <circle cx="515" cy="308.7965495652174" r="5" fill="#ffffff" stroke="#378ADD" stroke-width="2"/><circle cx="515" cy="308.7965495652174" r="2" fill="#378ADD"/>
  <text x="526" y="311.7965495652174" font-size="9" fill="#378ADD" font-weight="bold" font-family="sans-serif">CG fwd:</text>
  <text x="526" y="321.7965495652174" font-size="8.5" fill="#444441" font-family="sans-serif">5.56 cm  (26.5% MAC)</text>
  <circle cx="515" cy="326.7965495652174" r="5" fill="#ffffff" stroke="#0e6b3d" stroke-width="2"/><circle cx="515" cy="326.7965495652174" r="2" fill="#0e6b3d"/>
  <text x="526" y="329.7965495652174" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">CG nominal ✓:</text>
  <text x="526" y="339.7965495652174" font-size="8.5" fill="#444441" font-family="sans-serif">5.87 cm  (27.9% MAC)</text>
  <circle cx="515" cy="344.7965495652174" r="5" fill="#ffffff" stroke="#BA7517" stroke-width="2"/><circle cx="515" cy="344.7965495652174" r="2" fill="#BA7517"/>
  <text x="526" y="347.7965495652174" font-size="9" fill="#BA7517" font-weight="bold" font-family="sans-serif">CG aft (maks):</text>
  <text x="526" y="357.7965495652174" font-size="8.5" fill="#444441" font-family="sans-serif">7.09 cm  (33.7% MAC)</text></svg>

### Cara Mengukur

1. Tandai **31.0 cm dari CL** di kanan dan kiri → posisi MAC station
2. Di titik tersebut, ukur dari **LE (tepi depan sayap)**:
   - **5.56 cm** → CG fwd (first flight)
   - **5.87 cm** → CG nominal ✓
   - **7.09 cm** → batas maksimum
3. Tumpukan UAV di 2 jari simetris → hidung turun ringan = benar ✓

---

## 5. Performa Aerodinamis

| Parameter | Nilai |
|---|---|
| Wing loading | **85.5 N/m²** |
| **Stall speed Vs** | **9.649 m/s (34.7 km/h)** |
| Min safe airspeed | 11.58 m/s (41.7 km/h) |
| **Cruise speed** | **14.738 m/s (53.1 km/h)** |
| AoA cruise | 3.76° |
| VNE | 33.77 m/s (121.6 km/h) |
| **L/D max** | **12.366** |
| Cruise power | 45.9 W (0.0616 HP) |
| Peak power | 174 W (0.234 HP) |
| Motor rating min | 209 W (0.280 HP) |

### Mode High Speed

| Parameter | 80 km/h | 100 km/h |
|---|---|---|
| Kecepatan | 22.2 m/s | **27.8 m/s** |
| L/D | 9.12 | 6.44 |
| Cruise power | 94.0 W (0.126 HP) | **153 W (0.205 HP)** |
| Peak power | 117.5 W (0.158 HP) | 191 W (0.256 HP) |

### Mode High Speed — Opsi 3S (Standar)

Motor 2216 1000 KV @3S sudah cukup untuk HS 80 dan 100 km/h — satu motor untuk semua mode.

| Parameter | 80 km/h | 100 km/h |
|---|---|---|
| KV dibutuhkan @3S | **~1000 KV** | **~1000 KV** |
| Motor 1000 KV @3S | **✓ cukup** | **✓ cukup** |
| Propeller | APC 8×7 | **APC 9×8** |
| Baterai | **3S 10000 mAh** | 3S 10000 mAh |
| ESC | 40 A ✓ | 40 A ✓ |
| Current @3S | ~8.5 A | ~13.8 A |

---

## 6. Analisis Wingspan

### Endurance
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 280"><rect width="600" height="280" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Endurance vs Wingspan — 4S 8000 mAh</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft · root 23.8cm · tip 18.3cm</text><line x1="115" y1="44" x2="115" y2="262" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="37" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="61" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="157" y="61" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">83 mnt</text>
  <rect x="115" y="72" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="74" width="71" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="88" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="191" y="88" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">95 mnt</text>
  <rect x="115" y="99" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="101" width="106" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="115" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="226" y="115" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">107 mnt</text>
  <rect x="115" y="126" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="128" width="140" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="142" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="260" y="142" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">119 mnt</text>
  <rect x="115" y="153" width="330" height="25" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="155" width="177" height="21" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="169" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="297" y="169" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">132 mnt ← 130 cm ★</text>
  <rect x="115" y="180" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="182" width="212" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="196" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="332" y="196" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">144 mnt</text>
  <rect x="115" y="207" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="209" width="249" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="223" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="369" y="223" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">157 mnt</text>
  <rect x="115" y="234" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="236" width="289" height="21" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="250" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="409" y="250" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">171 mnt</text></svg>

### Wing Loading
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 280"><rect width="600" height="280" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Wing Loading vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft · root 23.8cm · tip 18.3cm</text><line x1="115" y1="44" x2="115" y2="262" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="264" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="61" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="384" y="61" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">123 N/m²</text>
  <rect x="115" y="72" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="74" width="217" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="88" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="337" y="88" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">111 N/m²</text>
  <rect x="115" y="99" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="101" width="178" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="115" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="298" y="115" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">101 N/m²</text>
  <rect x="115" y="126" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="128" width="147" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="142" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="267" y="142" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">93 N/m²</text>
  <rect x="115" y="153" width="330" height="25" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="155" width="116" height="21" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="169" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="236" y="169" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">85 N/m² ← 130 cm ★</text>
  <rect x="115" y="180" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="182" width="93" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="196" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="213" y="196" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">79 N/m²</text>
  <rect x="115" y="207" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="209" width="73" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="223" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="193" y="223" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">74 N/m²</text>
  <rect x="115" y="234" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="236" width="54" height="21" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="250" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="174" y="250" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">69 N/m²</text></svg>

### Kecepatan
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Kecepatan vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft</text>  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">21</text>
  <line x1="44" y1="89" x2="584" y2="89" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="93" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">18</text>
  <line x1="44" y1="135" x2="584" y2="135" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="139" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">14</text>
  <line x1="44" y1="180" x2="584" y2="180" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="184" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">11</text>
  <line x1="44" y1="226" x2="584" y2="226" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="230" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">8</text>
  <text x="44" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="121" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <text x="198" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">110</text>
  <text x="275" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">120</text>
  <text x="352" y="239" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130</text>
  <text x="429" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">140</text>
  <text x="506" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">150</text>
  <text x="584" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">160</text>
  <rect x="350" y="44" width="4" height="182" fill="#0e6b3d" opacity="0.12"/>
  <polyline points="44,70 121,90 198,106 275,121 352,133 429,143 506,153 584,161" fill="none" stroke="#534AB7" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="70" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="90" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="106" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="121" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="133" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="143" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="153" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="161" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,174 121,182 198,189 275,195 352,201 429,205 506,209 584,213" fill="none" stroke="#D85A30" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="174" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="182" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="189" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="195" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="201" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="205" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="209" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="213" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <line x1="352" y1="44" x2="352" y2="226" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="352" y="252" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">130 cm</text>
  <text x="44" y="265" font-size="9" fill="#534AB7" font-family="sans-serif">—— Vcruise m/s</text>
  <text x="150.5" y="265" font-size="9" fill="#D85A30" font-family="sans-serif">- -  Vstall m/s</text></svg>

### Aspect Ratio & L/D
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Aspect Ratio &amp; L/D max vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft</text>  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">15</text>
  <line x1="44" y1="89" x2="584" y2="89" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="93" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">12</text>
  <line x1="44" y1="135" x2="584" y2="135" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="139" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">9</text>
  <line x1="44" y1="180" x2="584" y2="180" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="184" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">7</text>
  <line x1="44" y1="226" x2="584" y2="226" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="230" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">4</text>
  <text x="44" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="121" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <text x="198" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">110</text>
  <text x="275" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">120</text>
  <text x="352" y="239" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130</text>
  <text x="429" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">140</text>
  <text x="506" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">150</text>
  <text x="584" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">160</text>
  <rect x="350" y="44" width="4" height="182" fill="#0e6b3d" opacity="0.12"/>
  <polyline points="44,218 121,210 198,204 275,196 352,188 429,179 506,173 584,165" fill="none" stroke="#0e6b3d" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="218" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="210" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="204" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="196" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="188" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="179" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="173" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="165" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,121 121,112 198,104 275,96 352,88 429,81 506,73 584,67" fill="none" stroke="#BA7517" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="121" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="112" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="104" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="96" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="88" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="81" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="73" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="67" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <line x1="352" y1="44" x2="352" y2="226" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="352" y="252" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">130 cm</text>
  <text x="44" y="265" font-size="9" fill="#0e6b3d" font-family="sans-serif">—— Aspect Ratio</text>
  <text x="156.0" y="265" font-size="9" fill="#BA7517" font-family="sans-serif">- -  L/D max</text></svg>

### Cruise Power
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 280"><rect width="600" height="280" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Cruise Power vs Wingspan (W)</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 5.25 lb · semi 2.13 ft · root 23.8cm · tip 18.3cm</text><line x1="115" y1="44" x2="115" y2="262" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="264" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="61" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="384" y="61" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">73 W</text>
  <rect x="115" y="72" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="74" width="214" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="88" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="334" y="88" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">64 W</text>
  <rect x="115" y="99" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="101" width="176" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="115" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">110 cm</text>
  <text x="296" y="115" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">57 W</text>
  <rect x="115" y="126" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="128" width="143" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="142" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">120 cm</text>
  <text x="263" y="142" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">51 W</text>
  <rect x="115" y="153" width="330" height="25" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="155" width="115" height="21" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="169" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">130 cm</text>
  <text x="235" y="169" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">46 W ← 130 cm ★</text>
  <rect x="115" y="180" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="182" width="93" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="196" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">140 cm</text>
  <text x="213" y="196" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">42 W</text>
  <rect x="115" y="207" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="209" width="71" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="223" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">150 cm</text>
  <text x="191" y="223" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">38 W</text>
  <rect x="115" y="234" width="330" height="25" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="236" width="55" height="21" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="250" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">160 cm</text>
  <text x="175" y="250" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">35 W</text></svg>

### Tabel

| Wingspan | Area | AR | WL | Vs | Vcruise | L/D | P cruise | Endurance (4S 8Ah) |
|---|---|---|---|---|---|---|---|---|
| 90 cm | 0.189 m² | 4.3 | 123 N/m² | 11.6 m/s | 19.4 m/s | 10.3 | 73 W | 83 mnt |
| 100 cm | 0.210 m² | 4.8 | 111 N/m² | 11.0 m/s | 17.9 m/s | 10.9 | 64 W | 95 mnt |
| 110 cm | 0.232 m² | 5.2 | 101 N/m² | 10.5 m/s | 16.7 m/s | 11.4 | 57 W | 107 mnt |
| 120 cm | 0.253 m² | 5.7 | 93 N/m² | 10.0 m/s | 15.6 m/s | 11.9 | 51 W | 119 mnt |
| **130 cm ★** | **0.2731 m²** | **6.17** | **86 N/m²** | **9.65 m/s** | **14.74 m/s** | **12.37** | **46 W** | **131 mnt** |
| 140 cm | 0.295 m² | 6.7 | 79 N/m² | 9.3 m/s | 13.9 m/s | 12.8 | 42 W | 144 mnt |
| 150 cm | 0.316 m² | 7.1 | 74 N/m² | 9.0 m/s | 13.2 m/s | 13.3 | 38 W | 157 mnt |
| 160 cm | 0.337 m² | 7.6 | 69 N/m² | 8.7 m/s | 12.6 m/s | 13.7 | 35 W | 171 mnt |

---

## 7. Propulsi

### Power Budget
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 650 210"><rect width="650" height="210" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="325" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Power Budget — Satria Talon</text><text x="325" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">MTOW 5.25 lb · semi 2.13 ft · sys eff 60.6%</text>  <rect x="200" y="52" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="200" y="52" width="82" height="26" fill="#1D9E75" rx="3" opacity="0.88"/>
  <text x="196" y="69" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Cruise (14.7 m/s)</text>
  <text x="287" y="69" font-size="10" fill="#1D9E75" font-weight="bold" font-family="sans-serif">46 W = 0.062 HP</text>
  <rect x="200" y="90" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="200" y="90" width="249" height="26" fill="#BA7517" rx="3" opacity="0.88"/>
  <text x="196" y="107" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Climb 4m/s (139 W)</text>
  <text x="454" y="107" font-size="10" fill="#BA7517" font-weight="bold" font-family="sans-serif">139 W = 0.186 HP</text>
  <rect x="200" y="128" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="200" y="128" width="311" height="26" fill="#D85A30" rx="3" opacity="0.88"/>
  <text x="196" y="145" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Peak ×1.25 (174 W)</text>
  <text x="516" y="145" font-size="10" fill="#D85A30" font-weight="bold" font-family="sans-serif">174 W = 0.233 HP</text>
  <rect x="200" y="166" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="200" y="166" width="430" height="26" fill="#D85A30" rx="3" opacity="0.88"/>
  <text x="196" y="183" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Motor rating min (250 W)</text>
  <text x="625" y="183" text-anchor="end" font-size="10" fill="#ffffff" font-weight="bold" font-family="sans-serif">250 W = 0.335 HP</text></svg>

### Propeller
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 190"><rect width="720" height="190" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Static Thrust vs Propeller — @ Peak 174 W</text><text x="360" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">2216 1000KV @3S · Vcruise 14.7 m/s · MTOW 2.381 kg</text>  <rect x="90" y="52" width="620" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="52" width="200" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="70" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">8×5.0</text>
  <text x="295" y="70" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">6.5 N · T/W 0.28 · RPM 11000 · KV@3S 990</text>
  <rect x="90" y="96" width="620" height="28" fill="#e6f4ee" rx="3"/>
  <rect x="90" y="96" width="260" height="28" fill="#0e6b3d" rx="3" opacity="0.88"/>
  <text x="86" y="114" text-anchor="end" font-size="12" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">9×5  ★</text>
  <text x="355" y="114" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">8.5 N · T/W 0.36 · RPM 9500 · KV@3S 855</text>
  <rect x="90" y="140" width="620" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="140" width="315" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="158" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">10×5.5</text>
  <text x="410" y="158" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">10.5 N · T/W 0.45 · RPM 8000 · KV@3S 720</text></svg>

| Parameter | Nilai |
|---|---|
| Motor | **2216, KV 1000 @ 3S** |
| Power rating | ≥ 250 W |
| **Propeller** | **APC 9×5** |
| ESC | **40 A BLHeli_32** |
| **Baterai** | **3S 10000 mAh** |

| Baterai | Endurance | Kargo | C-rate (cruise) | |
|---|---|---|---|---|
| 3S 5000 mAh | ~62 mnt | ~700 g | 0.83C | Cukup |
| 3S 8000 mAh | ~99 mnt | ~620 g | 0.52C | Baik |
| **3S 10000 mAh** | **~123 mnt** | **~541 g** | **0.41C** | **✓ Optimal** |
| 4S 8000 mAh | ~131 mnt | 571 g | 0.28C | Alternatif |

---

## 8. Misi & Jangkauan

| Konfigurasi | Kecepatan | Kargo | Endurance | Range one-way | Radius RTH |
|---|---|---|---|---|---|
| **3S 10000 mAh — cruise** | **53.1 km/h** | **~541 g** | **~123 mnt** | **~109 km** | **~44–47 km** |
| **3S 10000 mAh — HS 80** | **80 km/h** | **~541 g** | **~60 mnt** | **~80 km** | **~31–34 km** |
| **3S 10000 mAh — HS 100** | **100 km/h** | **~541 g** | **~37 mnt** | **~62 km** | **~23–25 km** |
| 4S 8000 mAh — cruise | 53.1 km/h | 571 g | ~131 mnt | ~116 km | ~49–52 km |
| 4S 8000 mAh — HS 80 | 80 km/h | 571 g | ~64 mnt | ~85 km | ~34–36 km |
| 4S 8000 mAh — HS 100 | 100 km/h | 571 g | ~39 mnt | ~65 km | ~25–27 km |

---

## 9. Rekomendasi Operasional

1. **CG fisik:** First flight di **5.56 cm dari LE** (26.5% MAC, 0.91 ft)
2. **CG nominal:** **5.87 cm dari LE** (27.9% MAC, 0.92 ft) setelah first flight validated
3. **Batas keras CG:** Jangan melebihi **7.09 cm dari LE** (33.7% MAC, 0.96 ft)
4. **V-tail mixing:** Konfigurasi ruddervator di ArduPlane/iNav, uji pitch/yaw di darat sebelum terbang
5. **Pitot tube:** Wajib — Vs 9.65 m/s, airspeed measurement kritis
6. **Baterai:** 3S 10000 mAh untuk endurance optimal; C-rate 0.41C sangat aman

---

## 10. Ringkasan Spesifikasi Final

| Parameter | Nilai |
|---|---|
| **Airfoil** | **NACA 2412** |
| **Semi-length** | **2.13 ft (64.92 cm)** |
| **Wingspan** | **129.84 cm** |
| **Root / Tip chord** | **23.77 cm / 18.29 cm** |
| Taper ratio | 0.7692 |
| Sweep | 0.0° |
| Wing area | 0.2731 m² |
| Aspect ratio | 6.1739 |
| MAC | 21.03 cm @ ±31.0 cm dari CL |
| Konfigurasi ekor | V-tail twin fin (45°) |
| **Empty weight** | **3.00 lb = 1.361 kg** |
| **MTOW** | **5.25 lb = 2.381 kg** |
| Payload total | 1.021 kg |
| **CG fwd** | **0.91 ft = 5.56 cm dari LE = 26.5% MAC** |
| **CG nominal ✓** | **0.92 ft = 5.87 cm dari LE = 27.9% MAC** |
| **CG aft limit** | **0.96 ft = 7.09 cm dari LE = 33.7% MAC** |
| Wing loading | 85.5 N/m² |
| **Stall speed** | **9.649 m/s (34.7 km/h)** |
| **Cruise speed** | **14.738 m/s (53.1 km/h)** |
| VNE | 33.77 m/s |
| L/D max | 12.366 |
| Cruise power | 45.9 W (0.0616 HP) |
| Peak power | 174 W (0.234 HP) |
| **Endurance cruise (3S 10Ah)** | **~123 mnt** |
| **Range one-way (cruise)** | **~109 km** |
| **Radius RTH (cruise)** | **~44–47 km** |
| Cruise power HS 80 | 94.0 W (0.126 HP) |
| **Endurance HS 80 (3S 10Ah)** | **~60 mnt** |
| **Range one-way HS 80** | **~80 km** |
| **Radius RTH HS 80** | **~31–34 km** |
| Cruise power HS 100 | 153 W (0.205 HP) |
| **Endurance HS 100 (3S 10Ah)** | **~37 mnt** |
| Range one-way HS 100 | ~62 km |
| Radius RTH HS 100 | ~23–25 km |
| Motor | **2216, KV 1000 @ 3S** |
| Propeller (cruise) | APC 9×5 |
| Propeller HS 80 | APC 8×7 |
| **Propeller HS 100** | **APC 9×8** |
| ESC | 40 A BLHeli_32 |
| **Baterai** | **3S 10000 mAh** |
| Baterai (4S opsi) | 4S 8000 mAh |

---

*UAV Satria Talon · NACA 2412 · Semi 2.13 ft · Root 0.78 ft · Tip 0.60 ft · Sweep 0° · V-tail*  
*Empty 3.00 lb · MTOW 5.25 lb · Seluruh nilai performa adalah estimasi teoritis.*
