#継承
# 既存のクラスから属性を受け継いで，それらを変更・拡張したクラスを定義できる
class Shape(object):
    def __init__(self,width):
        self.width = width
    def calculate_area(self):
        return 0
    
class Square(Shape):
    def calculate_area(self):
        return self.width**2

class Circle(Shape):
    def calculate_area(self):
        import math
        return (self.width/2)**2*math.pi

# コンストラクタはSquare, Circle共に親であるShapeの__init__を使っている
# 一方calculate_areaメソッドはそれぞれで挙動が異なる
square = Square(2)
print(square.calculate_area())

circle = Circle(2)
print(circle.calculate_area())

#インスタンスの判定指定したオブジェクトがそのインスタンスであるかを判定するにはisinstance関数を用いる
# あるクラスのインスタンスは継承元のインスタンスにもなる
print(isinstance(circle, Shape))
print(isinstance(square, Shape))
print(isinstance(square, Circle))

#継承元メソッド呼び出し
# 継承元のメソッドを呼び出すにはsuper関数を用いる
class BorderedShape(Shape):
    def __init__(self, width, border):
        #super関数で継承元の__init__メソッドを呼び出す
        super().__init__(width)
        self.border = border

borderedshape = BorderedShape(3,1)
print((borderedshape.width, borderedshape.border))

#抽象メソッドについて
# 組み込みで用意されてはいないが，標準モジュールabcで再現できる
import abc
class Shape(object, metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        return
#抽象メソッドが実装されていないとエラーになる
# TypeError: Can't instantiate abstract class Square with abstract methods calculate_area
#class Square(Shape):
#    pass

#多重継承
# Pythonでは複数のクラスから継承する多重継承ができる
# 利用しやすいのは，初期化目的ではなく機能追加目的であるMixin
class AreaCmpMixin(object):
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()
    
    def __lt__(self, other):
        return self.calculate_area() < other.calculate_area()

class AreaComparableCircle(AreaCmpMixin, Circle):
    pass

circle1 = AreaComparableCircle(3)
circle2 = AreaComparableCircle(4)
print(circle1.width)
print(circle2.width)
print(circle1 == circle2)
print(circle1 < circle2)

#継承順の表示
# 多重継承では__mro__メソッドで継承順を確認できる
import pprint
pprint.pprint(AreaComparableCircle.mro())
