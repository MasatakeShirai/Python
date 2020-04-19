'''
PDFの作成
ReportLabライブラリ
 データをPDFとして生成したいとき，
 個別に手動で作成する方法とHTMLやXMLなどのマークアップ言語を読み取って自動生成する方法がある
 前者の方法を解説する
'''
import os
os.chdir('chap20')

#もっとも簡単なPDF出力例
from reportlab.pdfgen import canvas
# PDFドキュメントのオブジェクトを生成
c = canvas.Canvas('helloworld.pdf')
# 文章を記述（x座標, y座標, 文章）
c.drawString(100, 500, "Helloworld!")
c.save()

#日本語を利用
from reportlab.pdfbase.cidfonts import UnicodeCIDFont
from reportlab.pdfbase import pdfmetrics

c = canvas.Canvas('fonts.pdf')

fontname_g = "HeiseiKakuGo-W5"
pdfmetrics.registerFont(UnicodeCIDFont(fontname_g))

fontname_m = "HeiseiMin-W3"
pdfmetrics.registerFont(UnicodeCIDFont(fontname_m))

c.setFont(fontname_g, 30)
c.drawString(0, 700, "ゴシック体です")

c.setFont(fontname_m, 30)
c.drawString(0, 650, "明朝体です")

c.save()

#シンプルなドキュメント作成
from reportlab.rl_config import defaultPageSize
FONT_NAME = 'HeiseiKakuGo-W5'
FONT_SIZE = 20

canvas = canvas.Canvas('simple.pdf')
canvas.setFont(FONT_NAME, FONT_SIZE)

PAGE_WIDTH = defaultPageSize[0]
PAGE_HIGHT =defaultPageSize[1]

canvas.drawString(0, PAGE_HIGHT-FONT_SIZE, "左上に出力されます")
canvas.line(0, 0, PAGE_HIGHT, PAGE_WIDTH)
canvas.rect(50,100,200,300)
canvas.circle(PAGE_WIDTH/2, PAGE_HIGHT/2, 100) 

canvas.save()

#テンプレートを使ったドキュメント作成
from reportlab.platypus import BaseDocTemplate, PageTemplate, Frame, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle

FONT_NAME = 'HeiseiKakuGo-W5'
FONT_SIZE = 20

pdfmetrics.registerFont(UnicodeCIDFont(FONT_NAME))

doc = BaseDocTemplate(
    'template.pdf',
    leftMargin = 0,
    rightMargin = 0,
    topMargin = 0,
    bottomMargin = 0,
)

frame = Frame(
    20,
    20,
    width=doc.width -40,
    height=doc.height -40,
    id="myframe",
    showBoundary=True,
)

page = PageTemplate(id="mypage",frames=[frame])

doc.addPageTemplates([page])

title_style = ParagraphStyle(
    name='Title',
    fontName = FONT_NAME,
    fontsize = 18,
    leading = 22,
    spaceAfter = 6,
)

normal_style = ParagraphStyle(
    name='Normal',
    fontName=FONT_NAME,
    fontSize=10,
    leading=12,
)

story=[
    Paragraph("桃太郎",title_style),
    Paragraph("昔々あるところに，おじいさんとおばあさんが住んでいました．", normal_style),
    Paragraph("おじいさんは山へ芝刈りに，おばあさんも山へ芝刈りに行きました．", normal_style),
    Spacer(1,10),
    Paragraph("めでたし，めでたし．", normal_style)    
]

doc.build(story)

#生成した画像ファイルを削除
import re
pattearn = re.compile('pdf')
for fname in os.listdir():
    if pattearn.search(fname) is not None:
        os.remove(fname)
