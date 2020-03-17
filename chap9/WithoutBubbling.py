def get_playre(name, cards):
    turn = 0
    while True:
        if turn==0:
            #カードを受け取るまで待期(コルーチン：処理を一時停止し，外部から値を与える)
            # 参考：https://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
            card = yield
        else:
            #カードを渡して受け取る（リストから数字をpopし，yieldで受け取る）
            card = (yield cards.pop(0))
        cards.append(card)
        print('turn %d : %s got %s: %s'%(turn,name,card,cards))
        turn += 1

player1 = get_playre('player1', [1,2,3,4])
player2 = get_playre('player2', [5,6,7,8])
#カードを受け取る準備をする（1つ目のyield文のところで処理を止めておく）
# デバッグにおける実行，yieldはブレークポイントのようなものか
# https://docs.python.org/ja/3/reference/expressions.html#generator.send
# '__next__()：ジェネレータ関数の実行を開始するか、最後に yield 式が実行されたところから再開します'
player1.__next__()
player2.__next__()

card = 9
for turn in range(2):
    #カードを受け取り，カードを渡す
    card = player1.send(card)
    card = player2.send(card)
