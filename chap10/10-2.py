#文字列の作成
# 直接指定して"""作る
print('abc')
print("abc")
s="""abc
def
"""
print(s)

#row文字列はエスケープシーケンスを無視する
print(r'abc\ndef')

#フォーマット文字列を使う
print('%s is %s'%('Bob', 'Superman'))
print('%(name)s is %(featuer)s'%{'name':'Tom', 'featuer':'Spiderman'})

#python3からはformatメソッドが使える
# 引数指定
print('{0} is {1}'.format('ab', 'AB'))
# キーワード引数指定
print('{a} is {b}'.format(a='cd', b='CD'))

#クラスから指定
class MyClass(object): pass;
obj = MyClass()
#クラスに要素を追加
obj.lower , obj.upper = 'ab', 'AB'
print('{0.lower} is {0.upper}'.format(obj))

#辞書から指定
a = {'lower':'ab', 'upper':'AB'}
print('{0[upper]} is {0[lower]}'.format(a))


#文字列をスライスして作成する
print('abcdefgh'[2:])
print('abcdefgh'[2:6])
print('abcdefgh'[2:6:2])

#文字列を結合する
print(','.join(['ab', 'cd']))
