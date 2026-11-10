const fs = require('fs');
const path = require('path');

const srcDir = '/Users/mac/GeminiCli/命理/六壬/四庫全書六壬大全/古今對照MD版';
const destDir = '/Users/mac/GeminiCli/Book-of-Fate/liuren_database';

/**
 * 終極六壬 MD 轉 JSON 解析器 v4.0 - 內容合併版
 * 解決「原文與白話被標題分割」的問題，確保同一術語內容完整。
 */
function parseLiurenMD(content) {
    const lines = content.split('\n');
    let title = '';
    const data = [];
    
    let currentStructure = [];
    let currentAncient = [];
    let currentModern = [];
    let state = 'ANCIENT'; 

    lines.forEach(line => {
        let trimmed = line.trim();
        if (!trimmed) return;
        
        // 優先過濾掉 Markdown 的引用符號，確保後續的 ^ 正則能正確匹配
        trimmed = trimmed.replace(/^>\s*/, '').trim();

        // 檢測標題 (#)
        const headerMatch = trimmed.match(/^(#+)\s+(.*)$/);
        if (headerMatch) {
            const level = headerMatch[1].length;
            const text = headerMatch[2].trim();
            
            if (level === 1) {
                title = text;
            } else {
                // 重要：判斷標題是否只是「狀態標籤」
                const isTagHeader = /原文|白話|翻譯|解說|對照/.test(text) && text.length < 10;
                
                if (isTagHeader) {
                    // 切換狀態，但不執行存檔 (Flush)
                    if (text.includes('原文')) state = 'ANCIENT';
                    else state = 'MODERN';
                } else {
                    // 這是一個「結構性標題」(例如：元首課、河魁)
                    // 執行存檔之前的內容
                    if (currentAncient.length > 0 || currentModern.length > 0) flush();
                    
                    // 更新目錄結構
                    currentStructure[level - 2] = text;
                    currentStructure = currentStructure.slice(0, level - 1);
                    state = 'ANCIENT'; // 新標題下通常先出現原文
                }
            }
            return;
        }

        // 檢測顯式加粗標籤 (例如 **【原文】**, **原文**, **翻譯**)
        const ancientMatch = trimmed.match(/^\*\*【?(原文|古籍原文)】?\*\*/);
        if (ancientMatch) {
            state = 'ANCIENT';
            const extra = trimmed.replace(/^\*\*【?(原文|古籍原文)】?\*\*/, '').replace(/^[:：]/, '').trim();
            if (extra) currentAncient.push(extra);
            return;
        }
        const modernMatch = trimmed.match(/^\*\*【?(白話.*?|翻譯|現代白話)】?\*\*/);
        if (modernMatch) {
            state = 'MODERN';
            const extra = trimmed.replace(/^\*\*【?(白話.*?|翻譯|現代白話)】?\*\*/, '').replace(/^[:：]/, '').trim();
            if (extra) currentModern.push(extra);
            return;
        }

        // 收集內容
        const cleanLine = trimmed.replace(/^>\s*/, '').trim();
        if (state === 'ANCIENT') {
            currentAncient.push(cleanLine);
        } else if (state === 'MODERN') {
            currentModern.push(cleanLine);
        }
    });

    flush();

    function flush() {
        if (currentAncient.length > 0 || currentModern.length > 0) {
            data.push({
                structure: [...currentStructure.filter(s => s)],
                ancient: currentAncient.join('\n').trim(),
                modern: currentModern.push ? currentModern.join('\n').trim() : ''
            });
            currentAncient = [];
            currentModern = [];
        }
    }

    return { title, data };
}

if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });

fs.readdirSync(srcDir).forEach(file => {
    if (file.endsWith('.md') && file !== 'index.md') {
        console.log(`Deep Merging ${file}...`);
        const content = fs.readFileSync(path.join(srcDir, file), 'utf8');
        const result = parseLiurenMD(content);
        fs.writeFileSync(path.join(destDir, file.replace('.md', '.json')), JSON.stringify(result, null, 2));
    }
});

console.log('Database Data Integrity Fully Restored (v4.0).');
