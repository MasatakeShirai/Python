#辞書型の更新
#キーを指定して変更をする
a = {'you':'that', 'me':'this'}
a['you'] = 'them'
print(a)
#キー値が存在しない時は，新しく作られる
a['her'] = 'that'
print(a)

#メソッドでキーを指定する
#キー値youの値が返る
print(a.setdefault('you'))
#存在しないキー値の時はそのキー値が追加され，Noneが返る．デフォルト値で指定できる
print(a.setdefault('it'))
print(a)

#辞書型の結合
#aの辞書型をbで更新，既存のキーは更新，存在しないキーは追加される
b = {'you':'old', 'me':'new', 'us':'these'}
a.update(b)
print(a)
#引数型で更新
b.update(it='cool', our='cute', me='hot')
print(b)
#タプル型で更新
b.update([('you','good'),('her','bad')])
print(b)
#リテラル型で更新
b.update({'us':'big', 'them':'small'})
print(b)
