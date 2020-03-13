#ループ
# forループ
# 構文：for 要素 in iterableオブジェクト
for a in [1,2,3]:
    print(a)

#カウンタを取るforループには，整数リストを作成するrange関数を利用する
for a in range(4):
    print(a)

#指定オブジェクトの要素の取り出しと共にカウントしたいときはenumerrate関数を用いる
for i, elem in enumerate(['a','b','c']):
    print('%s:%s'%(i,elem))

#whileループ
# 構文；while 条件式:
x=0
while x<=5:
    print(x)
    x+=1

#continue・break・else
# continue：それ以降の処理をせずに，ループの初めに戻る
for a in range(9):
    if a%2==0:
        continue
    print(a)

# break：それ以降の処理をせずに，ループを抜け出す
x=0
while True:
    print(x)
    x+=2
    if x>5:
        break

# else：break文が実行されなかった場合に限り，実行される
for a in range(1):
    break
else:
    print('yes')

for a in range(4):
    pass
else:
    print('yes')

#普通にループが終わってもelseは実行される
for a in range(4):
    print(a)
else:
    print('yes')
