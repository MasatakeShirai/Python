#辞書の作成
#直接指定して作成する
a = {'you':6, 'me':3}
print('a:',a)
b = {3:['this', 'that'], 'it':7}
print('b:',b)

#dict関数を使って作成
#引数型
print(dict(you=123, me=321))
#タプル型
print(dict([('yours',123), ('mine',321)]))
#リテラル型
print(dict({'your':123, 'my':321}))

#copyメソッドを使う
#作成はdictよりcopyを使ったほうが速い
print({'you':6, 'me':8}.copy())

#dictとcopyで時間を計測
import timeit
print(timeit.Timer("dict({'you':123, 'your':123, 'I':123, 'my':321, })").timeit(10000))
print(timeit.Timer("{'you':123, 'your':123, 'I':123, 'my':321, }.copy()").timeit(10000))

#キーのリストから作る
#デフォルトの初期値はNone
c = dict.fromkeys(['python', 'rudy', 123])
print(c)
#デフォルト値を指定できる
d = dict.fromkeys(['English', 'Japanese'], 'langage')
print(d)