import os, re

folder = "/Users/mac/Google Drive/我的雲端硬碟/賀寶芙/2026一月風尚之旅逐字稿"

rename_map = {
    "錄音 22.md": "錄音_022_完整中文版_GarySmall博士_健康老化與營養.md",
    "錄音 24.md": "錄音_024_完整中文版_護理師_產品的科學根基.md",
    "錄音 25.md": "錄音_025_完整中文版_體重管理分享者_減重與體態改變見證.md",
    "錄音 27.md": "錄音_027_完整中文版_辛雅博士_第一天活動回顧.md",
    "錄音 28.md": "錄音_028_完整中文版_江有為_服飾店老闆的賀寶芙故事.md",
    "錄音 29.md": "錄音_029_完整中文版_夥伴見證_營養與運動改變體態.md",
    "錄音 30.md": "錄音_030_完整中文版_年輕夥伴_改善健康與社交能力.md",
    "錄音 31.md": "錄音_031_完整中文版_助人夥伴_尋找有價值的工作.md",
    "錄音 32.md": "錄音_032_完整中文版_婷婕與彥浩_夫妻經營分享.md",
    "錄音 33.md": "錄音_033_完整中文版_韋翔與漾_傳統業老闆的翻轉人生.md",
    "錄音 34.md": "錄音_034_完整中文版_大會夫妻講者_選擇大於努力的故事.md",
    "錄音 35.md": "錄音_035_完整中文版_前醫護人員_從醫護到賀寶芙的轉變.md",
    "錄音 36.md": "錄音_036_完整中文版_新科總裁_晉升表揚與感恩.md",
    "錄音 37.md": "錄音_037_完整中文版_婕宇_夥伴見證.md",
    "錄音 38.md": "錄音_038_完整中文版_總裁組_總裁演講.md",
    "錄音 39.md": "錄音_039_完整中文版_高階領袖_快速晉升總裁組的故事.md",
    "錄音 40.md": "錄音_040_完整中文版_Xia_大會晚間演說.md",
    "錄音 41.md": "錄音_041_完整中文版_主席俱樂部講者_看見未來與熱情.md",
}

def is_ascii(char):
    return ord(char) < 128

def join_lines(lines):
    res = ""
    for i, line in enumerate(lines):
        if i == 0:
            res += line
        else:
            if res and line and is_ascii(res[-1]) and is_ascii(line[0]) and res[-1].isalnum() and line[0].isalnum():
                res += " " + line
            else:
                res += line
    return res

def format_mobile_friendly(text):
    lines = text.split('\n')
    paragraphs = []
    current_para = []
    current_len = 0
    
    for line in lines:
        line = line.strip()
        if not line:
            if current_para:
                paragraphs.append(join_lines(current_para))
                current_para = []
                current_len = 0
            continue
            
        if line.startswith('#'):
            if current_para:
                paragraphs.append(join_lines(current_para))
                current_para = []
                current_len = 0
            paragraphs.append(line)
            continue
            
        # Bold speakers if it matches Pattern "Name: " or "Name："
        line = re.sub(r'^([^：:]{2,10})([：:])', r'**\1**\2', line)
            
        current_para.append(line)
        current_len += len(line)
        
        # Break paragraph if it ends with punctuation and is long enough
        if current_len > 100 and line[-1:] in ['。', '！', '？', '!', '?', '”', '"']:
            paragraphs.append(join_lines(current_para))
            current_para = []
            current_len = 0

    if current_para:
        paragraphs.append(join_lines(current_para))

    return '\n\n'.join(paragraphs) + '\n'

for old_name, new_name in rename_map.items():
    old_path = os.path.join(folder, old_name)
    new_path = os.path.join(folder, new_name)
    
    if os.path.exists(old_path):
        with open(old_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        formatted_content = format_mobile_friendly(content)
        
        with open(new_path, 'w', encoding='utf-8') as f:
            f.write(formatted_content)
            
        os.remove(old_path)
        print(f"Processed and renamed {old_name} to {new_name}")
    else:
        print(f"File not found: {old_name}")
