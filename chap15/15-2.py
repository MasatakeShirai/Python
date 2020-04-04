#複数ファイルのモジュール
# フォルダ内の複数のPythonファイルを参照したい時は，そのフォルダに__init__.pyを置く
import os
os.chdir('chap15')
print(os.getcwd())

from ourpackage import mymodule
print(mymodule.MY_VALIABLE)

#ネストしたモジュールは以下のように参照できる
from ourpackage.hermodule import itsmodule

#__init__.pyの編集
# __init__.pyで定義した属性は親フォルダのモジュール属性となる
from ourpackage import hermodule
print(hermodule.HER_BALIABLE)