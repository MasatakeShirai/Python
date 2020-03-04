import copy
a = ['python', 'java', 'python', 'rudy']
b = copy.copy(a)
c = copy.copy(a)

#.removeを使って削除
print('a:')
print(a)
a.remove('python')
print(a)

#同じ要素をすべて削除するためには
print('b:')
print(b)
while b.count('python'):
    b.remove('python')
print(b)

#インデックスもしくはスライスを使った削除
print('c:')
print(c)
del c[1]
print(c)
del c[1:]
print(c)