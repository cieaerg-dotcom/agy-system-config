import os, sys, re

filepath = sys.argv[1]
filename = os.path.basename(filepath)
title = filename.replace('.md', '')

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
  h2 {{ font-size: 1.3em; margin-top: 1.5em; color: #0056b3; }}
  @media (prefers-color-scheme: dark) {{
    h2 {{ color: #409cff; }}
  }}
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
    elif para.startswith('## '):
        html_content += f"<h2>{para[3:]}</h2>\n"
    else:
        # Replace **text** with <strong>text</strong>
        para = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', para)
        html_content += f"<p>{para}</p>\n"
        
final_html = html_template.format(title=title, content=html_content)

html_path = filepath.replace('.md', '.html')
with open(html_path, 'w', encoding='utf-8') as f:
    f.write(final_html)

print(f"Converted {filename} to HTML.")
