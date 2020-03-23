#文字列の更新
# 文字列は本来は変更不可であり，新しく文字列を作成してコピーを返しているだけ
#文字列の分割
# 指定文字列で分割する
print('abcbdbe'.split('b'))
# 分割回数1回
print('abcbdbe'.split('b',1))
# 右側から1回だけ分割する
print('abcbdbe'.rsplit('b',1))
# 空白で分割する
print('ac de'.split(' '))
# 何も指定しないか，Noneを指定した時，空白文字列を両端から削除した後，空白で分割される
print(' ac de '.split())

# 文字列を改行文字で分割する
print('ac\nde'.splitlines())
# Trueを指定すると改行文字を残す
print('ac\nde'.splitlines(True))

# 区切り文字とその周辺の文字列がタプルで返る
print('abcbdbe'.partition('b'))
# 右側から検索
print('abcbdbe'.rpartition('b'))
# 区切り文字がない時，後ろ2要素は空白
print('abcbdbe'.partition('z'))

# 文字列を指定文字列で置き換える
print('abcbe'.replace('bc','BC'))
# 該当文字列はすべて置換
print('a b c b e'.replace(' ','+'))
# 置換回数を制限できる
print('a b c b e'.replace(' ','+',2))

#タブ幅に展開する
# すべてのタブ文字をタブ等分になるように分割
# タブ幅が与えられないならタブ幅は8文字
print('**\t*****\t'.expandtabs().replace(' ','-'))
print('**\t*****\t'.expandtabs(4).replace(' ','-'))

#大文字・小文字に変換する
# すべての大文字を小文字に変換する
print('ABC'.lower())
# すべての大文字を小文字に変換する
print('abc'.upper())
# 先頭だけ大文字に変換する
print('ABC DEF'.capitalize())
# タイトルケースにする
print('ABC DEF'.title())

#左寄せ，中央寄せ，右寄せに変更する
# 左寄せ
print('ABC'.ljust(10))
# 中央寄せ
print('ABC'.center(10))
# 右寄せ
print('ABC'.rjust(10))
# 空白以外も指定できる
print('ABC'.ljust(10,'-'))
# 指定文字数より多いときはそのまま
print('ABC'.center(2))

#0字詰め文字列に変更する
# 指定した文字数になるように0で埋める
print('abc'.zfill(10))
# 指定文字数が少ないときにはそのまま
print('abcdef'.zfill(4))
