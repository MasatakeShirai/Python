#文字列の概要
# バイト文字列，Unicode文字列，raw文字列が存在する
# 変更不能オブジェクト
# 日本語などマルチバイト文字列の扱いに注意

#'も”も同じ
print('abc',"def")

#""""で複数行にわたる文字列
string="""abc
        def"""
print(string)

#エスケープシーケンスはcと互換
print('abc\ndef')

#row文字列はエスケープシーケンスを無効化
print(r'abc\ndef')

#文字列の連結
print('ab'+'cd')

#文字列を指定回数反復して連結
print('ab' * 3)

#str関数でなんでも文字列表現にできる
print(str([1,2,3,4,5]))

#インデックスでアクセスできる
s='abcded'
print(s[3])
#スライスも使える
print(s[1:4])
#ただし変更は不可
#s[3]='D'
# TypeError: 'str' object does not support item assignment

#フォーマット文字列はCと互換
print('%s is now version %d.'%('Python', 3))

#辞書で値を指定できる
print('%(lang)s is now version %(num)d'%{'lang':'python', 'num':3})

#Unicode文字列，長さ3
print(len(u'日本語'))

#マルチコード文字列．長さは3ではない
print(len(u'日本語'.encode('utf8')))
