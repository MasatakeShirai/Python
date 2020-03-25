#パスの構築
# ファイルやディレクトリのパスを設定できるようになる
import os.path

#パスの結合
print(os.path.join('abc','def'))

#ディレクトリ名の取得
# 指定したファイルまたはフォルダを直下に持つフォルダ名を取得する
print(os.path.dirname('tmp/temp.txt'))
print(os.path.dirname(os.path.join('abc','def')))

#ファイル名/リーフ・フォルダ名の取得
# 指定したパスの末端成分のファイルまたはディレクトリ名を取得する
print(os.path.basename('tmp/temp.txt'))

#絶対パスの取得
# カレントディレクトリを基準に，指定した相対パスの絶対パスを取得する
print(os.path.abspath('chap11\\11-3.py'))
print(os.path.abspath(''))

#パスの分解
# split関数はパス・セパレータで分解する
print(os.path.split('Python/temp.txt'))
# splitext関数は拡張子とそうでない部分に分解する
print(os.path.splitext('Python/temp.txt'))
# splitdrive関数はドライブとそうでない部分で分解する
print(os.path.splitdrive(os.path.abspath('')))

#パスの正規化
pathes = ('abc\\def', 'acb\.\def', 'abc\..\def')
print([os.path.normpath(path) for path in pathes])

#ユーザホームディレクトリの展開
# expanduser関数は’~’または'user'成分をホームディレクトリに置換する
print(os.path.expanduser('~/tmp'))

#共通パス成分の取得
# commonpath関数は複数のパスにおいて，行頭からの最長共通成分を取得する
print(os.path.commonpath(['abc/def/ghi','abc/def']))