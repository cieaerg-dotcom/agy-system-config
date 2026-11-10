import os
import glob
import re

folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026六月風雲大會逐字稿"
md_files = glob.glob(os.path.join(folder, "*.md"))

def process_file(path):
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    # Normalize newlines: some files use \n\n, some use \n
    # Let's split into individual lines first, ignoring empty lines
    lines = [line.strip() for line in text.split('\n') if line.strip()]
    
    new_paragraphs = []
    current_para = ""
    
    for line in lines:
        if line.startswith("#"):
            # Flush current
            if current_para:
                new_paragraphs.append(current_para)
                current_para = ""
            new_paragraphs.append(line)
        elif line.startswith("-") or line.startswith("*"):
            # List item
            if current_para:
                new_paragraphs.append(current_para)
                current_para = ""
            new_paragraphs.append(line)
        else:
            # Regular text
            current_para += line
            
            # If current paragraph ends with sentence-ending punctuation and is long enough
            # OR if it's getting too long, we break it.
            if len(current_para) > 150 and current_para[-1] in "。！？!?":
                new_paragraphs.append(current_para)
                current_para = ""
            elif len(current_para) > 300:
                # Force break
                new_paragraphs.append(current_para)
                current_para = ""
                
    if current_para:
        new_paragraphs.append(current_para)
        
    formatted_text = "\n\n".join(new_paragraphs) + "\n"
    
    if formatted_text != text:
        with open(path, "w", encoding="utf-8") as f:
            f.write(formatted_text)
        return True
    return False

for path in md_files:
    if process_file(path):
        print(f"Reformatted: {os.path.basename(path)}")
