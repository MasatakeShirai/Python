def say_hello():
    print('hello')

#キーに関数を指定
a = {say_hello:'This is function!'}
print(a[say_hello])

#辞書型で関数の呼び出し
a = {'call function test':say_hello}
a['call function test']()

#キーが存在するか判定
print('call function test' in a)

#キーの削除
del a['call function test']
print(a)