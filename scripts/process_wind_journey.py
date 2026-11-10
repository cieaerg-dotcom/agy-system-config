import os
import re
import subprocess
import traceback

folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026風尚之旅"
log_path = os.path.join(folder, "process_log.txt")

try:
    with open(log_path, "w", encoding="utf-8") as log:
        log.write("Started processing...\n")
        
        all_files = os.listdir(folder)
        log.write(f"Found {len(all_files)} files in folder.\n")
        
        md_files = [f for f in all_files if f.endswith(".md") and "_part" in f]
        log.write(f"Found {len(md_files)} part files.\n")
        
        groups = {}
        pattern = re.compile(r"^(錄音\s+\d+)_part\d+\.md$")
        
        for basename in md_files:
            match = pattern.match(basename)
            if match:
                base = match.group(1)
                if base not in groups:
                    groups[base] = []
                groups[base].append(os.path.join(folder, basename))
            else:
                log.write(f"File {basename} did not match pattern!\n")
                
        for base, paths in groups.items():
            paths.sort()
            combined_path = os.path.join(folder, f"{base}.md")
            log.write(f"Combining {len(paths)} parts into {combined_path}\n")
            
            with open(combined_path, "w", encoding="utf-8") as out_f:
                for p in paths:
                    with open(p, "r", encoding="utf-8") as in_f:
                        out_f.write(in_f.read())
                        out_f.write("\n")
                        
            for p in paths:
                os.remove(p)
                audio_part = p.replace(".md", ".m4a")
                if os.path.exists(audio_part):
                    os.remove(audio_part)

        # Step 2: Reformat and Rename
        all_mds = [f for f in os.listdir(folder) if f.endswith(".md") and "part" not in f]
        log.write(f"Found {len(all_mds)} full md files.\n")
        rename_pattern = re.compile(r"^錄音\s+(\d+)\.md$")

        def reformat_text(text):
            timestamp_pattern = re.compile(r"^\[\d\d:\d\d:\d\d\.\d\d\d --> \d\d:\d\d:\d\d\.\d\d\d\]\s+(.*)$", re.MULTILINE)
            text = timestamp_pattern.sub(r"\1", text)
            
            paragraphs = text.split("\n\n")
            new_paragraphs = []
            
            for p in paragraphs:
                p = p.strip()
                if not p:
                    continue
                
                lines = [line.strip() for line in p.split('\n') if line.strip()]
                p = "".join(lines)
                    
                sentences = re.split(r'(?<=[。！？!\?])', p)
                
                current_chunk = ""
                for s in sentences:
                    s = s.strip()
                    if not s:
                        continue
                        
                    if len(s) > 300:
                        sub_sentences = re.split(r'(?<=[，,])', s)
                        for sub in sub_sentences:
                            sub = sub.strip()
                            if not sub:
                                continue
                            current_chunk += sub
                            if len(current_chunk) > 150:
                                new_paragraphs.append(current_chunk)
                                current_chunk = ""
                    else:
                        current_chunk += s
                        if len(current_chunk) > 200:
                            new_paragraphs.append(current_chunk)
                            current_chunk = ""
                            
                if current_chunk:
                    new_paragraphs.append(current_chunk)

            return "\n\n".join(new_paragraphs) + "\n"

        for basename in all_mds:
            match = rename_pattern.match(basename)
            if match:
                num = int(match.group(1))
                new_basename = f"錄音_{num:03d}_完整中文版.md"
                new_path = os.path.join(folder, new_basename)
                old_path = os.path.join(folder, basename)
                
                log.write(f"Formatting and renaming {basename} -> {new_basename}\n")
                with open(old_path, "r", encoding="utf-8") as f:
                    text = f.read()
                    
                formatted_text = reformat_text(text)
                
                with open(new_path, "w", encoding="utf-8") as f:
                    f.write(formatted_text)
                    
                os.remove(old_path)
            else:
                log.write(f"File {basename} did not match rename pattern!\n")

        log.write("Finished processing python steps.\n")
        
        # Step 3: Convert to HTML
        subprocess.run(["python3", "/Users/mac/geminicli/scripts/convert_to_html.py", folder], check=True)
        log.write("HTML conversion done.\n")

except Exception as e:
    with open(log_path, "a", encoding="utf-8") as log:
        log.write(f"ERROR: {e}\n{traceback.format_exc()}\n")
