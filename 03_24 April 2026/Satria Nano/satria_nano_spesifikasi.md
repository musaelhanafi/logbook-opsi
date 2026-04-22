# UAV Satria Nano — Spesifikasi Lengkap

![Satria Nano](Satria%20Nano.png)

> **Airfoil:** NACA 2412 · **Semi:** 1.52 ft · **Root:** 0.66 ft · **Tip:** 0.48 ft · **Sweep:** 0°  
> **Empty:** 2.20 lb (0.998 kg) · **MTOW:** 3.50 lb (1.588 kg) · **Wingspan:** 92.7 cm  
> **CG:** fwd 0.62 ft · nominal 0.63 ft · aft 0.65 ft

---

## Tentang LE dan MAC

**LE (Leading Edge)** = tepi depan sayap — titik referensi pengukuran CG secara fisik.

**MAC (Mean Aerodynamic Chord)** = chord rata-rata aerodinamis yang mewakili seluruh sayap. Untuk sayap taper, MAC ≠ root chord. Satria Nano:
- MAC berada di **21.9 cm dari CL** (kiri dan kanan), di **47.4% semi-span**
- Panjang MAC = **17.37 cm**
- Karena sweep **0°**, LE lurus sejajar — ukur langsung dari tepi depan sayap

**CG diukur sebagai jarak dari LE di posisi MAC ke belakang.**

---

## 1. Weight & Balance

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 745 320"><rect width="745" height="320" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="372" y="24" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Weight &amp; Balance — Satria Nano (Final)</text>  <text x="20" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Parameter</text>
  <text x="195" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Imperial</text>
  <text x="280" y="44" font-size="10" font-weight="bold" fill="#888780" font-family="sans-serif">Keterangan</text>
  <line x1="8" y1="48" x2="738" y2="48" stroke="#d4d2c8" stroke-width="0.8"/>
  <rect x="8" y="38" width="730" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="52" font-size="10" fill="#444441" font-family="sans-serif">Empty weight</text>
  <text x="195" y="52" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">2.20 lb</text>
  <text x="280" y="52" font-size="10" fill="#444441" font-family="sans-serif">0.998 kg</text>
  <rect x="8" y="66" width="730" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="80" font-size="10" fill="#444441" font-family="sans-serif">Maximum weight (MTOW)</text>
  <text x="195" y="80" font-size="10" fill="#444441" font-weight="bold" font-family="monospace">3.50 lb</text>
  <text x="280" y="80" font-size="10" fill="#444441" font-family="sans-serif">1.588 kg</text>
  <rect x="8" y="94" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="108" font-size="10" fill="#444441" font-family="sans-serif">Payload total</text>
  <text x="195" y="108" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">1.30 lb</text>
  <text x="280" y="108" font-size="10" fill="#0e6b3d" font-family="sans-serif">590 g</text>
  <rect x="8" y="122" width="730" height="24" fill="#ffffff" rx="2"/>
  <text x="20" y="136" font-size="10" fill="#444441" font-family="sans-serif">CG fwd limit</text>
  <text x="195" y="136" font-size="10" fill="#378ADD" font-weight="bold" font-family="monospace">0.62 ft</text>
  <text x="280" y="136" font-size="10" fill="#378ADD" font-family="sans-serif">28.5% MAC · 4.95 cm dari LE</text>
  <rect x="8" y="150" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="164" font-size="10" fill="#444441" font-family="sans-serif">CG nominal ✓</text>
  <text x="195" y="164" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">0.63 ft</text>
  <text x="280" y="164" font-size="10" fill="#0e6b3d" font-family="sans-serif">30.3% MAC · 5.26 cm dari LE</text>
  <rect x="8" y="178" width="730" height="24" fill="#fff8ee" rx="2"/>
  <text x="20" y="192" font-size="10" fill="#444441" font-family="sans-serif">CG aft limit</text>
  <text x="195" y="192" font-size="10" fill="#BA7517" font-weight="bold" font-family="monospace">0.65 ft</text>
  <text x="280" y="192" font-size="10" fill="#BA7517" font-family="sans-serif">33.8% MAC · 5.87 cm dari LE  (SM 6.2%)</text>
  <rect x="8" y="206" width="730" height="24" fill="#f5f5f5" rx="2"/>
  <text x="20" y="220" font-size="10" fill="#444441" font-family="sans-serif">Vert CG</text>
  <text x="195" y="220" font-size="10" fill="#888780" font-weight="bold" font-family="monospace">0.00 ft</text>
  <text x="280" y="220" font-size="10" fill="#888780" font-family="sans-serif">—</text>
  <rect x="8" y="234" width="730" height="24" fill="#e6f4ee" rx="2"/>
  <text x="20" y="248" font-size="10" fill="#444441" font-family="sans-serif">SM @ nominal</text>
  <text x="195" y="248" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="monospace">—</text>
  <text x="280" y="248" font-size="10" fill="#0e6b3d" font-family="sans-serif">~9.7% MAC (NP est. ~40%) — AMAN ✓</text>
  <rect x="8" y="262" width="730" height="24" fill="#fff8ee" rx="2"/>
  <text x="20" y="276" font-size="10" fill="#444441" font-family="sans-serif">SM @ aft limit</text>
  <text x="195" y="276" font-size="10" fill="#BA7517" font-weight="bold" font-family="monospace">—</text>
  <text x="280" y="276" font-size="10" fill="#BA7517" font-family="sans-serif">~6.2% MAC — AMAN</text></svg>

