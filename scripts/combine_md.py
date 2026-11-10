import os

folder = "/Users/mac/Google Drive/我的雲端硬碟/AGY工作區/617-618"
parts = ["part1.md", "part2.md", "part3.md"]
output = os.path.join(folder, "錄音_017_完整中文版_EricWorre_逐字翻譯.md")

with open(output, "w", encoding="utf-8") as outfile:
    for p in parts:
        filepath = os.path.join(folder, f"錄音_017_完整逐字中文版_{p}")
        with open(filepath, "r", encoding="utf-8") as infile:
            outfile.write(infile.read())
            outfile.write("\n")

print("Files combined successfully.")
