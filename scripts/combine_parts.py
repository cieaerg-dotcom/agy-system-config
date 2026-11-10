import os
import glob
import re

folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026風尚之旅"
md_files = glob.glob(os.path.join(folder, "*_part*.md"))

# Group parts by base name
groups = {}
pattern = re.compile(r"^(錄音 \d+)_part\d+\.md$")

for path in md_files:
    basename = os.path.basename(path)
    match = pattern.match(basename)
    if match:
        base = match.group(1)
        if base not in groups:
            groups[base] = []
        groups[base].append(path)

# Combine each group
for base, paths in groups.items():
    paths.sort()  # Ensure correct part order
    combined_path = os.path.join(folder, f"{base}.md")
    
    with open(combined_path, "w", encoding="utf-8") as out_f:
        for p in paths:
            with open(p, "r", encoding="utf-8") as in_f:
                out_f.write(in_f.read())
                out_f.write("\n")
    
    print(f"Combined {len(paths)} parts into {base}.md")
    
    # Remove parts after combining
    for p in paths:
        os.remove(p)
        # Also remove the corresponding audio parts to save space
        audio_part = p.replace(".md", ".m4a")
        if os.path.exists(audio_part):
            os.remove(audio_part)

print("All parts combined successfully.")