### CG Envelope

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 680 250"><rect width="680" height="250" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="340" y="19" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">CG Envelope — Satria Nano (Final)</text><text x="340" y="33" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · Semi 1.52 ft · root 0.66 ft · tip 0.48 ft · MAC 17.37 cm</text>  <rect x="411" y="96" width="39" height="44" fill="#e6f4ee" rx="3" opacity="0.8"/>
  <text x="430" y="123" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">safe zone</text>
  <line x1="50" y1="118" x2="630" y2="118" stroke="#d4d2c8" stroke-width="1.5"/>
  <text x="46" y="123" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">nose</text>
  <text x="634" y="123" text-anchor="start" font-size="9" fill="#888780" font-family="sans-serif">tail</text>
  <line x1="125" y1="114" x2="125" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="125" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.40</text>
  <line x1="190" y1="114" x2="190" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="190" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.45</text>
  <line x1="255" y1="114" x2="255" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="255" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.50</text>
  <line x1="320" y1="114" x2="320" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="320" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.55</text>
  <line x1="385" y1="114" x2="385" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="385" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.60</text>
  <line x1="450" y1="114" x2="450" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="450" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.65</text>
  <line x1="515" y1="114" x2="515" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="515" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.70</text>
  <line x1="580" y1="114" x2="580" y2="122" stroke="#888780" stroke-width="0.8"/>
  <text x="580" y="160" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.75</text>
  <defs><marker id="arr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="5" markerHeight="5" orient="auto"><path d="M1 2L9 5L1 8" fill="none" stroke="#0e6b3d" stroke-width="1.5" stroke-linejoin="round"/></marker></defs>
  <line x1="426" y1="178" x2="494" y2="178" stroke="#0e6b3d" stroke-width="1.2" stroke-dasharray="3,2" marker-end="url(#arr)"/>
  <text x="460" y="192" text-anchor="middle" font-size="9" fill="#0e6b3d" font-family="sans-serif">static margin ~9.7% MAC (nominal)</text>
  <line x1="199" y1="82" x2="199" y2="114" stroke="#888780" stroke-width="1.2"/>
  <text x="199" y="68" text-anchor="middle" font-size="9" fill="#888780" font-family="sans-serif">LE MAC</text>
  <text x="199" y="80" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">0.4575 ft</text>
  <line x1="411" y1="58" x2="411" y2="114" stroke="#378ADD" stroke-width="1.8"/>
  <text x="411" y="42" text-anchor="middle" font-size="10" font-weight="bold" fill="#378ADD" font-family="sans-serif">fwd limit</text>
  <text x="411" y="55" text-anchor="middle" font-size="8.5" fill="#378ADD" font-family="sans-serif">0.62 ft · 28.5%</text>
  <line x1="424" y1="122" x2="424" y2="126" stroke="#0e6b3d" stroke-width="2.4"/>
  <text x="424" y="130" text-anchor="middle" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">nominal ✓</text>
  <text x="424" y="142" text-anchor="middle" font-size="8.5" fill="#0e6b3d" font-family="sans-serif">0.63 ft · 30.3%</text>
  <line x1="450" y1="82" x2="450" y2="114" stroke="#BA7517" stroke-width="2.0"/>
  <text x="450" y="68" text-anchor="middle" font-size="10" font-weight="bold" fill="#BA7517" font-family="sans-serif">aft limit</text>
  <text x="450" y="80" text-anchor="middle" font-size="8.5" fill="#BA7517" font-family="sans-serif">0.65 ft · 33.8%</text>
  <line x1="496" y1="122" x2="496" y2="126" stroke="#888780" stroke-width="1.0"/>
  <text x="496" y="130" text-anchor="middle" font-size="9" fill="#888780" font-family="sans-serif">NP est.</text>
  <text x="496" y="142" text-anchor="middle" font-size="8" fill="#888780" font-family="sans-serif">~40% MAC</text></svg>

| Titik CG | Nilai | % MAC | Dari LE | Static Margin | Status |
|---|---|---|---|---|---|
| **CG fwd** | **0.62 ft** | **28.5%** | **4.95 cm** | 11.5% | AMAN |
| **CG nominal ✓** | **0.63 ft** | **30.3%** | **5.26 cm** | 9.7% | **AMAN** |
| CG aft limit | 0.65 ft | 33.8% | 5.87 cm | 6.2% | AMAN |
| NP (estimasi) | ~0.685 ft | ~40% | ~6.95 cm | — | ref |

### Payload Breakdown

| Komponen | Berat | Sisa |
|---|---|---|
| Empty weight | 0.998 kg | 590 g |
| + Baterai 4S 2200 mAh | +180 g | **410 g** |
| + Baterai 3S 3000 mAh | +200 g | **390 g** |

---

## 2. Geometri Sayap

### Wing 1

| Parameter | Imperial | Metrik |
|---|---|---|
| **Semi-length** | **1.52 ft** | **46.33 cm** |
| **Wingspan** | **3.04 ft** | **92.66 cm** |
| **Root chord** | **0.66 ft** | **20.12 cm** |
| **Tip chord** | **0.48 ft** | **14.63 cm** |
| Taper ratio | — | 0.7273 |
| Sweep | 0.0° | — |
| Dihedral | 0.0° | — |
| **MAC** | **0.5700 ft** | **17.37 cm** |
| **Wing area** | **1.733 ft²** | **0.1610 m²** |
| **Aspect ratio** | — | **5.3333** |
| Long arm (aero ref) | 0.60 ft | 18.29 cm |
| Lat arm | 0.20 ft | 6.10 cm |
| Vert arm | 0.18 ft | 5.49 cm |

### Wing 2 — Winglet

| Parameter | Nilai |
|---|---|
| Semi-length | 0.45 ft (13.72 cm) |
| Root chord | 0.48 ft (14.63 cm) |
| Tip chord | 0.008 ft (0.24 cm) |
| Sweep / Dihedral | 60° / 10° |
| **Lat arm** | **1.72 ft (52.43 cm)** |

### Vertical Stabilizer — V-tail (×2)

| Parameter | Nilai |
|---|---|
| Height | 0.55 ft (16.76 cm) |
| Root / Tip chord | 0.55 ft / 0.32 ft |
| Sweep / Dihedral | 45° / 45° |
| Long arm | 1.38 ft (42.06 cm) |

---

## 3. Titik Seimbang

