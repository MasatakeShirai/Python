#インスタンスにかかわる文法
# インスタンスの生成
# クラス宣言．すべてのクラスは'object'を根底に継承する
# 構文　class クラス名(継承元のクラス名)
class Shape(object):
    pass
# インスタンス生成
# 構文　インスタンス = クラス名()
shape = Shape()

#インスタンスの属性
# 個々のインスタンスで保持する属性をインスタンス属性と呼ぶ
# 属性はオブジェクトにピリオドで紐づくもの
# 最初に_がつくものを慣例的にプライベート属性として扱う．
# 両端に__がつくものはシステムで内部的に扱われる
shape1 = Shape()
shape2 = Shape()
shape1.position = 3
shape2.position = 4
print((shape1.position, shape2.position))

#インスタンスのメソッド
import random
class Shape(object):
    #インスタンス・メソッド内のselfはインスタンス自身を指す
    # メソッドの第1引数はself，第2引数にはインスタンス生成時に渡した引数と対応する
    # 第1引数のselfは省略できない
    def set_random_position(self, bound):
        self.position = bound * random.random()

shape = Shape()
shape.set_random_position(3)
print(shape.position)

#特殊メソッド
# コンストラクタ
class Shape(object):
    #コンストラクタの定義
    def __init__(self, width):
        self.width = width

#コンストラクタが呼び出される
shape = Shape(3)
print(shape.width)

#プロパティ
# プロパティはいわゆるゲッタやセッタのインスタンス・メソッドを使って
# インスタンス属性を扱っているように見せる属性
class Shape(object):
    def _get_color(self):
        return tuple(v * 255.0 for v in self._rgb)
    def _set_color(self, rgb):
        self._rgb = tuple(v/255.0 for v in rgb)
    color = property(_get_color, _set_color)

shape = Shape()
#0-255のRGBで設定
shape.color = (255, 0, 0)
#0-255のRGBを参照
print(shape.color)
#内部的には0-1で保持
print(shape._rgb)