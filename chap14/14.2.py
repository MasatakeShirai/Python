#例外情報を取り出す
# 例外インスタンス情報の取得

try:
    x = 1/0
except ZeroDivisionError as instance:
    print(instance)

#トレースバックの表示
# 例外がどこでどのように起こったか詳しく知りたいときは
#sysモジュールのexc_info関数空取得できるエラー情報を調査する．
import sys
import traceback
try:
    f = open('temp.txt', 'r')
except IOError:
    error_type, error_value, traceback_ =sys.exc_info()
    tb_list = traceback.format_tb(traceback_)
    print(error_type)
    print(error_value)
    print(tb_list)
