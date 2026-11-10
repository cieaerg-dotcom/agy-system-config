import json
import os

transcript_path = "/Users/mac/.gemini/antigravity-cli/brain/34a7f87d-7431-4921-a669-9f283e028fe0/.system_generated/logs/transcript.jsonl"
output_path = "/Users/mac/Google Drive/我的雲端硬碟/AGY工作區/2015MBP_最新對話記錄.md"

md_content = "# Antigravity 2015MBP 最新對話記錄\n\n"

if os.path.exists(transcript_path):
    with open(transcript_path, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                data = json.loads(line)
                if data.get("type") == "USER_INPUT":
                    md_content += f"## [User] {data.get('timestamp', '')}\n{data.get('content', '')}\n\n"
                elif data.get("type") == "PLANNER_RESPONSE":
                    md_content += f"## [Gemini] {data.get('timestamp', '')}\n{data.get('content', '')}\n\n"
            except:
                pass

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(md_content)

print("Transcript exported.")
