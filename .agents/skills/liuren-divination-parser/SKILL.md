---
name: liuren-divination-parser
description: >-
  Parses, aligns, and converts classical Da Liu Ren (大六壬) divination Markdown documents into clean, structured JSON databases, resolving ancient text and modern vernacular translation alignments.
---

# 大六壬命理文獻解析與結構化技能 (Liu Ren Divination Parser)

本技能提供標準化流程，用於將《四庫全書六壬大全》等古典大六壬典籍的 Markdown 筆記，精確解析為結構化 JSON 資料庫，供 `Book-of-Fate` 排盤系統與課體推演直接引用。

## 核心功能與特色

- **古今雙語對照合併**：自動解決「原文」與「白話翻譯」被標題切斷的問題，將同一術語、課體（如元首課、涉害課）與神煞的古今內容自動關聯為同一 JSON 物件。
- **階層標題解析**：自動識別章節層級、課體類別與細部斷語。

## 執行方式

執行內建 Node.js 解析腳本：

```bash
node .agents/skills/liuren-divination-parser/scripts/universal_liuren_parser.js
```

### 驗證與測試原則（依據 GEMINI.md 規範）
修改或執行本技能的代碼前，必須執行全功能測試，確保排盤、格局判斷與課體輸出無邏輯斷點或資料結構錯誤。
