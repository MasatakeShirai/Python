#dateutilモジュール
# dateutilモジュールの概要
import datetime
from dateutil import relativedelta
today = datetime.datetime.now()
print(today)
#datetimeではできなかった年・月・日の加算ができる
print(today + relativedelta.relativedelta(years=1, months=2, days=3))

#月初・月末の取得
# day引数を1にすると月初
# 99などにすると月末が加算時に得られるオブジェクトが返される
print(today + relativedelta.relativedelta(day=1))
print(today + relativedelta.relativedelta(day=99))
#月末の取得その2
print(today + relativedelta.relativedelta(months=1, days=-1))

#特定規格の日時文字列を解析
# parse関数に特定規格の文字列を入れると，datetimeオブジェクトに変換できる
from dateutil import parser
dt = parser.parse("2010-04-01T11:22:33.123456+09:00")
print(dt)
dt = parser.parse("Thu, 01 Apr 2010 11:22:33 +0000")
print(dt)
