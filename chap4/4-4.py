def my_cmp(x,y):
    x1 = int(x)
    y1 = int(y)

    if x1 > y1:
        return 1
    elif x1 == y1:
        return 0
    else:
        return -1

a = ['1000', '90', '-800', '120']
b = ['abc', 'bc', 'a', 'ab']
print(sorted(a))

#文字列のソートはそのまま返される
print(sorted(b))
print(sorted(b, key=len))

def a_key1(x):
    return int(x)

def a_key2(x):
    return -int(x)

#sortedのkey引数は全体に適応されるもの
print(sorted(a, key=a_key1))
print(sorted(a, key=a_key2))
