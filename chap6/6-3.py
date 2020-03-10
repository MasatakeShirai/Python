 #タプルの読み込み
#インデックスで指定
a = ('python',1,2,'python',4,5,1)
print(a[2])

#位置を調べる・存在しない要素を指定するとエラー
print(a.index('python'))
#インデックス2移行で1を検索
print(a.index(1,2))
#インデックス1から5の間でpythonを検索
print(a.index('python',1,5))

#指定された要素の数を数える
print(a.count('python'))
#存在しない要素の時は0
print(a.count(6))

#指定された要素が含まれるか判定
print('python' in a)
print('java' in a)

#タプルの長さを調べる
print(len(a))
print(len(()))

#タプルの最大・最小を調べる
print(max((1,5,2,3)))
print(min((1,3,2,4)))
#int型に戻してから比較
print(max(('4','2','1','3'),key=int))

#集約関数
#タプルの各要素を足し合わせる
print(sum((1,4,2,3)))
#いずれかの要素がTrueであれば，Trueを返す
print(any((True,False,True)))
#すべての要素がTrueであれば，Trueを返す
print(all((True,False,True)))
print(all((True,)*3))
