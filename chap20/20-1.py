#画像の作成
'''
PILライブラリ
Pythonで画像編集をするときはPILライブラリを使うのが一般的
'''
#セットアップ
# easy_installでインストールした場合とソースからインストールした場合はモジュールの位置が異なる
from PIL import Image

import os
os.chdir('chap20')

#基本的な処理
# 編集したい画像パスを指定し，PILオブジェクトを生成
image = Image.open('Lenna.jpg')
# オブジェクトに対して編集を行う
image = image.resize([256,256])
image.save('jane.jpg')

#基本的なエラー処理
# 以下の状況でopen時にIOErrorが発生する
# ・画像ではないファイルを読み込んだ時
# ・PILが対応できないフォーマットの時
# ・ファイルが存在しない時
try:
    image = Image.open('memo.txt')
except IOError:
    print('IOError')

#画像フォーマット変更
# 拡張子から自動的にフォーマットを判定して変換する．
# 明示的に指定することも可能
image.save('jane.png')
image.save('jane.gif')

#カラーモード変更
print(image.mode)
image = image.convert('P')
print(image.mode)
image.save('jane.png')

#拡大・縮小
image = Image.open('Lenna.jpg')
big = image.resize((400, 400))
big.save('bigjane.jpg')
small = image.resize((50, 50))
small.save('smalljane.jpg')
 
#回転
image = Image.open('Lenna.jpg')
rotate = image.rotate(45)
rotate.save('lotatejane.jpg')

#反転
image = Image.open('Lenna.jpg')
left_right = image.transpose(Image.FLIP_LEFT_RIGHT)
left_right.save('left-right_jane.jpg')

image = Image.open('Lenna.jpg')
top_bottom = image.transpose(Image.FLIP_TOP_BOTTOM)
top_bottom.save('top-bottom_jane.jpg')

#切り張り
image = Image.open('Lenna.jpg')
part = image.crop([0,0,128,64])
left_right.save('left-right_jane.jpg')
image.paste(part, (0,64,128,128))
image.save('cutedjane.jpg')

#透過画像に加工して貼り付け
surface = Image.open('Lenna.jpg')
background =Image.open('Lenna.jpg')
surface = surface.crop([32,32,96,96])
surface_mask = Image.new('L', surface.size, 128)
background.paste(surface, (0,0,64,64), mask=surface_mask)
background.save('maskedjane.jpg')

#透過PNGを重ねる
background = Image.open('Lenna.jpg')
surface = Image.open('top-bottom_jane.jpg')
surface = surface.resize([128,128])
surface_mask = surface.split()[2]
background.paste(surface,[0,0,128,128],mask=surface_mask)
background.save('doublejane.jpg')

#描画する
from PIL import ImageDraw
image = Image.open('Lenna.jpg')
draw = ImageDraw.Draw(image)
draw.rectangle([16,16,48,48], "#FF0000")
draw.pieslice([80,80,112,112], 0, 360, "#00FF00")
draw.line([0,128,128,0], "#0000FF")
image.save('drawedjane.jpg')

#フィルタをかける
from PIL import ImageFilter
image = Image.open('Lenna.jpg')
image = image.filter(ImageFilter.BLUR)
image.save('filteredjane.jpg')

#画質の調整
from PIL import ImageEnhance
image = Image.open('Lenna.jpg')
image = ImageEnhance.Brightness(image)
image = image.enhance(2.0)
image.save('enhancedjane.jpg')

#モノクロ画像生成と白黒反転
image = Image.open('Lenna.jpg')
# モノクロ化
image = image.convert('L')
image.save('convertedjane.jpg')

# 白黒反転
def reverser(i):
    return 255 - i

image = image.point(reverser)
image.save('reversedjane.jpg')

#生成した画像ファイルを削除
import re
pattearn = re.compile('jane')
for fname in os.listdir():
    if pattearn.search(fname) is not None:
        os.remove(fname)