<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 820 510"><rect width="820" height="510" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="410" y="22" text-anchor="middle" font-size="14" font-weight="bold" fill="#444441" font-family="sans-serif">Titik Seimbang — Satria Nano (Final)</text><text x="410" y="36" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">Semi 1.52 ft · Wingspan 92.7 cm · NACA 2412 · root 20.1cm · tip 14.6cm</text>  <polygon points="310.0,150.0 313.0,150.0 315.9,150.0 318.9,150.0 321.9,150.0 324.9,150.0 327.8,150.0 330.8,150.0 333.8,150.0 336.8,150.0 339.7,150.0 342.7,150.0 345.7,150.0 348.6,150.0 351.6,150.0 354.6,150.0 357.6,150.0 360.5,150.0 363.5,150.0 366.5,150.0 369.5,150.0 372.4,150.0 375.4,150.0 378.4,150.0 381.3,150.0 384.3,150.0 387.3,150.0 390.3,150.0 393.2,150.0 396.2,150.0 399.2,150.0 402.2,150.0 405.1,150.0 408.1,150.0 411.1,150.0 414.0,150.0 417.0,150.0 420.0,150.0 423.0,150.0 425.9,150.0 428.9,150.0 431.9,150.0 434.9,150.0 437.8,150.0 440.8,150.0 443.8,150.0 446.7,150.0 449.7,150.0 452.7,150.0 455.7,150.0 458.6,150.0 461.6,150.0 464.6,150.0 467.6,150.0 470.5,150.0 473.5,150.0 476.5,150.0 479.5,150.0 482.4,150.0 485.4,150.0 488.4,150.0 488.4,206.3 485.4,206.7 482.4,207.0 479.5,207.4 476.5,207.7 473.5,208.1 470.5,208.4 467.6,208.8 464.6,209.1 461.6,209.5 458.6,209.8 455.7,210.2 452.7,210.6 449.7,210.9 446.7,211.3 443.8,211.6 440.8,212.0 437.8,212.3 434.9,212.7 431.9,213.0 428.9,213.4 425.9,213.7 423.0,214.1 420.0,214.4 417.0,214.8 414.0,215.1 411.1,215.5 408.1,215.8 405.1,216.2 402.2,216.5 399.2,216.9 396.2,217.2 393.2,217.6 390.3,217.9 387.3,218.3 384.3,218.6 381.3,219.0 378.4,219.4 375.4,219.7 372.4,220.1 369.5,220.4 366.5,220.8 363.5,221.1 360.5,221.5 357.6,221.8 354.6,222.2 351.6,222.5 348.6,222.9 345.7,223.2 342.7,223.6 339.7,223.9 336.8,224.3 333.8,224.6 330.8,225.0 327.8,225.3 324.9,225.7 321.9,226.0 318.9,226.4 315.9,226.7 313.0,227.1 310.0,227.4" fill="#c8d8e8" stroke="#2a5a8a" stroke-width="1.5" opacity="0.85"/>
  <polygon points="310.0,150.0 307.0,150.0 304.1,150.0 301.1,150.0 298.1,150.0 295.1,150.0 292.2,150.0 289.2,150.0 286.2,150.0 283.2,150.0 280.3,150.0 277.3,150.0 274.3,150.0 271.4,150.0 268.4,150.0 265.4,150.0 262.4,150.0 259.5,150.0 256.5,150.0 253.5,150.0 250.5,150.0 247.6,150.0 244.6,150.0 241.6,150.0 238.7,150.0 235.7,150.0 232.7,150.0 229.7,150.0 226.8,150.0 223.8,150.0 220.8,150.0 217.8,150.0 214.9,150.0 211.9,150.0 208.9,150.0 206.0,150.0 203.0,150.0 200.0,150.0 197.0,150.0 194.1,150.0 191.1,150.0 188.1,150.0 185.1,150.0 182.2,150.0 179.2,150.0 176.2,150.0 173.3,150.0 170.3,150.0 167.3,150.0 164.3,150.0 161.4,150.0 158.4,150.0 155.4,150.0 152.4,150.0 149.5,150.0 146.5,150.0 143.5,150.0 140.5,150.0 137.6,150.0 134.6,150.0 131.6,150.0 131.6,206.3 134.6,206.7 137.6,207.0 140.5,207.4 143.5,207.7 146.5,208.1 149.5,208.4 152.4,208.8 155.4,209.1 158.4,209.5 161.4,209.8 164.3,210.2 167.3,210.6 170.3,210.9 173.3,211.3 176.2,211.6 179.2,212.0 182.2,212.3 185.1,212.7 188.1,213.0 191.1,213.4 194.1,213.7 197.0,214.1 200.0,214.4 203.0,214.8 206.0,215.1 208.9,215.5 211.9,215.8 214.9,216.2 217.8,216.5 220.8,216.9 223.8,217.2 226.8,217.6 229.7,217.9 232.7,218.3 235.7,218.6 238.7,219.0 241.6,219.4 244.6,219.7 247.6,220.1 250.5,220.4 253.5,220.8 256.5,221.1 259.5,221.5 262.4,221.8 265.4,222.2 268.4,222.5 271.4,222.9 274.3,223.2 277.3,223.6 280.3,223.9 283.2,224.3 286.2,224.6 289.2,225.0 292.2,225.3 295.1,225.7 298.1,226.0 301.1,226.4 304.1,226.7 307.0,227.1 310.0,227.4" fill="#c8d8e8" stroke="#2a5a8a" stroke-width="1.5" opacity="0.85"/>
  <rect x="297" y="155.8" width="26" height="65.8" fill="#d4c4a0" stroke="#8a7050" stroke-width="1" rx="5" opacity="0.9"/>
  <line x1="310" y1="124" x2="310" y2="237.44968" stroke="#888780" stroke-width="0.6" stroke-dasharray="5,4" opacity="0.4"/>
  <line x1="394.5" y1="150" x2="394.5" y2="217.4" stroke="#1D9E75" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="225.5" y1="150" x2="225.5" y2="217.4" stroke="#1D9E75" stroke-width="1.3" stroke-dasharray="4,3"/>
  <line x1="131.6" y1="169.2" x2="488.4" y2="169.2" stroke="#378ADD" stroke-width="0.9" stroke-dasharray="6,3" opacity="0.55"/>
  <line x1="131.6" y1="170.4" x2="488.4" y2="170.4" stroke="#0e6b3d" stroke-width="1.1" stroke-dasharray="6,3" opacity="0.65"/>
  <circle cx="374.2" cy="169.1" r="7" fill="#ffffff" stroke="#378ADD" stroke-width="2.5"/>
  <circle cx="374.2" cy="169.1" r="2.5" fill="#378ADD"/>
  <circle cx="245.8" cy="169.1" r="7" fill="#ffffff" stroke="#378ADD" stroke-width="2.5"/>
  <circle cx="245.8" cy="169.1" r="2.5" fill="#378ADD"/>
  <circle cx="406.3" cy="170.2" r="8" fill="#ffffff" stroke="#0e6b3d" stroke-width="2.5"/>
  <circle cx="406.3" cy="170.2" r="2.5" fill="#0e6b3d"/>
  <circle cx="213.7" cy="170.2" r="8" fill="#ffffff" stroke="#0e6b3d" stroke-width="2.5"/>
  <circle cx="213.7" cy="170.2" r="2.5" fill="#0e6b3d"/>
  <line x1="374.2" y1="169.1" x2="374.2" y2="132" stroke="#378ADD" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="374.2" y="118" text-anchor="middle" font-size="10" font-weight="bold" fill="#378ADD" font-family="sans-serif">CG fwd (first flight)</text>
  <text x="374.2" y="130" text-anchor="middle" font-size="8.5" fill="#378ADD" font-family="sans-serif">4.95 cm dari LE · 28.5% MAC</text>
  <line x1="406.3" y1="170.2" x2="494.36896" y2="234.0434544" stroke="#0e6b3d" stroke-width="0.8" stroke-dasharray="3,2"/>
  <text x="498.36896" y="234.0434544" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">CG nominal ✓</text>
  <text x="498.36896" y="247.0434544" font-size="8.5" fill="#0e6b3d" font-family="sans-serif">5.26 cm dari LE · 30.3% MAC</text>
  <text x="384.5" y="179.7" text-anchor="end" font-size="9" fill="#1D9E75" font-family="sans-serif">MAC</text>
  <text x="384.5" y="191.7" text-anchor="end" font-size="8" fill="#1D9E75" font-family="sans-serif">17.4cm</text>
  <line x1="195.50943999999998" y1="150" x2="195.50943999999998" y2="170.4" stroke="#0e6b3d" stroke-width="0.9"/>
  <line x1="191.50943999999998" y1="150" x2="199.50943999999998" y2="150" stroke="#0e6b3d" stroke-width="0.9"/>
  <line x1="191.50943999999998" y1="170.4" x2="199.50943999999998" y2="170.4" stroke="#0e6b3d" stroke-width="0.9"/>
  <text x="189.50943999999998" y="164.2" text-anchor="end" font-size="9" fill="#0e6b3d" font-family="sans-serif">5.26cm</text>
  <text x="233.8" y="157.1" text-anchor="middle" font-size="9" fill="#378ADD" font-family="sans-serif">fwd</text>
  <text x="201.7" y="192.2" text-anchor="middle" font-size="9" fill="#0e6b3d" font-family="sans-serif">nom</text>
  <line x1="131.6" y1="104" x2="488.4" y2="104" stroke="#888780" stroke-width="0.8"/>
  <line x1="131.6" y1="99" x2="131.6" y2="109" stroke="#888780" stroke-width="0.8"/>
  <line x1="488.4" y1="99" x2="488.4" y2="109" stroke="#888780" stroke-width="0.8"/>
  <text x="310" y="96" text-anchor="middle" font-size="11" fill="#888780" font-family="sans-serif">← wingspan 92.7 cm →</text>
  <line x1="95.63103999999998" y1="150" x2="95.63103999999998" y2="227.4" stroke="#888780" stroke-width="0.8"/>
  <line x1="91.63103999999998" y1="150" x2="99.63103999999998" y2="150" stroke="#888780" stroke-width="0.8"/>
  <line x1="91.63103999999998" y1="227.4" x2="99.63103999999998" y2="227.4" stroke="#888780" stroke-width="0.8"/>
  <text x="89.63103999999998" y="192.7" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">root 20.1cm</text>
  <line x1="496.36896" y1="150" x2="496.36896" y2="206.3" stroke="#888780" stroke-width="0.8"/>
  <line x1="492.36896" y1="150" x2="500.36896" y2="150" stroke="#888780" stroke-width="0.8"/>
  <line x1="492.36896" y1="206.3" x2="500.36896" y2="206.3" stroke="#888780" stroke-width="0.8"/>
  <text x="502.36896" y="182.2" font-size="9" fill="#888780" font-family="sans-serif">tip 14.6cm</text>
  <line x1="310" y1="239.44421894736843" x2="394.5" y2="239.44421894736843" stroke="#1D9E75" stroke-width="0.8"/>
  <line x1="310" y1="235.44421894736843" x2="310" y2="243.44421894736843" stroke="#1D9E75" stroke-width="0.8"/>
  <line x1="394.5" y1="235.44421894736843" x2="394.5" y2="243.44421894736843" stroke="#1D9E75" stroke-width="0.8"/>
  <text x="352.2" y="252.44421894736843" text-anchor="middle" font-size="9" fill="#1D9E75" font-family="sans-serif">MAC station: 21.9 cm dari CL</text>
  <text x="292" y="145" text-anchor="end" font-size="9" fill="#2a5a8a" opacity="0.7" font-family="sans-serif">LE</text>
  <text x="292" y="241.4" text-anchor="end" font-size="9" fill="#2a5a8a" opacity="0.7" font-family="sans-serif">TE</text>
  <rect x="28" y="271.4442189473684" width="762" height="90" fill="#e6f4ee" rx="6" stroke="#0e6b3d" stroke-width="0.8"/>
  <text x="44" y="287.4442189473684" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">Cara menyeimbangkan:</text>
  <text x="44" y="301.4442189473684" font-size="9" fill="#444441" font-family="sans-serif">1. Tandai 21.9 cm dari CL di kanan dan kiri → posisi MAC station</text>
  <text x="44" y="315.4442189473684" font-size="9" fill="#444441" font-family="sans-serif">2. Ukur 5.26 cm dari LE (tepi depan sayap) ke belakang → titik nominal ✓</text>
  <text x="44" y="329.4442189473684" font-size="9" fill="#444441" font-family="sans-serif">3. Tumpukan UAV lengkap di 2 jari secara simetris pada kedua titik</text>
  <text x="44" y="343.4442189473684" font-size="9" fill="#444441" font-family="sans-serif">4. Hidung turun ringan = CG benar ✓   |   Ekor turun = geser baterai ke depan</text>
  <line x1="488" y1="279.4442189473684" x2="488" y2="355.4442189473684" stroke="#0e6b3d" stroke-width="0.5" opacity="0.4"/>
  <text x="500" y="287.4442189473684" font-size="10" font-weight="bold" fill="#0e6b3d" font-family="sans-serif">Referensi jarak dari LE:</text>
  <circle cx="505" cy="300.4442189473684" r="5" fill="#ffffff" stroke="#378ADD" stroke-width="2"/><circle cx="505" cy="300.4442189473684" r="2" fill="#378ADD"/>
  <text x="516" y="303.4442189473684" font-size="9" fill="#378ADD" font-weight="bold" font-family="sans-serif">CG fwd:</text>
  <text x="516" y="313.4442189473684" font-size="8.5" fill="#444441" font-family="sans-serif">4.95 cm  (28.5% MAC)</text>
  <circle cx="505" cy="318.4442189473684" r="5" fill="#ffffff" stroke="#0e6b3d" stroke-width="2"/><circle cx="505" cy="318.4442189473684" r="2" fill="#0e6b3d"/>
  <text x="516" y="321.4442189473684" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">CG nominal ✓:</text>
  <text x="516" y="331.4442189473684" font-size="8.5" fill="#444441" font-family="sans-serif">5.26 cm  (30.3% MAC)</text>
  <circle cx="505" cy="336.4442189473684" r="5" fill="#ffffff" stroke="#BA7517" stroke-width="2"/><circle cx="505" cy="336.4442189473684" r="2" fill="#BA7517"/>
  <text x="516" y="339.4442189473684" font-size="9" fill="#BA7517" font-weight="bold" font-family="sans-serif">CG aft (maks):</text>
  <text x="516" y="349.4442189473684" font-size="8.5" fill="#444441" font-family="sans-serif">5.87 cm  (33.8% MAC)</text></svg>

