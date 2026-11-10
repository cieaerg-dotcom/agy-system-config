const fs = require('fs');
const path = require('path');

const srcDir = '命理/六壬/六壬大全_分卷/MD檔/古今對照版';
const destDir = '命理/六壬/六壬大全_分卷/JSON檔/古今對照版';

if (!fs.existsSync(destDir)) {
    fs.mkdirSync(destDir, { recursive: true });
}

function parseMarkdown(content) {
    const lines = content.split('\n');
    let title = '';
    let intro = '';
    const entries = [];
    
    let currentHeaders = [];
    let state = 'NONE'; // NONE, ORIGINAL, TRANSLATION
    let currentOriginal = [];
    let currentTranslation = [];

    lines.forEach(line => {
        const trimmed = line.trim();
        
        // Match Header
        const headerMatch = trimmed.match(/^(#+)\s+(.*)$/);
        if (headerMatch) {
            const level = headerMatch[1].length;
            const text = headerMatch[2].trim();
            
            if (level === 1) {
                title = text;
            } else if (text === '原文' || text === '白話翻譯' || text.includes('速查表解讀')) {
                // If we hit a functional header, change state
                if (text === '原文') {
                    // If we were already in a pair, we might need to flush (though usually Translation follows Original)
                    flushPair();
                    state = 'ORIGINAL';
                } else if (text === '白話翻譯') {
                    state = 'TRANSLATION';
                }
            } else {
                // Regular structural header
                flushPair();
                state = 'NONE';
                // Adjust header stack
                currentHeaders = currentHeaders.slice(0, level - 2);
                currentHeaders[level - 2] = text;
            }
            return;
        }

        if (state === 'ORIGINAL') {
            if (trimmed.startsWith('>')) {
                currentOriginal.push(trimmed.replace(/^>\s?/, ''));
            } else if (trimmed !== '' && !trimmed.startsWith('---')) {
                currentOriginal.push(trimmed);
            }
        } else if (state === 'TRANSLATION') {
            if (trimmed.startsWith('>')) {
                currentTranslation.push(trimmed.replace(/^>\s?/, ''));
            } else if (trimmed !== '' && !trimmed.startsWith('---')) {
                currentTranslation.push(trimmed);
            }
        } else if (state === 'NONE' && title && !trimmed.startsWith('---') && trimmed !== '') {
            if (entries.length === 0 && currentHeaders.length === 0) {
                intro += trimmed + '\n';
            }
        }
    });

    flushPair();

    function flushPair() {
        if (currentOriginal.length > 0 || currentTranslation.length > 0) {
            entries.push({
                headers: [...currentHeaders.filter(h => h)],
                original: currentOriginal.join('\n').trim(),
                translation: currentTranslation.join('\n').trim()
            });
            currentOriginal = [];
            currentTranslation = [];
        }
    }

    return {
        title,
        introduction: intro.trim(),
        entries
    };
}

fs.readdirSync(srcDir).forEach(file => {
    if (file.endsWith('.md')) {
        console.log(`Processing ${file}...`);
        const content = fs.readFileSync(path.join(srcDir, file), 'utf8');
        const result = parseMarkdown(content);
        const jsonFileName = file.replace('.md', '.json');
        fs.writeFileSync(path.join(destDir, jsonFileName), JSON.stringify(result, null, 2));
    }
});

console.log('Done.');
