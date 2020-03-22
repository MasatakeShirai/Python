#文字列の読み込み
#インデックスで指定
s='0123456'
print(s[4])

#文字列を検索
# in演算子は指定した文字列を検索してtrueかfalseを返す
print('ab' in 'abcde')
print('ef' in 'abcde')
print('ba' in 'abcde')

#文字列を検索する
# 指定した文字列を検索して出現したインデックスを返す
print('abcdef'.find('a'))
print('abcbeb'.find('b'))
# 右側から検索する
print('abcbeb'.rfind('b'))
# indexはfindaと同じような動作
print('abcbeb'.index('b'))
# 存在しない文字列の時は-1を返す
print('abcbeb'.find('f'))

# 検索の開始位置と終了位置を指定できる
# 開始位置指定
print('abcbeb'.find('b',2))
# 開始，終了位置指定
print('abcbeb'.find('b',2,4))

#文字列の出現回数を調べる
print('abcbeb'.count('b'))
# 開始位置を指定できる
print('abcbeb'.count('b',2))
# 終了位置も指定できる
print('abcbeb'.count('b',5))

#開始文字・終了文字を調べる
# aで文字列で始まるのでtrue
print('abcbeb'.startswith('a'))
print('abcbeb'.startswith('ab'))
print('abcbeb'.startswith('ba'))
# 開始位置が1だとbcで始まる
print('abcbeb'.startswith('bc',1))
# 開始位置が4だとbeで始まる
print('abcbeb'.endswith('cb',0,4))

#英数文字列の確認
# アルファベットのみの時にtrueを返す
print('abc'.isalpha())
# 数字のみの時にtrueを返す
print('123'.isalnum())

#数字の確認すべて
# 数字の時にtrueを返す
print('123'.isdigit())
print('-123'.isdigit())
# python3なら全角にも対応
print('１２３'.isdigit())
# isnumeric()ならアラビア文字対応
print('Ⅰ'.isnumeric())

#大文字・小文字の判定
# 文字列がすべて小文字かを確認する
print('abc'.islower())
# 文字列がすべて大文字かを確認する
print('ABC'.isupper())
# 最初の文字だけが大文字（タイトルケース）であるかを確認する
print('Abc'.istitle())
# スペースや記号があっても無視する
print('a b c!'.islower())

#空白文字の確認
# 文字列がすべて空白，タブ，もしくは改行の時にtrueを返す
print('\n \t'.isspace())

#識別子の確認(python3のみ)
# 文字列が変数として利用できるかを判定できる
print('_abc'.isidentifier())

#表示可能な文字列を確認する(python3のみ)
print('abc'.isprintable())
# タブは表示可能ではない
print('a\tbc'.isprintable())