### Cara Mengukur

1. Tandai **21.9 cm dari CL** di kanan dan kiri → posisi MAC station
2. Di titik tersebut, ukur dari **LE (tepi depan sayap)**:
   - **4.95 cm** → CG fwd (first flight)
   - **5.26 cm** → CG nominal ✓
   - **5.87 cm** → batas maksimum
3. Tumpukan UAV di 2 jari simetris → hidung turun ringan = benar ✓

---

## 4. Performa Aerodinamis

| Parameter | Nilai |
|---|---|
| Wing loading | **96.7 N/m²** |
| **Stall speed Vs** | **10.26 m/s (36.9 km/h)** |
| Min safe airspeed | 12.31 m/s (44.3 km/h) |
| **Cruise speed** | **16.26 m/s (58.5 km/h)** |
| AoA cruise | 3.35° |
| VNE | 35.92 m/s (129.3 km/h) |
| **L/D max** | **11.49** |
| Cruise power | 36.3 W (0.049 HP) |
| Peak power | 123 W (0.165 HP) |
| Motor rating min | 148 W (0.198 HP) |

### Mode High Speed

| Parameter | 80 km/h | 100 km/h |
|---|---|---|
| Kecepatan | 22.2 m/s | **27.8 m/s** |
| L/D | 9.57 | 7.05 |
| Cruise power | 59.7 W (0.080 HP) | **93 W (0.125 HP)** |
| Peak power | 74.6 W (0.100 HP) | 116 W (0.156 HP) |

