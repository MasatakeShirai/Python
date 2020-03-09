#タプルの作成
a=(1,2,3)
print(a)

#要素が1つしかない時はカンマをつける.付けないと定数として扱われる.変更もできる
b=('abc',)
print(b)
c=(1)
print(c)
d=('abc')
print(d)
d='def'
print(d)

#掛け算でも作成できる
e = a*3
print(e)

#tuple関数で空タプルを作成できる
print(tuple([1,2,3,'python']))

#タプルの一部から作る
f=(0,1,2,3,4,5,6,7,8)
print(f[0:4])
print(f[0:10:2])
