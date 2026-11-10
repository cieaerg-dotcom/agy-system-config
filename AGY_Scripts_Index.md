# AGY 專案腳本清單與紀錄 (AGY Scripts Index)

本檔案記錄了由 AGY (Antigravity) 協助撰寫或本機常用的腳本，以便未來快速查詢與維護。

## 1. 根目錄工具腳本 (`/Users/mac/AGY本地工作區/`)
*   **`agy_watcher.py`**: 用於監控 AGY 狀態或同步日誌的 Python 腳本。
*   **`build_keynote.scpt`**: 自動化建置或操作 Mac Keynote 簡報的 AppleScript。
*   **`generate_keynote_script.py`**: 搭配產生 Keynote 簡報內容或自動化腳本的 Python 程式。
*   **`extract.py`**: 資料擷取腳本。
*   **`rebuild_logs.py`**: 用於重建或修復系統日誌的腳本。
*   **`transcribe_file.py`**: 單一音檔轉錄文字的 Python 腳本（搭配 Whisper 使用）。

## 2. 語音轉錄與文本處理工具 (`/Users/mac/AGY本地工作區/scripts/`)
此資料夾主要包含大量自動化語音轉文字、文檔格式轉換、以及特定專案處理的腳本：
*   **轉錄控制 (Transcription)**:
    *   `transcribe_all.sh`, `transcribe.sh`, `run_whisper.sh`
    *   `transcribe_audios.py`, `transcribe_17.py`, `transcribe_yuanmeng.py`
    *   `build_and_transcribe.sh`, `start_sync.sh`, `auto_sync_transcripts.py`
*   **音檔處理**: `split_audio.sh`
*   **文檔與格式轉換 (Format & Conversion)**:
    *   `convert_md_to_json.js`, `convert_to_html.py`, `convert_single.py`
    *   `format_verbatim.py`, `reformat_paragraphs.py`, `read_headers.py`, `export_transcript.py`
*   **檔案合併與重命名**: `combine.js`, `combine_md.py`, `combine_parts.py`, `rename_files.py`
*   **特定專案資料處理**:
    *   `fix_liuren_json.js`, `universal_liuren_parser.js` (大六壬相關解析)
    *   `process_transcripts.py`, `process_wind_journey.py`
    *   `split_kege.js`, `normalize_zhinan.js`, `build_encyclopedia.js`
    *   `generate_ppt.py` (自動產生簡報檔)

## 3. 命理系統開發檔案 (`/Users/mac/AGY本地工作區/Book-of-Fate/`)
這是一個命理與占卜的 Web 應用程式專案，包含多種命理引擎與前端介面（UI）腳本：
*   **核心引擎 (`*_engine.js`)**: `zhouyi_engine.js` (周易), `ziwei_engine.js` (紫微斗數), `qimen_engine.js` (奇門遁甲), `meihua_engine.js` (梅花易數), `liuren_engine.js` (大六壬), `numerology_engine.js` (生命靈數), `astrology_engine.js` (占星學)。
*   **介面邏輯 (`*_ui.js`)**: 對應上述引擎的 UI 檔案，如 `zhouyi_ui.js`, `tarot_ui.js` 等。
*   **資料與輔助**: `*_data.js`, `storage_manager.js`, `ui_controller.js`, `main_app.js`。

---
*註：這個清單是用來協助 AGY 記憶與管理過去撰寫的腳本。當您需要修改上述任何功能時，可以直接參考這個檔案。*
