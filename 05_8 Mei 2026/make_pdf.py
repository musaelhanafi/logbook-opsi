import markdown, base64, os, re, subprocess, tempfile
from urllib.parse import unquote

CHROME   = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BASE     = os.path.dirname(os.path.abspath(__file__))
MD_PATH  = os.path.join(BASE, "logbook_8_mei_2026.md")
PDF_PATH = os.path.join(BASE, "logbook_8_mei_2026.pdf")
SCALE    = 2

with open(MD_PATH, encoding="utf-8") as f:
    md = f.read()

def embed_ext(m):
    alt, path = m.group(1), m.group(2)
    if path.startswith("data:") or path.startswith("http"):
        return m.group(0)
    abs_path = os.path.join(BASE, unquote(path))
    if not os.path.exists(abs_path):
        return m.group(0)
    ext  = os.path.splitext(abs_path)[1].lower().lstrip(".")
    mime = {"png": "image/png", "jpg": "image/jpeg", "jpeg": "image/jpeg"}.get(ext, "image/png")
    with open(abs_path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    return f'<img src="data:{mime};base64,{b64}" alt="{alt}" class="ext-img" />'

md = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', embed_ext, md)

body = markdown.markdown(md, extensions=["tables", "fenced_code", "nl2br", "extra"])

css = """
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
.ext-img { max-width: 75%; height: auto; display: block; margin: 8px auto; border-radius: 4px; }
p { margin: 4px 0; }
em { color: #666; }
a { color: #0e6b3d; }
"""

html = f"""<!DOCTYPE html>
<html lang="id">
<head>
<meta charset="UTF-8">
<title>Logbook 8 Mei 2026</title>
<style>{css}</style>
</head>
<body>{body}</body>
</html>"""

with tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8") as tf:
    tf.write(html)
    tmp_html = tf.name

print("Membuat PDF via Chrome headless...")
result = subprocess.run(
    [
        CHROME,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--run-all-compositor-stages-before-draw",
        "--print-to-pdf-no-header",
        f"--print-to-pdf={PDF_PATH}",
        f"file://{tmp_html}",
    ],
    capture_output=True,
    timeout=60,
)
os.remove(tmp_html)

if result.returncode != 0:
    print("STDERR:", result.stderr.decode())
    raise RuntimeError("Chrome gagal generate PDF")

print(f"PDF selesai: {PDF_PATH} ({os.path.getsize(PDF_PATH)//1024} KB)")
