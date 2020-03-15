#ジェネレータ
# ジェネレータとは
# ジェネレータは関数に結び付く広義のイテレータ
# 基本的な作成方法
# 関数の定義においてyield文を用いるとイテレータ（ジェネレータ）を生成する関数になる
def gen():
    yield 1
    yield 2
    yield 3

for i in gen():
    print(i)

def get_primes():
    n=2
    while True:
        i=2
        while i<n:
            if n%i==0:
                break
            i+=1
        if i==n:
            yield n
        n+=1
primes = get_primes() 
print([primes.__next__() for a in range(10)])

#内包表記による作成
gen2 = (i*3 for i in range(10))
try:
    while True:
        print(gen2.__next__())
except StopIteration:
    pass