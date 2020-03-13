#その他の操作
#セットの比較
#セットの同一性を比較
print(set([1,2,3]) == set([1,2,3]))
#セットの部分集合・上位集合を判定
print(set([1,2,3]) <= set([1,2,3,4,5]))
print(set([1,2,3]) < set([3,4,5]))
#オブジェクト自体の同一性を比較
print(set([1,2,3]) is set([1,2,3]))

#セットのコピー
import copy
class MyClass(object):pass
obj=MyClass()
obj.ref=[1,2]
myset=set([obj])
#浅いコピー
shallow=myset.copy()
#深いコピー
deep=copy.deepcopy(myset)
#参照先を更新
obj.ref.append(3)
#浅いコピーでは更新される
print(shallow.pop().ref)
#深いコピーでは更新されない
print(deep.pop().ref)

#セット内包表記
print({i for i in range(6) if i%2})