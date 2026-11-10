import os
import re
import sys

def format_verbatim(input_path, output_path):
    with open(input_path, "r", encoding="utf-8") as f:
        lines = f.readlines()

    header = ""
    processed_paragraphs = []
    
    current_para = ""
    lines_in_para = 0
    
    # Regex to match whisper timestamps
    timestamp_pattern = re.compile(r"^\[\d\d:\d\d:\d\d\.\d\d\d --> \d\d:\d\d:\d\d\.\d\d\d\]\s+(.*)$")

    for line in lines:
        line = line.strip()
        if not line:
            continue
            
        if line.startswith("# "):
            header = line + "\n\n"
            continue
            
        match = timestamp_pattern.match(line)
        if match:
            text = match.group(1).strip()
            if not text:
                continue
                
            current_para += text
            lines_in_para += 1
            
            # Check if we should break paragraph
            ends_with_punct = text.endswith('。') or text.endswith('！') or text.endswith('？') or text.endswith('!') or text.endswith('?')
            
            if (ends_with_punct and lines_in_para >= 3) or (lines_in_para >= 6):
                processed_paragraphs.append(current_para)
                current_para = ""
                lines_in_para = 0
        else:
            # If it's not a timestamp line and not empty, it might be a header or something else.
            # Just ignore it since it's a pure text conversion.
            pass

    if current_para:
        processed_paragraphs.append(current_para)

    # Write output
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(header)
        for p in processed_paragraphs:
            f.write(p + "\n\n")
            
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python3 format_verbatim.py <input> <output>")
        sys.exit(1)
    format_verbatim(sys.argv[1], sys.argv[2])