### Mode High Speed — Opsi 3S (Utama)

Motor 2216 1000 KV @3S sudah cukup untuk HS 80 dan 100 km/h — satu motor untuk semua mode.

| Parameter | 80 km/h | 100 km/h |
|---|---|---|
| KV dibutuhkan @3S | **~950 KV** | **~1050 KV** |
| Motor 1000 KV @3S | **✓ cukup** | **✓ cukup** |
| Propeller | APC 8×6 | **APC 9×7** |
| Baterai | **3S 3000 mAh** | 3S 3000 mAh |
| ESC | 30 A ✓ | 30 A ✓ |
| Current @3S | ~5.4 A | ~8.4 A |

---

## 5. Analisis Wingspan

### Endurance
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Endurance vs Wingspan — 3S 3000 mAh</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 3.50 lb · semi 1.52 ft · root 0.66 ft · tip 0.48 ft</text><line x1="115" y1="44" x2="115" y2="252" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="75" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="60" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">70 cm</text>
  <text x="195" y="60" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">33 mnt</text>
  <rect x="115" y="71" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="73" width="103" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="86" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">76 cm</text>
  <text x="223" y="86" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">36 mnt</text>
  <rect x="115" y="97" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="99" width="132" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="112" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">80 cm</text>
  <text x="252" y="112" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">39 mnt</text>
  <rect x="115" y="123" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="125" width="160" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="138" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">85 cm</text>
  <text x="280" y="138" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">42 mnt</text>
  <rect x="115" y="149" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="151" width="188" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="164" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="308" y="164" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">45 mnt</text>
  <rect x="115" y="175" width="330" height="24" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="177" width="207" height="20" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="190" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">93 cm</text>
  <text x="327" y="190" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">47 mnt ← 93 cm ★</text>
  <rect x="115" y="201" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="203" width="216" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="216" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">95 cm</text>
  <text x="336" y="216" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">48 mnt</text>
  <rect x="115" y="227" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="229" width="245" height="20" fill="#1D9E75" rx="2" opacity="0.88"/>
  <text x="109" y="242" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="365" y="242" font-size="10" fill="#1D9E75" font-weight="normal" font-family="sans-serif">51 mnt</text></svg>

