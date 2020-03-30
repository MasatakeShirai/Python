#関数オブジェクト
# Pythonでは関数を制限のないオブジェクトとして利用できる
def square(x):
    return x**2
print(square)
# （）をつけることで関数を実行できる
print(square(3))

# オブジェクトなので，引数としても利用できる
def distance(x,y,func):
    print(func)
    return func(x-y)    
print(distance(2,1,square))

# 関数の中で関数を定義することも可能
def func():
    def inner_func():
        pass
    print(inner_func)
func()

# 無名関数（ラムダ式）
# 構文　lambda 引数 : 戻り値
# lambda構文を使うと無名の関数オブジェクトが作成される 
print(distance(3,1,lambda x : x**2))