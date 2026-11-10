const fs = require('fs');
const path = require('path');

const filePath = '/Users/mac/GeminiCli/Book-of-Fate/liuren_database/六壬大全_卷01_理論篇_古今對照.json';

function splitKeGe() {
    if (!fs.existsSync(filePath)) return;

    const db = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    let newData = [];
    let hasModified = false;

    db.data.forEach(item => {
        // 尋找包含 65 課格總覽的條目
        if (item.modern && item.modern.includes("六十五種課格的名稱與簡要定義歌訣")) {
            hasModified = true;
            console.log("Found KeGe overview, splitting...");

            // 保留原本的條目，但可以縮減或保留作為總覽
            newData.push({
                structure: item.structure,
                ancient: item.ancient,
                modern: item.modern.split('1. 元首課')[0].trim() + "\n（各課格詳細定義已拆分為獨立條目）"
            });

            // 解析白話文中的 65 項條目
            const lines = item.modern.split('\n');
            lines.forEach(line => {
                const match = line.match(/^\d+\.\s+([^:]+):\s+(.*)$/);
                if (match) {
                    const kegeName = match[1].trim();
                    const kegeDesc = match[2].trim();
                    
                    // 為了能在 ancient 中也匹配到，嘗試從 ancient 中提取對應的句子 (簡單匹配)
                    let ancientDesc = "";
                    const ancientLines = item.ancient.split('\n');
                    const ancientMatch = ancientLines.find(al => al.includes(kegeName.replace('課', '')));
                    if (ancientMatch) {
                        ancientDesc = ancientMatch.trim();
                    }

                    newData.push({
                        structure: ["課目 (六十四課格名稱)", kegeName],
                        term: kegeName,
                        ancient: ancientDesc || '見《六壬大全》卷七至卷十課經詳解。',
                        modern: `**${kegeName}**：\n${kegeDesc}`
                    });
                }
            });
        } else {
            newData.push(item);
        }
    });

    if (hasModified) {
        db.data = newData;
        fs.writeFileSync(filePath, JSON.stringify(db, null, 2));
        console.log("Splitting complete. File updated.");
    } else {
        console.log("No KeGe overview found to split.");
    }
}

splitKeGe();
