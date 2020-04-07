#dateクラス
#dateクラスの概要
# 日付だけを表現する
# datetimeクラスはdateクラスのサブクラスなので，dateクラスにあるメソッドはdatetimeクラスデモ使える
import datetime
print(datetime.date(2020,4,7))

#dateクラスの基本的な操作
# ほぼdatetimeクラスと同じだが，現在日付の取得はnow関数でなく，today関数を使う
# 現在日付の取得
print(datetime.date.today())
# 属性の取得
oneday = datetime.date(2020,4,7)
print(oneday.year)
# 加算
print(oneday + datetime.timedelta(days=1))
# 比較
print(oneday > datetime.date.today())
# 文字列変換
print(oneday.strftime('%Y-%m-%d'))

#datetimeオブジェクトとdateオブジェクトの変換
# そのまま加算・減算．比較できないので，変換する必要がある
dt = datetime.datetime(2020,4,7,21,25)
d = datetime.date.today()
#比較
dt2 = dt.date()
print(d > dt2)

#dateオブジェクトをdatetimeオブジェクトに変換するメソッドはないので，以下のようにする
d2 = datetime.datetime(d.year, d.month, d.day)
print(dt < d2)
