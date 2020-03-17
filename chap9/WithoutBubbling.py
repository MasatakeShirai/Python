def get_playre(name, cards):
    turn = 0
    while True:
        if turn==0:
            card = yield
        else:
            card = (yield cards.pop(0))
        cards.append(card)
        print('%s got %s: %s'%(name,card,cards))
        turn += 1

player1 = get_playre('player1', [1,2,3])
player2 = get_playre('player2', [4,5,6])
player1.__next__()
player2.__next__()

card = 7
for turn in range(2):
    card = player1.send(card)
    card = player2.send(card)
