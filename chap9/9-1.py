#イテレータの基礎
#イテレータとは
# 一般的にデータを走査するポインタ的な役割を果たす，
# 大きなデータをロードして，for文を回すより，イテレータを用いて逐次的に処理するほうが効率的．
#イテレータの挙動
#イテレータの作成
users = iter(['Alice','Bob','Carol'])
print(users)

#python2環境だと.next(),python3環境だと._next_()
# https://qiita.com/polarbear08/items/b2022b534633114207e9
try:
    while True:
        print(users.__next__())
except StopIteration:
   pass

users =  iter(['Alice','Bob','Carol'])
for user in users:
    print(user)
#二度目は空になる
for user in users:
    print(user)
