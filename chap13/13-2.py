#クラスに係わる文法
#クラス属性
# クラス自体が保持する属性で，個々のインスタンス共有される．
# 例えば，変更するとすべてのインスタンスに反映される
class Shape(object):
    dimention = 1

shape1 = Shape()
shape2 = Shape()
print((shape1.dimention, shape2.dimention))
#まとめて変更される
Shape.dimention = 2
print((shape1.dimention, shape2.dimention))
#shape1のみ変更される
shape1.dimention = 3
print((shape1.dimention, shape2.dimention))

#クラスメソッドとスタティックメソッド
# クラスメソッドはメソッド内でクラス自身を参照できるメソッド
# スタティックメソッドはクラスの属性である以外はグローバルなメソッドと変わらない
class Shape(object):
    def __init__(self, width):
        self.width = width
    #クラスメソッドの定義
    # clsはクラス自身を指す
    @classmethod
    def create_from_text(cls, text):
        width = {'large':10, 'medium':3, 'small':1}[text]
        #コンストラクタに値をわたすことでインスタンスを作成する
        return cls(width)
    #スタティックメソッドの定義
    @staticmethod
    def get_golden_ratio(width):
        return (width, width/1.61803399)

shape = Shape.create_from_text('large')
print(shape.width)
print(Shape.get_golden_ratio(1.0))