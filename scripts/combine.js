const fs = require('fs');
const path = require('path');

const folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026風尚之旅";
const files = fs.readdirSync(folder);

const mdFiles = files.filter(f => f.endsWith('.md') && f.includes('_part'));
const groups = {};

mdFiles.forEach(f => {
    const match = f.match(/^(錄音 \d+)_part\d+\.md$/);
    if (match) {
        const base = match[1];
        if (!groups[base]) groups[base] = [];
        groups[base].push(f);
    }
});

for (const base in groups) {
    const paths = groups[base].sort();
    let combinedText = "";
    paths.forEach(p => {
        combinedText += fs.readFileSync(path.join(folder, p), 'utf-8') + "\n";
        fs.unlinkSync(path.join(folder, p)); // delete md part
        
        const audioPart = p.replace('.md', '.m4a');
        if (fs.existsSync(path.join(folder, audioPart))) {
            fs.unlinkSync(path.join(folder, audioPart)); // delete m4a part
        }
    });
    fs.writeFileSync(path.join(folder, base + '.md'), combinedText, 'utf-8');
}

console.log("Combined successfully");
