#関数の戻り値
# 戻り値の指定はreturn文で行う
def distance(a,b):
    import math
    return math.sqrt((a[0]-b[0])**2 + (a[1]-b[1])**2)

print(distance((3,4), (0,0)))

#戻り値がないときはNoneになる
def func():
    pass

print(func())

#アンパック代入
# タプル型のオブジェクトを返す場合単純にやると，以下のようになる
def func():
    return (2,3)
r=func()
x=r[0]
y=r[1]
print(x,y)
# この時アンパック代入を使えば単純にかける
x, y = func()
print(x, y)
