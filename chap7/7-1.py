#セットの概要
#セットの作成
a = set([1,2,3])
print(a)
#重ならない要素を追加
a.add(4)
print(a)
#重なる要素は追加されない
a.add(3)
print(a)
#要素の削除
a.remove(1)
print(a)

#コンストラクタ引数の順番はソートされる
a=set([3,1,2])
print(a)
#コンストラクタ引数の重複は除去される
a=set([3,1,2,1])
print(a)

#変更可能オブジェクトを要素に持てない
#a=set([[1,2],3,4])
#TypeError: unhashable type: 'list'

b=set([2,3,4])
#和集合の作成
print(a.union(b))
#共通集合を作成
print(a.intersection(b))

#変更不能なフローズンセットを作成
b=frozenset([3,4,5])
print(b)
#b.add(7)
#AttributeError: 'frozenset' object has no attribute 'add'