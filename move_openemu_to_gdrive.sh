#!/bin/bash
# OpenEmu 遊戲庫搬移至 Google 雲端硬碟排程腳本
set -e

SOURCE_DIR="$HOME/Library/Application Support/OpenEmu"
TARGET_DIR="$HOME/Library/CloudStorage/GoogleDrive-cieaer.g@gmail.com/我的雲端硬碟/OpenEmu遊戲庫"
LOG_FILE="$HOME/Library/Logs/openemu_gdrive_move.log"

echo "==========================================" >> "$LOG_FILE"
echo "開始執行 OpenEmu 遊戲庫搬移: $(date)" >> "$LOG_FILE"
echo "來源: $SOURCE_DIR" >> "$LOG_FILE"
echo "目標: $TARGET_DIR" >> "$LOG_FILE"
echo "==========================================" >> "$LOG_FILE"

if [ ! -d "$SOURCE_DIR" ]; then
    echo "錯誤: 來源資料夾 $SOURCE_DIR 不存在！" >> "$LOG_FILE"
    exit 1
fi

if [ ! -d "$TARGET_DIR" ]; then
    mkdir -p "$TARGET_DIR"
fi

# 使用 rsync 增量傳輸，並在單檔傳輸成功後立即刪除本地來源檔（節省磁碟空間）
rsync -av --remove-source-files --progress "$SOURCE_DIR/" "$TARGET_DIR/" >> "$LOG_FILE" 2>&1

# 清理空目錄
find "$SOURCE_DIR" -type d -empty -delete 2>/dev/null || true

echo "==========================================" >> "$LOG_FILE"
echo "OpenEmu 遊戲庫搬移完成: $(date)" >> "$LOG_FILE"
echo "==========================================" >> "$LOG_FILE"
