# Antigravity 會話交接文件 (Handover Context)

## 1. 專案背景與目標
*   **目標：** 建立一個能在「完全無網路」的 Windows 電腦上執行的 AI 離線安裝包。
*   **核心功能：** 
    1. 手寫筆記光學字元辨識 (OCR)
    2. 語音辨識轉文字 (ASR)
    3. AI 文字排版與校正
    4. 最終自動匯出成 Office 講義格式

## 2. 檔案與目錄結構 (存放在 Mac 本機)
所有打包好的離線資源皆存放於 `~/Windows_AI_Offline_Pack/`，總容量已優化至約 6GB，完美適用於 32GB 隨身碟。
*   `models/Breeze-ASR-25/`：聯發科研發的語音辨識模型 (約 3GB，已清除訓練用紀錄檔)。
*   `models/whisper-large-v3/`：OpenAI 的語音辨識模型 (約 3GB，已清除贅餘的 FP32 與非 PyTorch 版本)。
*   `models/chandra/`：手寫辨識模型 (約 16MB)。
*   `packages/`：Windows 64位元專用的 Python 3.10 離線依賴套件檔 (`.whl`)，包含 PyTorch (2.6GB) 等。
*   `translator_packages/`：Windows 專用 OCR 與翻譯組件包 (含 Pillow, winrt-windows-* 系列, deep-translator 等)。
*   `officecli-win-x64.exe`：Office 快速排版生成工具的 Windows 版執行檔。
*   `python-3.10.11-amd64.exe`：供目標 Windows 電腦離線安裝的 Python 官方執行檔。

*註：有幾個 winrt 組件已應使用者要求，存放於 Google Drive 的 `搬運工碼頭` 資料夾中。*

## 3. 使用者偏好與特殊設定 (User Rules)
1.  **語言與用字：** 回答請強制使用繁體中文（台灣用語）。
2.  **安裝原則：** 以後安裝軟體優先尋找官方預先編譯好的二進制檔案 (Binary) 或釋出版本 (Release)，絕對不要用 Homebrew 從頭編譯原始碼。
3.  **工程標準：** 修改或提交代碼前，必須執行包含所有核心功能的全功能測試，確保無邏輯斷點或執行錯誤。

## 4. 下一步計畫
1.  使用者將透過隨身碟將 `Windows_AI_Offline_Pack` 轉移至目標 Windows 電腦。
2.  在 Windows 端進行離線環境建置 (`pip install --no-index --find-links .`)。
3.  撰寫串接腳本，將 OCR、Whisper/Breeze、以及 OfficeCLI 整合為一鍵生成講義的自動化流程。

> [!IMPORTANT]
> 給新的 Antigravity 視窗版 Agent：請讀取此文件後，向使用者打聲招呼，表示您已完全掌握先前的所有進度與檔案位置，並準備好協助後續的 Windows 部署腳本撰寫！
