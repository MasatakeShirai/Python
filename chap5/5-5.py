#辞書型の削除
#指定したキーと対応値を削除できる
#存在しないキーは指定できない
buff = {'you':'that', 'me':'this'}
a = {}
a.update(buff)
print(a)
del a['you']
print(a)

#キー値を取り出して削除する
#キーが存在しない場合にはエラー，またはデフォルトで設定した値を返す
a.update(buff)
print(a)
print(a.pop('you'))
print(a.pop('him', 'new'))
print(a)

#キー値との組み合わせを取り出して削除
#空の辞書に対して行うとエラー
a.update(buff)
print(a)
print(a.popitem())
print(a.popitem())
print(a)
