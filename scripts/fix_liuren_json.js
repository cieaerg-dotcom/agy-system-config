const fs = require('fs');
const path = require('path');

const srcDir = '/Users/mac/GeminiCli/命理/六壬/四庫全書六壬大全/古今對照MD版';
const destDir = '/Users/mac/GeminiCli/Book-of-Fate/liuren_database';

function parseLiurenMD(content) {
    const lines = content.split('\n');
    let title = '';
    const data = [];
    
    let currentStructure = [];
    let currentOriginal = [];
    let currentModern = [];
    let state = 'NONE'; 

    lines.forEach(line => {
        const trimmed = line.trim();
        if (!trimmed && state === 'NONE') return;

        // Match Header
        const headerMatch = trimmed.match(/^(#+)\s+(.*)$/);
        if (headerMatch) {
            const level = headerMatch[1].length;
            const text = headerMatch[2].trim();
            if (level === 1) {
                title = text;
            } else {
                flushPair();
                state = 'NONE';
                // Adjust structure
                currentStructure[level - 2] = text;
                currentStructure = currentStructure.slice(0, level - 1);
            }
            return;
        }

        if (trimmed.includes('**【原文】**')) {
            flushPair();
            state = 'ORIGINAL';
            return;
        } else if (trimmed.includes('**【白話解說】**')) {
            state = 'MODERN';
            return;
        }

        if (state === 'ORIGINAL') {
            if (trimmed !== '' && !trimmed.startsWith('---')) {
                currentOriginal.push(trimmed);
            }
        } else if (state === 'MODERN') {
            if (trimmed !== '' && !trimmed.startsWith('---')) {
                currentModern.push(trimmed);
            }
        }
    });

    flushPair();

    function flushPair() {
        if (currentOriginal.length > 0 || currentModern.length > 0) {
            data.push({
                structure: [...currentStructure.filter(s => s)],
                ancient: currentOriginal.join('\n').trim(),
                modern: currentModern.join('\n').trim()
            });
            currentOriginal = [];
            currentModern = [];
        }
    }

    return { title, data };
}

if (!fs.existsSync(destDir)) fs.mkdirSync(destDir, { recursive: true });

const files = fs.readdirSync(srcDir);
files.forEach(file => {
    if (file.endsWith('.md') && file !== 'index.md') {
        console.log(`Converting ${file}...`);
        const content = fs.readFileSync(path.join(srcDir, file), 'utf8');
        const result = parseLiurenMD(content);
        fs.writeFileSync(path.join(destDir, file.replace('.md', '.json')), JSON.stringify(result, null, 2));
    }
});
console.log('Done.');
