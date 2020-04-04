#モジュール
#単一ファイルのモジュール

# カレントディレクトリをchap15にする
import os
os.chdir('chap15')

# import文を用いてほかファイルの属性を参照できる
import mymodule
print(mymodule.my_function)
print(mymodule.MyClass1)

#簡便なインポート
# 次のようにすると，指定したモジュール属性をローカルな名前空間で使える
from mymodule import MY_VALIABLE, my_function
print(MY_VALIABLE)
print(my_function)

# 次のようにすると，すべてのモジュール属性をローカルな名前空間で使える
from mymodule import *
print(my_function)
print(MY_VALIABLE)
print(MyClass1)

# 次のようにすると，モジュールを別名で使える
import mymodule as mine
from chap15.mymodule import MyClass1
print(mine.my_function)
