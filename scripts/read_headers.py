import os, glob
folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026一月風尚之旅逐字稿"
files = [f for f in glob.glob(os.path.join(folder, "錄音 *.md")) if "_" not in os.path.basename(f)]
for f in sorted(files):
    with open(f, "r", encoding="utf-8") as file:
        lines = [file.readline().strip() for _ in range(30)]
        # find non-empty lines
        lines = [l for l in lines if l and not l.startswith("# ")]
        print(f"File: {os.path.basename(f)} | Snippet: {' '.join(lines[:3])}")
