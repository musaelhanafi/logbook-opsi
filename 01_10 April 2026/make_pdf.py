import markdown, base64, os, re, subprocess
from urllib.parse import unquote
from weasyprint import HTML, CSS

CHROME   = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE     = os.path.dirname(os.path.abspath(__file__))
MD_PATH  = os.path.join(BASE, "logbook_10_april_2026.md")
PDF_PATH = os.path.join(BASE, "logbook_10_april_2026.pdf")
SCALE    = 2

with open(MD_PATH, encoding="utf-8") as f:
    md = f.read()

def embed_ext(m):
    alt, path = m.group(1), m.group(2)
    if path.startswith("data:") or path.startswith("http"): return m.group(0)
    abs_path = os.path.join(BASE, unquote(path))
    if not os.path.exists(abs_path): return m.group(0)
    ext  = os.path.splitext(abs_path)[1].lower().lstrip(".")
    mime = {"png":"image/png","jpg":"image/jpeg","jpeg":"image/jpeg"}.get(ext,"image/png")
    with open(abs_path,"rb") as f: b64 = base64.b64encode(f.read()).decode()
    return f'<img src="data:{mime};base64,{b64}" alt="{alt}" class="ext-img" />'

md = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', embed_ext, md)

def render_svg(svg, idx):
    png = os.path.join(BASE, f"svg_{idx:02d}.png")
    if os.path.exists(png):
        print(f"  [{idx:02d}] pakai {os.path.basename(png)}", flush=True)
        return png
    print(f"  [{idx:02d}] render → {os.path.basename(png)}", flush=True)
    vb = re.search(r'viewBox=["\']([^"\']+)["\']', svg)
    vw, vh = 860, 400
    if vb:
        p = vb.group(1).split()
        if len(p) == 4: vw, vh = float(p[2]), float(p[3])
    px_w, px_h = int(vw*SCALE), int(vh*SCALE)
    svg_s = re.sub(r'^(<svg\b)', f'\\1 width="{px_w}" height="{px_h}"', svg, count=1)
    import tempfile
    with tempfile.NamedTemporaryFile(suffix=".svg", delete=False, mode="w", encoding="utf-8") as tf:
        tf.write(svg_s); tmp = tf.name
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox",
                    "--hide-scrollbars",f"--window-size={px_w},{px_h}",
                    f"--screenshot={png}",f"file://{tmp}"],
                   capture_output=True, timeout=30)
    os.remove(tmp)
    return png

svg_paths = []
counter   = [0]

def lift(m):
    idx = counter[0]
    svg_paths.append(render_svg(m.group(0), idx))
    counter[0] += 1
    return f"SVGBLOCK{idx:02d}HERE"

print("Memeriksa SVG...")
md = re.sub(r"<svg\b.*?</svg>", lift, md, flags=re.DOTALL)
print(f"  {counter[0]} SVG siap.\n")

body = markdown.markdown(md, extensions=["tables","fenced_code","nl2br","extra"])

for i, png in enumerate(svg_paths):
    with open(png,"rb") as f: b64 = base64.b64encode(f.read()).decode()
    img = f'<div class="svg-box"><img src="data:image/png;base64,{b64}" /></div>'
    ph  = f"SVGBLOCK{i:02d}HERE"
    body = body.replace(f"<p>{ph}</p>", img).replace(ph, img)

css = CSS(string="""
@page { size: A4; margin: 16mm 14mm 16mm 14mm; }
* { box-sizing: border-box; }
body { font-family: "Helvetica Neue", Arial, sans-serif; font-size: 9.5pt; line-height: 1.55; color: #222; }
h1 { font-size: 16pt; color: #1a1a2e; border-bottom: 2px solid #0e6b3d; padding-bottom: 5px; margin: 0 0 10px; }
h2 { font-size: 12pt; color: #0e6b3d; margin-top: 20px; border-bottom: 1px solid #d4d2c8; padding-bottom: 3px; }
h3 { font-size: 10.5pt; color: #333; margin: 12px 0 4px; }
blockquote { background: #f0f7f4; border-left: 4px solid #0e6b3d; margin: 8px 0; padding: 6px 12px; border-radius: 4px; font-size: 9pt; }
table { border-collapse: collapse; width: 100%; margin: 8px 0; font-size: 8.5pt; }
th { background: #f0f0f0; font-weight: 600; padding: 4px 8px; border: 1px solid #c8c8c8; text-align: left; }
td { padding: 3px 8px; border: 1px solid #ddd; }
tr:nth-child(even) td { background: #fafafa; }
hr { border: none; border-top: 1px solid #d4d2c8; margin: 14px 0; }
pre { background: #f5f5f5; padding: 8px 12px; border-radius: 4px; font-size: 7.5pt; overflow: auto; white-space: pre-wrap; }
code { font-size: 8pt; }
.svg-box { width: 100%; margin: 6px 0; }
.svg-box img { width: 100%; height: auto; display: block; }
.ext-img { max-width: 75%; height: auto; display: block; margin: 8px auto; border-radius: 4px; }
p { margin: 4px 0; }
em { color: #666; }
a { color: #0e6b3d; }
""")

print("Membuat PDF...")
HTML(string=f"""<!DOCTYPE html>
<html lang="id"><head><meta charset="UTF-8"><title>Logbook 10 April 2026</title></head>
<body>{body}</body></html>""", base_url=BASE
).write_pdf(PDF_PATH, stylesheets=[css])

print(f"PDF selesai: {PDF_PATH} ({os.path.getsize(PDF_PATH)//1024} KB)")
