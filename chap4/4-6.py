#リストのコピー
#浅いコピー
#代入前
a = [0,1,2]
b = a[:]
print('a:' ,a)
print('b:' ,b)

#代入後
a[1] = 'item'
print('a:' ,a)
print('b:' ,b)

import copy
#深いコピー
#変更前
a = [[1,3], [2,4], 5]
b = copy.deepcopy(a)
print('a:' ,a)
print('b:' ,b)
#変更後
b[0].append('change')
print('a:' ,a)
print('b:' ,b)

#リストの比較
print([1,2,3] == [1,2,3])
print([1,2,3] > [2,1])
print([1,2,3] < [2,1])
print([1,2,3] is [2,1])

#リスト内包表記
new_listA = []

#以下同じ処理
for i in [1,2,3]:
    new_listA.append(i*2)
print(new_listA)

print([i*2 for i in[1,2,3]])