### Wing Loading
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Wing Loading vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 3.50 lb · semi 1.52 ft · root 0.66 ft · tip 0.48 ft</text><line x1="115" y1="44" x2="115" y2="252" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="264" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="60" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">70 cm</text>
  <text x="384" y="60" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">128 N/m²</text>
  <rect x="115" y="71" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="73" width="225" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="86" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">76 cm</text>
  <text x="345" y="86" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">118 N/m²</text>
  <rect x="115" y="97" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="99" width="201" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="112" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">80 cm</text>
  <text x="321" y="112" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">112 N/m²</text>
  <rect x="115" y="123" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="125" width="174" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="138" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">85 cm</text>
  <text x="294" y="138" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">105 N/m²</text>
  <rect x="115" y="149" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="151" width="155" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="164" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="275" y="164" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">100 N/m²</text>
  <rect x="115" y="175" width="330" height="24" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="177" width="139" height="20" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="190" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">93 cm</text>
  <text x="259" y="190" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">96 N/m² ← 93 cm ★</text>
  <rect x="115" y="201" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="203" width="132" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="216" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">95 cm</text>
  <text x="252" y="216" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">94 N/m²</text>
  <rect x="115" y="227" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="229" width="116" height="20" fill="#378ADD" rx="2" opacity="0.88"/>
  <text x="109" y="242" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="236" y="242" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">90 N/m²</text></svg>

### Kecepatan
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Kecepatan vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 3.50 lb · semi 1.52 ft</text>  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">22</text>
  <line x1="44" y1="89" x2="584" y2="89" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="93" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">19</text>
  <line x1="44" y1="135" x2="584" y2="135" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="139" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">15</text>
  <line x1="44" y1="180" x2="584" y2="180" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="184" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">12</text>
  <line x1="44" y1="226" x2="584" y2="226" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="230" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">9</text>
  <text x="44" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">70</text>
  <text x="121" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">76</text>
  <text x="198" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">80</text>
  <text x="275" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">85</text>
  <text x="352" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="429" y="239" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">93</text>
  <text x="506" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">95</text>
  <text x="584" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <rect x="427" y="44" width="4" height="182" fill="#0e6b3d" opacity="0.12"/>
  <polyline points="44,72 121,88 198,99 275,110 352,119 429,125 506,127 584,136" fill="none" stroke="#534AB7" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="72" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="88" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="99" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="110" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="119" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="125" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="127" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="136" r="3" fill="#534AB7" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,185 121,191 198,195 275,199 352,204 429,206 506,208 584,210" fill="none" stroke="#D85A30" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="185" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="191" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="195" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="199" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="204" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="206" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="208" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="210" r="3" fill="#D85A30" stroke="#ffffff" stroke-width="1"/>
  <line x1="429" y1="44" x2="429" y2="226" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="429" y="252" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">93 cm</text>
  <text x="44" y="265" font-size="9" fill="#534AB7" font-family="sans-serif">—— Vcruise m/s</text>
  <text x="150.5" y="265" font-size="9" fill="#D85A30" font-family="sans-serif">- -  Vstall m/s</text></svg>

### Aspect Ratio & L/D
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Aspect Ratio & L/D max vs Wingspan</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 3.50 lb · semi 1.52 ft</text>  <line x1="44" y1="44" x2="584" y2="44" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="48" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">13</text>
  <line x1="44" y1="89" x2="584" y2="89" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="93" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">11</text>
  <line x1="44" y1="135" x2="584" y2="135" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="139" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">8</text>
  <line x1="44" y1="180" x2="584" y2="180" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="184" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">6</text>
  <line x1="44" y1="226" x2="584" y2="226" stroke="#d4d2c8" stroke-width="0.6" stroke-dasharray="3,3"/>
  <text x="40" y="230" text-anchor="end" font-size="9" fill="#888780" font-family="sans-serif">4</text>
  <text x="44" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">70</text>
  <text x="121" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">76</text>
  <text x="198" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">80</text>
  <text x="275" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">85</text>
  <text x="352" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">90</text>
  <text x="429" y="239" text-anchor="middle" font-size="9" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">93</text>
  <text x="506" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">95</text>
  <text x="584" y="239" text-anchor="middle" font-size="9" fill="#888780" font-weight="normal" font-family="sans-serif">100</text>
  <rect x="427" y="44" width="4" height="182" fill="#0e6b3d" opacity="0.12"/>
  <polyline points="44,217 121,210 198,206 275,200 352,195 429,191 506,189 584,183" fill="none" stroke="#0e6b3d" stroke-width="2.2" stroke-linejoin="round" />
  <circle cx="44" cy="217" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="210" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="206" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="200" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="195" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="191" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="189" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="183" r="3" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <polyline points="44,103 121,96 198,90 275,84 352,79 429,75 506,73 584,67" fill="none" stroke="#BA7517" stroke-width="2.2" stroke-linejoin="round" stroke-dasharray="5,3"/>
  <circle cx="44" cy="103" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="121" cy="96" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="198" cy="90" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="275" cy="84" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="352" cy="79" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="429" cy="75" r="5" fill="#0e6b3d" stroke="#ffffff" stroke-width="1"/>
  <circle cx="506" cy="73" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <circle cx="584" cy="67" r="3" fill="#BA7517" stroke="#ffffff" stroke-width="1"/>
  <line x1="429" y1="44" x2="429" y2="226" stroke="#0e6b3d" stroke-width="1.5" stroke-dasharray="4,3" opacity="0.7"/>
  <text x="429" y="252" text-anchor="middle" font-size="8" fill="#0e6b3d" font-family="sans-serif">93 cm</text>
  <text x="44" y="265" font-size="9" fill="#0e6b3d" font-family="sans-serif">—— Aspect Ratio</text>
  <text x="156.0" y="265" font-size="9" fill="#BA7517" font-family="sans-serif">- -  L/D max</text></svg>

