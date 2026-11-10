---
name: verbatim-processor
description: >-
  Standardizes and formats Whisper audio transcription outputs by removing timestamps, grouping dialogue into natural readable paragraphs, and applying business terminology correction workflows according to the recording SOP.
---

# 錄音轉錄逐字稿標準化與處理技能 (Verbatim Processor)

本技能提供標準化流程，用於將 `whisper.cpp` 轉錄出的時間軸文字檔，快速清理為段落自然流暢、無時間戳記雜訊的 Markdown 逐字稿文件。

## 核心處理流程

1. **時間戳記剔除與智慧分段**：
   執行內建 Python 腳本，自動過濾 `[00:00:00.000 --> 00:00:00.000]` 時間標記，並依標點符號與語句長度自動組織段落。

   ```bash
   python3 .agents/skills/verbatim-processor/scripts/format_verbatim.py <輸入原始逐字稿.txt> <輸出整理後逐字稿.md>
   ```

2. **語音校正與名詞對照（依據 GEMINI.md 規範）**：
   - 嚴禁擅自精簡或刪減說話者原文。
   - 針對切塊產出的逐字稿，依據事業上下文（如營養補充產品、專業術語）執行同音錯字校正。
   - 保持語句通順，不改變說話者語氣與原意。

3. **命名與存檔規範**：
   - 完成校正後，文件命名格式強制為：
     `「資料夾名稱」「錄音序號」-「內容簡介」.md`
   - 內容簡介由系統閱讀文本後產出 5~10 字簡短說明。
