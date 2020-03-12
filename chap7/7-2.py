#セットの作成
#set,frozenset関数を使う
#変更可能なset関数を使う
a=set([1,2,3])
print(a)
#変更不能なfrozenset関数を使う
b=frozenset([2,3,4])
print(b)

#setは変更可能な要素を持てない
#a=set([1,2,[3,4,5]])
#TypeError: unhashable type: 'list'
#入れ子にするにはfrozensetを使う
b=set([1,2,frozenset([3,4,5])])
print(b)

a=set([1,2,3])
b=set([2,3,4])
#union:要素の論理和から作る
print(a.union(b))
#intersection:要素の論理積から作る
print(a.intersection(b))
#difference:要素の差集合から作る
print(a.difference(b))
#difference:要素の対称差から作る
print(a.symmetric_difference(b))

#集合演算子を使う
#要素の論理和から作る
print(a | b)
#要素の論理積から作る
print(a & b)
#要素の差集合から作る
print(a - b)
#要素の対称差から作る
print(a ^ b)

#直接指定して作る(python3のみ)
print(type({1,2,3,4}))
#空のセットは作れない
print(type({}))
