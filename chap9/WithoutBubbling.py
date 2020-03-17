import random

def get_playre(name, cards):
    turn = 1
    while True: 
        if turn==1:
            #カードを受け取るまで待期(コルーチン：処理を一時停止し，外部から値を与える)
            # 参考：https://postd.cc/python-generators-coroutines-native-coroutines-and-async-await/
            card = yield
        else:
            #手札からランダムにカードを渡す．カードがないときは処理を行わない
            if len(cards)!=0:
                PassNum = random.randint(1,len(cards))-1
                card = (yield cards.pop(PassNum))
        
        #手札（リスト）が無くなった時にゲームに勝利する
        if len(cards)==0:
            yield [name,'win']

        #カードを手札（リスト）に入れる
        cards.append(card)
        if type(card)!=list:
            print('%s : got %s : %s'%(name,card,cards))
        turn += 1

        #同じカードを捨てる
        if cards.count(card)==2:
            for n in range(2):
                cards.remove(card)


player1 = get_playre('player1', [1,2,3,4,5,6])
player2 = get_playre('player2', [1,2,3,4,5,6])
#カードを受け取る準備をする（1つ目のyield文のところで処理を止めておく）
# デバッグにおける実行，yieldはブレークポイントのようなものか
# https://docs.python.org/ja/3/reference/expressions.html#generator.send
# '__next__()：ジェネレータ関数の実行を開始するか、最後に yield 式が実行されたところから再開します'
player1.__next__()
player2.__next__()

card = 'joker'
turn = 1
#while True:
for a in range(8):
    print('%d turn----------'%turn)
    #カードを受け取り，カードを渡す．
    # 手札（リスト）が無くなった時点でループを抜ける
    card = player1.send(card)
    if type(card)==list:
        break

    card = player2.send(card)
    if type(card)==list:
        break
    turn+=1

print('Game is finish. %s is win! in %d turn'%(card[0],turn))