### Cruise Power
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 270"><rect width="600" height="270" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="300" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Cruise Power vs Wingspan (W)</text><text x="300" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">NACA 2412 · MTOW 3.50 lb · semi 1.52 ft · root 0.66 ft · tip 0.48 ft</text><line x1="115" y1="44" x2="115" y2="252" stroke="#d4d2c8" stroke-width="0.8"/>  <rect x="115" y="45" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="47" width="234" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="60" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">70 cm</text>
  <text x="354" y="60" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">52 W</text>
  <rect x="115" y="71" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="73" width="198" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="86" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">76 cm</text>
  <text x="318" y="86" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">47 W</text>
  <rect x="115" y="97" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="99" width="176" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="112" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">80 cm</text>
  <text x="296" y="112" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">44 W</text>
  <rect x="115" y="123" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="125" width="146" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="138" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">85 cm</text>
  <text x="266" y="138" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">40 W</text>
  <rect x="115" y="149" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="151" width="132" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="164" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">90 cm</text>
  <text x="252" y="164" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">38 W</text>
  <rect x="115" y="175" width="330" height="24" fill="#e6f4ee" rx="2"/>
  <rect x="115" y="177" width="117" height="20" fill="#0e6b3d" rx="2" opacity="0.88"/>
  <text x="109" y="190" text-anchor="end" font-size="11" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">93 cm</text>
  <text x="237" y="190" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">36 W ← 93 cm ★</text>
  <rect x="115" y="201" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="203" width="110" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="216" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">95 cm</text>
  <text x="230" y="216" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">35 W</text>
  <rect x="115" y="227" width="330" height="24" fill="#f5f5f5" rx="2"/>
  <rect x="115" y="229" width="95" height="20" fill="#D85A30" rx="2" opacity="0.88"/>
  <text x="109" y="242" text-anchor="end" font-size="11" fill="#888780" font-weight="normal" font-family="sans-serif">100 cm</text>
  <text x="215" y="242" font-size="10" fill="#D85A30" font-weight="normal" font-family="sans-serif">33 W</text></svg>

### Tabel

| Wingspan | Area | AR | WL | Vs | Vcruise | L/D | P cruise | Endurance |
|---|---|---|---|---|---|---|---|---|
| 70 cm | 0.121 m² | 4.0 | 128 N/m² | 11.8 m/s | 20.1 m/s | 10.0 | 52 W | 33 mnt |
| 76 cm | 0.131 m² | 4.4 | 118 N/m² | 11.3 m/s | 18.9 m/s | 10.4 | 47 W | 36 mnt |
| 80 cm | 0.139 m² | 4.6 | 112 N/m² | 11.0 m/s | 18.1 m/s | 10.7 | 44 W | 39 mnt |
| 85 cm | 0.147 m² | 4.9 | 105 N/m² | 10.7 m/s | 17.3 m/s | 11.0 | 40 W | 42 mnt |
| 90 cm | 0.156 m² | 5.2 | 100 N/m² | 10.4 m/s | 16.6 m/s | 11.3 | 38 W | 45 mnt |
| **93 cm ★** | **0.1610 m²** | **5.33** | **97 N/m²** | **10.26 m/s** | **16.26 m/s** | **11.49** | **36 W** | **47 mnt** |
| 95 cm | 0.164 m² | 5.5 | 94 N/m² | 10.1 m/s | 16.0 m/s | 11.6 | 35 W | 48 mnt |
| 100 cm | 0.174 m² | 5.8 | 90 N/m² | 9.9 m/s | 15.4 m/s | 11.9 | 33 W | 51 mnt |

---

## 6. Propulsi

### Power Budget
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 640 210"><rect width="640" height="210" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="320" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Power Budget — Satria Nano</text><text x="320" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">MTOW 3.50 lb · semi 1.52 ft · sys eff 60.6%</text>  <rect x="190" y="52" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="190" y="52" width="88" height="26" fill="#1D9E75" rx="3" opacity="0.88"/>
  <text x="186" y="69" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Cruise (16.3 m/s)</text>
  <text x="283" y="69" font-size="10" fill="#1D9E75" font-weight="bold" font-family="sans-serif">36 W = 0.048 HP</text>
  <rect x="190" y="90" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="190" y="90" width="243" height="26" fill="#BA7517" rx="3" opacity="0.88"/>
  <text x="186" y="107" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Climb 4m/s (99 W)</text>
  <text x="438" y="107" font-size="10" fill="#BA7517" font-weight="bold" font-family="sans-serif">99 W = 0.133 HP</text>
  <rect x="190" y="128" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="190" y="128" width="302" height="26" fill="#D85A30" rx="3" opacity="0.88"/>
  <text x="186" y="145" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Peak ×1.25 (123 W)</text>
  <text x="497" y="145" font-size="10" fill="#D85A30" font-weight="bold" font-family="sans-serif">123 W = 0.165 HP</text>
  <rect x="190" y="166" width="430" height="26" fill="#f5f5f5" rx="3"/>
  <rect x="190" y="166" width="430" height="26" fill="#D85A30" rx="3" opacity="0.88"/>
  <text x="186" y="183" text-anchor="end" font-size="10" fill="#444441" font-family="sans-serif">Motor rating min (200 W)</text>
  <text x="615" y="183" text-anchor="end" font-size="10" fill="#ffffff" font-weight="bold" font-family="sans-serif">200 W = 0.268 HP</text></svg>

