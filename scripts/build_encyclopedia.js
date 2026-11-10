const fs = require('fs');
const path = require('path');

const srcDir = '/Users/mac/GeminiCli/Book-of-Fate/liuren_database';
const outputFile = path.join(srcDir, 'liuren_encyclopedia.json');

function buildEncyclopedia() {
    const files = fs.readdirSync(srcDir).filter(f => f.endsWith('.json') && f !== 'index.json' && f !== 'liuren_encyclopedia.json');
    let encyclopedia = [];
    let idCounter = 1;

    files.forEach(file => {
        const dbPath = path.join(srcDir, file);
        const db = JSON.parse(fs.readFileSync(dbPath, 'utf8'));

        if (db.data && Array.isArray(db.data)) {
            db.data.forEach(item => {
                const term = item.term || (item.structure && item.structure.length > 0 ? item.structure[item.structure.length - 1] : "未命名");
                const fullText = `${item.structure ? item.structure.join(' ') : ''} ${item.ancient || ''} ${item.modern || ''}`.replace(/\n/g, ' ');
                
                encyclopedia.push({
                    id: idCounter++,
                    term: term,
                    category: file.includes('神煞') ? '神煞' : 
                              file.includes('十二將') ? '十二將' :
                              file.includes('十二神') ? '十二神' :
                              file.includes('課經') ? '課經' :
                              file.includes('畢法') ? '畢法' : '一般知識',
                    path: item.structure ? ` > ${item.structure.join(' > ')}` : '',
                    ancient: item.ancient,
                    modern: item.modern,
                    source: file.replace('.json', ''),
                    full_text: fullText
                });
            });
        }
    });

    fs.writeFileSync(outputFile, JSON.stringify(encyclopedia, null, 2));
    console.log(`Successfully built liuren_encyclopedia.json with ${encyclopedia.length} entries.`);
}

buildEncyclopedia();
