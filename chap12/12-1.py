#関数の基本定義・呼び出し
def greet():
    print('Hello')
greet()

#一般的な引数
def greet2(target):
    print('Hello ', target)
greet2('python')

#複数の引数も渡せる
def greet3(target1, target2):
    print('Hello ', target1, ' ', target2)
greet3('python2','python3')

#引数を指定して渡すことができる
greet3(target2='python2', target1='python3')

#デフォルト値の指定
def greet4(target='World'):
    print('Hello ', target)
greet4()
greet4('python')

#シーケンス型の可変長引数
# 引数宣言の前にアスタリスクをつけると，複数の引数をタプル型として受け取る
def greet5(*tatgets):
    print('Hello ', ' '.join(tatgets))
greet5('python2', 'python3')
greet5()
#シーケンス型のオブジェクトを引数として渡したいときはアスタリスクをつける
greet5(*['pyhon2', 'python3'])

#辞書型の可変長引数
# 引数宣言の前にアスタリスクを2つつけると，キーワード付き引数を辞書型として受け入れる
def greet6(**options):
    if options.get('country') == 'jp':
        greeting = 'こんにちは'
    else:
        greeting = 'Hello'
    print(greeting, options.get('suffix', ' '))
greet6(country='jp', suffix='!')
greet6()
#辞書型のオブジェクトを引数として渡したいときはアスタリスクを2つつける
greet6(**{'country':'jp', 'suffix':'?'})

#引数の順番
# 一般的な引数，デフォルト値のある引数，シーケンス型の引数，辞書型の引数は同時にしてできる
# ただし指定するのは上の順番でなくてはいけない

#参照渡しと値渡し
# 基本的に参照渡しだが，変更不能オブジェクトの時は実質的に値渡しになる
def func(x):
    x.append(4)
x = [1,2,3]
print(x)
func(x)
print(x)
# 数，文字列，タプルは変更が反映されない
def func2(x):
    x+=1
x=3
print(x)
func2(x)
print(x)

#配列のデフォルト値について
# 引数のデフォルト値に配列を指定すると，関数内での更新がグローバルに聞いてしまう
def func3(x=[]):
    x.append(1)
    return x
print(func3())
print(func3())
# 配列をデフォルト値として扱いたいときは，
# デフォルト値をNoneとして，関数内でNoneの時に引数に初期配列を代入するとしたほうがいい
def func4(x=None):
    x = x or []
    x.append(1)
    return x
print(func4())
print(func4())
