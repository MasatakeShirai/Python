#モジュールのパスを通す
#sys.path
# モジュールをインポートするときにどのフォルダ・ファイルを参照するかは
# sys.pathに格納されるモジュールの検索パスに基づいて決められる
# 検索パスに値を追加する時はappendを使う
import sys
sys.path.append('Python/chap15/ourpackage')

import ourpackage

#sys.pathはリストなので表示することができる
import pprint
print(type(sys.path))
pprint.pprint(sys.path)