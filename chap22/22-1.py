'''
バッチ処理の基本ツール
コマンドラインオプションの解釈
'''
'''
getoptモジュール
引数を適切にパースするためのモジュール
'''
import sys
import getopt

#スクリプト名を除いたコマンドライン引数リストを取得
argv = sys.argv[1:]

#getopt引数で許可するオプション名や引数の有無を設定
#戻り値で，オプション情報と引数情報に分解する

#短いオプション名の処理は第2引数で扱う
#長いオプション名の処理は第3引数で扱う
options, arguments = getopt.getopt(argv, "ab:", ('apple', 'beans='))

#オプションへの処理
for name, value in options:
    print('Name=%s, Value=%s' % (name, value))

#引数への処理
for argument in arguments:
    print('Arguments=%s' % argument)
