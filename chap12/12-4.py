#デコレーター関数
# 定義時に，関数を修飾して新たな関数を作り出す．
# 複数の関数に共通する処理を書きたいとき，デコレーターを用いると簡潔で可読性の高いコードをかける

#基本文法
# デコレーターは関数を受け取り，修飾した関数を返す関数
# 構文  @デコレーター名(引数 ...)

#デコレーターの定義
# 引数として受け取った関数(オブジェクト)に対して属性xを定義し，1を代入する
def decorate(f):
    f.x = 1
    return f

#デコレーターと共に定義しているので，func関数の属性値xには1が代入される
@decorate
def func():
    pass

print(func.x)

#デコレーター関数内で新たに関数を定義する
def add_one(f):
    def new_f(*args, **kwds):
        result = f(*args, **kwds)
        return result + 1
    return new_f

@add_one
def func():
    return 3

print(func())

#デコレーターに引数を指定する
# "関数を受け取り，修飾した関数を返す関数"を返す
def multiple(x):
    def _multiple(f):
        def new_f(*args, **kwds):
            result = f(*args, **kwds)
            return result * x
        return new_f
    return _multiple

@multiple(2)
def func():
    return 3

print(func())

#デコレーターのネスト
# (3+1)*2になる
@multiple(2)
@add_one
def func():
    return 3
print(func())
