#データのやり取り
#オブジェクトの直列化
#pickleモジュール
# オブジェクトをセーブしたり，送信したりする時には直列化が必要になる
import pickle
cache = {'id':123, 'name':'Alice', 'content':None}
# 文字列ベースのオブジェクトの直列化と復元はdumps関数とloads関数を用いて行われる
# 直列化
serialize = pickle.dumps(cache)
print(type(serialize))
print(serialize == cache)
# 復元
deserialize = pickle.loads(serialize)
# 内容は一致するが，同じものではない
print(deserialize == cache)
print(deserialize is cache)

#ストリーム上の直列化と復元
f = open('data.pkl','wb')
# 直列化
pickle.dump(cache, f)
f.close()

f = open('data.pkl','rb')
# 復元
deserialize = pickle.load(f)
f.close()
print(deserialize == cache)

import os
os.remove('data.pkl')

#循環参照
# 循環参照があるオブジェクトは自動的に循環参照が考慮されて直列化される
class Node(object):
    def __init__(self,name):
        self.name = name
        self.edges = []
    def connect(self,node):
        self.edges.append(node)
        
a = Node('a')
b = Node('b')
c = Node('c')
a.connect(b)
b.connect(c)
c.connect(a)
serialized = pickle.dumps(a)
deserialized = pickle.loads(serialized)
print(deserialized.edges[0].edges[0].edges[0].name)

