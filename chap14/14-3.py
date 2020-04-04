#例外を発生させる
#raise文
# ある関数において目的を達成でいなくなった時，明示的に例外を発生させることで処理を外部にゆだねることができる
#例外の再発生
# 例外を補足して何らかの処理をした後，その例外を再び発生させるには特定の例外を指定しないraise文を用いる
def accumulate(values):
    total = 0
    try:
        for v in values:
            if v < 0:
                raise ValueError('all elements must not be less than 0')
            total += v
        return total
    except ValueError:
        print('raise ValueError')
        #例外の再発生
        raise

accumulate([1,2,-1])