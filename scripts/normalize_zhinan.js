const fs = require('fs');
const path = require('path');

const dir = '/Users/mac/GeminiCli/Book-of-Fate/liuren_database/';

function normalize(fileName) {
    const filePath = path.join(dir, fileName);
    if (!fs.existsSync(filePath)) return;

    const raw = JSON.parse(fs.readFileSync(filePath, 'utf8'));
    if (!raw.chapters) return;

    const normalizedData = [];
    raw.chapters.forEach(ch => {
        normalizedData.push({
            structure: [ch.title],
            ancient: (ch.content || []).join('\n'),
            modern: "" // 指南系列多為原文，無古今對照版
        });
    });

    const result = {
        title: raw.title,
        data: normalizedData
    };

    fs.writeFileSync(filePath, JSON.stringify(result, null, 2));
    console.log(`Normalized ${fileName}`);
}

normalize('六壬指南.json');
normalize('六壬指南注解.json');
