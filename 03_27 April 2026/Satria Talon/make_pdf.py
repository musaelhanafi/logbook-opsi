import markdown, base64, os, re, subprocess, tempfile

CHROME   = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE     = os.path.dirname(os.path.abspath(__file__))
MD_PATH  = os.path.join(BASE, "satria_talon_spesifikasi.md")
PDF_PATH = os.path.join(BASE, "satria_talon_spesifikasi.pdf")
SCALE    = 2

with open(MD_PATH, encoding="utf-8") as f:
    md = f.read()

def render_svg_to_png(svg: str, out_png: str):
    vb = re.search(r'viewBox=["\']([^"\']+)["\']', svg)
    vw, vh = 860, 400
    if vb:
        parts = vb.group(1).split()
        if len(parts) == 4:
            vw = float(parts[2])
            vh = float(parts[3])
    px_w = int(vw * SCALE)
    px_h = int(vh * SCALE)
    html = f"""<!DOCTYPE html>
<html><head><meta charset="UTF-8"><style>
  html, body {{ margin:0; padding:0; background:#ffffff; }}
  svg {{ width:{px_w}px; height:{px_h}px; display:block; }}
</style></head>
<body>{svg}</body></html>"""
    with tempfile.NamedTemporaryFile(suffix=".html", delete=False,
                                     mode="w", encoding="utf-8") as tf:
        tf.write(html)
        tmp = tf.name
    subprocess.run([
        CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
        "--hide-scrollbars", "--force-device-scale-factor=1",
        f"--window-size={px_w},{px_h}",
        f"--screenshot={out_png}",
        f"file://{tmp}",
    ], capture_output=True, timeout=30)
    os.remove(tmp)

svg_pngs = []
counter  = [0]

def extract_svg(m):
    idx = counter[0]
    png = os.path.join(BASE, f"svg_{idx:02d}.png")
    print(f"  [{idx:02d}] render SVG → {os.path.basename(png)}", flush=True)
    render_svg_to_png(m.group(0), png)
    svg_pngs.append(png)
    counter[0] += 1
    return f"SVGBLOCK{idx:02d}HERE"

print("Rendering SVGs ke PNG...")
md_clean = re.sub(r"<svg\b.*?</svg>", extract_svg, md, flags=re.DOTALL)
print(f"  {counter[0]} SVG selesai.\n")

body = markdown.markdown(md_clean, extensions=["tables", "fenced_code", "nl2br", "extra"])

for i, png_path in enumerate(svg_pngs):
    with open(png_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    img_tag = f'<div class="svg-box"><img src="data:image/png;base64,{b64}" /></div>'
    ph = f"SVGBLOCK{i:02d}HERE"
    body = body.replace(f"<p>{ph}</p>", img_tag)
    body = body.replace(ph, img_tag)

html_full = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>UAV Satria Talon — Spesifikasi</title>
<style>
  @media print {{
    @page {{ size: A4; margin: 14mm 13mm; }}
    body  {{ -webkit-print-color-adjust: exact; print-color-adjust: exact; }}
  }}
  * {{ box-sizing: border-box; }}
  body {{
    font-family: -apple-system, "Helvetica Neue", Arial, sans-serif;
    font-size: 10pt; line-height: 1.55; color: #222;
    max-width: 780px; margin: 0 auto; padding: 10px 0;
  }}
  h1 {{ font-size: 17pt; color: #1a1a2e; border-bottom: 2.5px solid #0e6b3d; padding-bottom: 5px; margin: 0 0 10px; }}
  h2 {{ font-size: 12.5pt; color: #0e6b3d; margin-top: 22px; border-bottom: 1px solid #d4d2c8; padding-bottom: 3px; }}
  h3 {{ font-size: 10.5pt; color: #333; margin: 14px 0 4px; }}
  blockquote {{ background: #f0f7f4; border-left: 4px solid #0e6b3d; margin: 8px 0; padding: 6px 14px; border-radius: 4px; font-size: 9pt; }}
  table {{ border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 9pt; }}
  th {{ background:#f0f0f0; font-weight:600; padding:4px 8px; border:1px solid #c8c8c8; text-align:left; }}
  td {{ padding:3px 8px; border:1px solid #ddd; }}
  tr:nth-child(even) td {{ background:#fafafa; }}
  hr {{ border:none; border-top:1px solid #d4d2c8; margin:14px 0; }}
  .svg-box {{ width:100%; margin:6px 0; }}
  .svg-box img {{ width:100%; height:auto; display:block; }}
  p {{ margin:4px 0; }}
  em {{ color:#666; }}
</style>
</head>
<body>{body}</body>
</html>"""

tmp_html = os.path.join(BASE, "_build.html")
with open(tmp_html, "w", encoding="utf-8") as f:
    f.write(html_full)

print("Membuat PDF...")
result = subprocess.run([
    CHROME, "--headless=new", "--disable-gpu", "--no-sandbox",
    f"--print-to-pdf={PDF_PATH}",
    "--print-to-pdf-no-header", "--no-pdf-header-footer",
    f"file://{tmp_html}",
], capture_output=True, text=True, timeout=60)

os.remove(tmp_html)

if result.returncode != 0:
    print("ERROR:", result.stderr[:500])
else:
    sz = os.path.getsize(PDF_PATH) // 1024
    print(f"PDF selesai: {PDF_PATH} ({sz} KB)")
    print(f"PNG files : {[os.path.basename(p) for p in svg_pngs]}")
