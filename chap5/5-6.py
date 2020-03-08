#辞書のコピー
#浅いコピーにはcopyメソッドやdict関数を用いる
john = {'age':20, 'programming':['Python','perl','rudy']}
taro = john.copy()
taro['age']=22
john['programming'].append('php')   #コピー元の参照データも更新
print('john:',john)
print('taro:',taro)

#深いコピーにはcopyモジュールのdeepcopy関数を用いる
import copy
taro = copy.deepcopy(john)
taro['programming'].append('C')     #コピー元の参照データは更新されない
print('john:',john)
print('taro:',taro)

#辞書の比較
#==, !=：キーと値すべての同一性を比較
print({'a':1, 'b':2} == {'a':1, 'b':2})
print({'a':1, 'b':2} == {'a':1, 'b':3})
#is比較：オブジェクトそのものの同一性を比較
a = b = {'a':1, 'b':2} == {'a':1, 'b':2}
print(a is {'a':1, 'b':2})
print(a is b)