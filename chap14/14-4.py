#独自の例外
#Exceptionクラス
# 独自の例外クラスを置くことでより柔軟に例外制御ができるようになる
# すべての例外クラスはExceptionクラスを継承して作る
class RangeError(Exception):
    pass

def get_grade(score):
    if score<10 or score>990:
        raise RangeError(score)
    return int((1000-score)/100)

#print(get_grade(5))
# 独自の例外が発生する
# __main__.RangeError: 5

# 独自の例外クラスを継承して，より詳細に例外パターンを処理できる
class UpperRangeError(RangeError):
    pass

class LowerRangeError(RangeError):
    pass

def get_grade(score):
    if score<10:
        raise LowerRangeError(score)
    if score>990:
        raise UpperRangeError(score)
    
    return int((1000-score)/100)

#print(get_grade(1000))
# 継承先の例外が発生する
# __main__.UpperRangeError: 1000

# 継承先の例外は継承元の例外クラスでも補足できる
# この時，継承先の例外をすべて補足できる
try:
    print(get_grade(5))
except RangeError:
    print('too high ot too low')
    raise
