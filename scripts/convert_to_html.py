import os, glob, re, sys

if len(sys.argv) > 1:
    folder = sys.argv[1]
else:
    folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026一月風尚之旅逐字稿"

md_files = glob.glob(os.path.join(folder, "錄音_*_*.md"))

html_template = """<!DOCTYPE html>
<html lang="zh-TW">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<style>
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "PingFang TC", "Microsoft JhengHei", sans-serif;
    line-height: 1.8;
    padding: 20px;
    max-width: 800px;
    margin: 0 auto;
    color: #333333;
    background-color: #f9f9f9;
  }}
  @media (prefers-color-scheme: dark) {{
    body {{ background-color: #1c1c1e; color: #e5e5ea; }}
    h1 {{ border-bottom: 1px solid #38383a; }}
  }}
  h1 {{ font-size: 1.6em; border-bottom: 1px solid #e5e5ea; padding-bottom: 10px; margin-bottom: 20px; }}
  p {{ margin-bottom: 1.2em; text-align: justify; }}
  strong {{ color: #007aff; font-weight: 600; }}
  @media (prefers-color-scheme: dark) {{
    strong {{ color: #0a84ff; }}
  }}
</style>
</head>
<body>
{content}
</body>
</html>"""

for filepath in md_files:
    filename = os.path.basename(filepath)
    title = filename.replace('.md', '')
    
    with open(filepath, 'r', encoding='utf-8') as f:
        md_text = f.read()
        
    paragraphs = md_text.split('\n\n')
    html_content = ""
    for para in paragraphs:
        para = para.strip()
        if not para:
            continue
        if para.startswith('# '):
            html_content += f"<h1>{para[2:]}</h1>\n"
        else:
            # Replace **text** with <strong>text</strong>
            para = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', para)
            html_content += f"<p>{para}</p>\n"
            
    final_html = html_template.format(title=title, content=html_content)
    
    html_path = os.path.join(folder, title + ".html")
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(final_html)

print("Converted all MD files to HTML.")
