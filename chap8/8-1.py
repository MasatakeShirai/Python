#条件分岐
#if-then-else
a=1
if a>0:
    print(True)
else:
    print(False)

#else-ifパート
# 複数条件を評価する場合は，elifを使う
n=5
if n<0:
    print('n<0')
elif n==0:
    print('n==0')
elif n==5:
    print('n==5')
elif n<10:
    print('n<10')
else:
    print('else')

#条件式
#無や負に相当するものはfalse,1や実体の存在するものはtrueになる
print(bool(''))
print(bool('python'))
print(bool(1))
print(bool(0))

if '':
    print('HELLO')

if 'python':
    print('hello')

#論理演算子
#and,or,notがあり，優先度はnot>and>or.
# orは先にTrueの評価が行われた時点でTrueを返す．
# andは先にfalseの評価が行われた時点でfalseを返す．
print(bool('' or 0 or 1 or False or []))
print(bool(1 and [1,2,3] and 0 and True and 'python'))

#三項演算子 
# 構文：成功した時の値 if 条件式 else 失敗した時の値
#用いない場合
py='python'
if py=='python':
    ans='Hello.py'
else:
    ans='goodby'
print(ans)

#用いる場合
print('Hello.py' if py=='python' else 'goodby')