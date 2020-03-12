#セットの削除
#要素を指定して削除する
buff = [0,1,2,3,4,5]
a = set(buff)
a.remove(3)
a.discard(4)
print(a)

#指定した要素が存在しない時，removeはエラーが発生するが，discardは発生しない
#a.remove(6)
# KeyError: 6
a.discard(6)

#要素を取り出して削除する
#popメソッドは要素を取り出して削除する．取り出される順番の保証はない．
#指定された要素が存在しない場合，エラーが発生する．
a = set(buff)
print(a.pop())
print(a)

#要素をすべて削除する
a.clear()
print(a)

