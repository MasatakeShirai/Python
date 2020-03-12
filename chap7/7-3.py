#セットの読み込み
#forループによる要素の取得
a=set([1,3,2])
for v in a:
    print(v)

#部分集合の確認をする
# issubsetメソッドは，全要素が指定オブジェクトに含まれるか調べる
print(a.issubset(([1,2,3,4,5])))
print(a.issubset(([3,4,5])))

#上位集合の確認をする
# issupersetメソッドは，指定オブジェクトの全要素が含まれるか調べる
print(a.issuperset(([1,2])))
print(a.issubset(([3,4,5])))

#要素の存在を確認する
print(3 in a)
print(5 in a)

#要素の数を確認する
print(len(a))