### Propeller
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 720 185"><rect width="720" height="185" fill="#ffffff" rx="10" stroke="#d4d2c8" stroke-width="0.8"/><text x="360" y="26" text-anchor="middle" font-size="13" font-weight="bold" fill="#444441" font-family="sans-serif">Static Thrust vs Propeller — @ Peak 123 W</text><text x="360" y="40" text-anchor="middle" font-size="10" fill="#888780" font-family="sans-serif">J=0.55 · Vcruise 16.3 m/s · MTOW 1.588 kg</text>  <rect x="90" y="52" width="620" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="52" width="297" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="70" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">8×4.0</text>
  <text x="392" y="70" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">7.6 N · T/W 0.49 · RPM 8728 · KV@3S 983</text>
  <rect x="90" y="96" width="620" height="28" fill="#e6f4ee" rx="3"/>
  <rect x="90" y="96" width="320" height="28" fill="#0e6b3d" rx="3" opacity="0.88"/>
  <text x="86" y="114" text-anchor="end" font-size="12" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">9×4.5  ★</text>
  <text x="415" y="114" font-size="10" fill="#0e6b3d" font-weight="bold" font-family="sans-serif">8.2 N · T/W 0.53 · RPM 7758 · KV@3S 874</text>
  <rect x="90" y="140" width="620" height="28" fill="#f5f5f5" rx="3"/>
  <rect x="90" y="140" width="344" height="28" fill="#378ADD" rx="3" opacity="0.88"/>
  <text x="86" y="158" text-anchor="end" font-size="12" fill="#378ADD" font-weight="normal" font-family="sans-serif">10×4.7</text>
  <text x="439" y="158" font-size="10" fill="#378ADD" font-weight="normal" font-family="sans-serif">8.8 N · T/W 0.57 · RPM 6982 · KV@3S 786</text></svg>

| Parameter | Nilai |
|---|---|
| Motor | **2216, KV 1000 @ 3S** |
| Power rating | ≥ 200 W |
| **Propeller** | **APC 9×4.5** |
| ESC | **30 A BLHeli_32** |
| **Baterai** | **4S 2200 mAh atau 3S 3000 mAh** |

| Baterai | Endurance | Kargo | C-rate | |
|---|---|---|---|---|
| 2S 2200 mAh | ~17 mnt | 460 g | tinggi | ✗ Hindari |
| 3S 2200 mAh | ~33 mnt | 430 g | 7.7C | Cukup |
| **3S 3000 mAh** | **~47 mnt** | **390 g** | **5.7C** | **✓** |
| **4S 2200 mAh** | **~47 mnt** | **410 g** | **5.8C** | **✓** |

---

## 7. Misi & Jangkauan

| Konfigurasi | Kecepatan | Kargo | Endurance | Range one-way | Radius RTH |
|---|---|---|---|---|---|
| 3S 3000 mAh — cruise | 58.5 km/h | 390 g | ~47 mnt | ~46 km | ~19–21 km |
| 4S 2200 mAh — cruise | 58.5 km/h | 410 g | ~47 mnt | ~46 km | ~19–21 km |
| **3S 3000 mAh — HS 80** | **80 km/h** | **390 g** | **~28 mnt** | **~38 km** | **~16 km** |
| **4S 2200 mAh — HS 80** | **80 km/h** | **410 g** | **~28 mnt** | **~38 km** | **~16 km** |
| 3S 3000 mAh — HS 100 | 100 km/h | 390 g | ~18 mnt | ~30 km | ~12 km |
| 4S 2200 mAh — HS 100 | 100 km/h | 410 g | ~18 mnt | ~30 km | ~12 km |

---

## 8. Ringkasan Spesifikasi Final

| Parameter | Nilai |
|---|---|
| **Airfoil** | **NACA 2412** |
| **Semi-length** | **1.52 ft (46.33 cm)** |
| **Wingspan** | **92.66 cm** |
| **Root / Tip chord** | **20.12 cm / 14.63 cm** |
| Taper ratio | 0.7273 |
| Sweep | 0.0° |
| Wing area | 0.1610 m² |
| Aspect ratio | 5.3333 |
| MAC | 17.37 cm @ ±21.9 cm dari CL |
| Konfigurasi ekor | V-tail twin fin (45°) |
| **Empty weight** | **2.20 lb = 0.998 kg** |
| **MTOW** | **3.50 lb = 1.588 kg** |
| Payload | 590 g |
| **CG fwd** | **0.62 ft = 4.95 cm dari LE = 28.5% MAC** |
| **CG nominal ✓** | **0.63 ft = 5.26 cm dari LE = 30.3% MAC** |
| **CG aft limit** | **0.65 ft = 5.87 cm dari LE = 33.8% MAC** |
| Wing loading | 96.7 N/m² |
| **Stall speed** | **10.26 m/s (36.9 km/h)** |
| **Cruise speed** | **16.26 m/s (58.5 km/h)** |
| VNE | 35.92 m/s |
| L/D max | 11.49 |
| Cruise power | 36.3 W (0.049 HP) |
| Peak power | 123 W (0.165 HP) |
| **Endurance (cruise)** | **~47 mnt** |
| **Range one-way (cruise)** | **~46 km** |
| **Radius RTH (cruise)** | **~19–21 km** |
| Cruise power HS 80 | 59.7 W (0.080 HP) |
| **Endurance HS 80** | **~28 mnt** |
| **Range one-way HS 80** | **~38 km** |
| **Radius RTH HS 80** | **~16 km** |
| Cruise power HS 100 | 93 W (0.125 HP) |
| Endurance HS 100 | ~18 mnt |
| Range one-way HS 100 | ~30 km |
| Radius RTH HS 100 | ~12 km |
| Motor | **2216, KV 1000 @ 3S** |
| Propeller (cruise) | APC 9×4.5 |
| Propeller HS 80 | APC 8×6 |
| **Propeller HS 100** | **APC 9×7** |
| ESC | 30 A BLHeli_32 |
| Baterai | 4S 2200 mAh / 3S 3000 mAh |

---

*UAV Satria Nano · NACA 2412 · Semi 1.52 ft · Root 0.66 ft · Tip 0.48 ft · Sweep 0° · V-tail*  
*Empty 2.20 lb · MTOW 3.50 lb · Seluruh nilai performa adalah estimasi teoritis.*
