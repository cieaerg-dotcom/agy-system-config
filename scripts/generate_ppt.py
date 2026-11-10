import collections 
import collections.abc
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor

# Create presentation
prs = Presentation()

# Slide 1: Title
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "健康陷阱？"
subtitle.text = "吃得好、吃得健康，熱量卻大大不同！\n\n專為減重班設計"

# Slide 2: 核心觀念
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "什麼是「熱量密度」？"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "同樣體積的食物，熱量卻天差地遠"
p = tf.add_paragraph()
p.text = "• 高熱量密度：吃一點點，熱量就超標 (例如：油脂、堅果)"
p.level = 1
p = tf.add_paragraph()
p.text = "• 低熱量密度：吃一大盤，熱量依然很低 (例如：蔬菜、原型清湯)"
p.level = 1
p = tf.add_paragraph()
p.text = "減重陷阱：為了「健康」吃很多高熱量密度的好食物，結果瘦不下來！"
p.level = 0

# Slide 3: 擂台一
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "殘酷擂台 1：解饞零食篇"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "綜合堅果 vs. 帶莢毛豆 (同樣 100g)"
p = tf.add_paragraph()
p.text = "綜合堅果 (100g) = 約 600 大卡"
p.level = 1
p = tf.add_paragraph()
p.text = "帶莢毛豆 (100g) = 約 116 大卡"
p.level = 1
p = tf.add_paragraph()
p.text = "💡 觀念：堅果很健康，但熱量等同兩個便當！想滿足咀嚼感，毛豆是高蛋白又低卡的首選。"
p.level = 0

# Slide 4: 擂台二
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "殘酷擂台 2：沙拉常客篇"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "酪梨 vs. 芭樂"
p = tf.add_paragraph()
p.text = "半顆酪梨 (100g) = 約 160 大卡 (都是油脂)"
p.level = 1
p = tf.add_paragraph()
p.text = "一整顆大芭樂 (300g) = 約 115 大卡 (高維生素C)"
p.level = 1
p = tf.add_paragraph()
p.text = "💡 觀念：酪梨在營養學上是「油脂」不是水果！想吃飽肚子，一顆芭樂完勝半顆酪梨。"
p.level = 0

# Slide 5: 擂台三
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "殘酷擂台 3：健康早餐篇"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "燕麥脆片(Granola) vs. 傳統大燕麥片"
p = tf.add_paragraph()
p.text = "燕麥脆片 (50g) = 約 230 大卡 (含糖與油)"
p.level = 1
p = tf.add_paragraph()
p.text = "傳統大燕麥片 (50g) = 約 185 大卡 (泡水後膨脹)"
p.level = 1
p = tf.add_paragraph()
p.text = "💡 觀念：好吃的脆片燕麥常藏著大量的糖漿與烘焙油。選擇無添加的原型大燕麥片，吸水膨脹才有飽足感。"
p.level = 0

# Slide 6: 神隊友
slide = prs.slides.add_slide(prs.slide_layouts[1])
title = slide.shapes.title
title.text = "如何聰明吃？3大秘訣"
body = slide.placeholders[1]
tf = body.text_frame
tf.text = "不是不能吃，而是要「控制份量」"
p = tf.add_paragraph()
p.text = "1. 脂肪要定量：堅果一天「一小把」，酪梨一天「四分之一顆」。"
p.level = 1
p = tf.add_paragraph()
p.text = "2. 改變烹調法：健康的食物也要用清蒸、水煮，避開高溫油煎炸。"
p.level = 1
p = tf.add_paragraph()
p.text = "3. 蔬菜打底法：餐前先吃一大碗蔬菜佔滿胃部，減少吃下高熱量密度食物的空間。"
p.level = 1

# Slide 7: 結語
slide = prs.slides.add_slide(prs.slide_layouts[0])
title = slide.shapes.title
subtitle = slide.placeholders[1]
title.text = "挑對好食物，\n更要吃對好份量！"
subtitle.text = "祝大家這週都吃得飽，又瘦得好！\n\nQ&A 時間"

# Save presentation
prs.save('/Users/mac/agy本地工作區/健康食物選擇簡報.pptx')
print('Presentation saved successfully.')
