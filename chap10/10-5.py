#文字列の削除
# 文字列は変更不可なので，削除に見える動作を紹介
#文字列から特定の文字列を取り除く
print('abca'.strip('a'))
# 左側から取り除く
print('abca'.lstrip('a'))
# 右側から取り除く
print('abca'.rstrip('a'))
# 端以外の文字列は取り除かれない
print('abaca'.strip('a'))
# 指定がないと，端の空白文字が取り除かれる
print(' ab a ca '.strip())
