#日時の操作
# datetimeクラス
# 日時情報はdatetimeモジュールのdatetimeクラスが保持する
#日時を生成
import datetime
print(datetime.datetime(2020,4,4))
print(datetime.datetime(2020,4,4,16,4,0,0))

#現在日時を取得
print(datetime.datetime.now())

#年，月，日，時，分，秒，マイクロ秒を個別に取得する
dt = datetime.datetime.now()
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(dt.microsecond)

#曜日を取得
# 0-6(月-日)で取得できる
print(datetime.datetime.now().weekday())
print(datetime.datetime(2020,4,1).weekday())

#日時の加算・減算
# timedeltaクラスを用いて日時の加算・減算ができる
# 年・月単位の計算はできない
print(dt + datetime.timedelta(days=7))
print(dt - datetime.timedelta(weeks=5))

#日時同氏の差分を計算
dt2 = datetime.datetime(2010,4,1)
delta = dt - dt2
print(delta)
print(delta.days)

#日時の比較
# 大きい：進んでいる扱い
print(dt > dt2)
print(dt < dt2)

#協定世界時の取得
utc = datetime.datetime.utcnow()
print(utc)

#日時を文字列に変換
print(utc.strftime('%Y-%m-%d %H:%M:%S'))
