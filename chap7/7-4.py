#セットの更新
#要素の追加
a=set([1,2,3])
a.add(4)
print(a)
#すでに存在する要素は追加されない
a.add(2)
print(a)

#要素の論理和で更新する
a.update([3,4,5])
print(a)

#要素の論理積で更新する
a.intersection_update([1,2,3,4,7,8])
print(a)

#要素の論理差で更新する
#指定要素を削除して更新
a.difference_update([3,4])
print(a)

#要素の対称差で更新する
#指定要素と共通する要素を削除して更新
a.symmetric_difference_update([1,2,3])
print(a)

#代入演算子を使って
# 更新集合演算を使った後に左辺が更新される
#論理和
a=set([1,2,3])
a |= set([1,2,3,4,5])
print(a)

#論理積
a &= set([1,2,3,4,7,8])
print(a)

#論理差
a -= set([3,4])
print(a)

#対称差
a ^= set([1,2,3])
print(a)

#フローズンセットも更新できるが，その場合は新しいものが代入されるだけ
a = frozenset([1,2,3])
b = set([3,4,5])
a |= b
print(a)

