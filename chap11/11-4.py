#ファイルシステム上の操作
# 基本的にはosモジュールを利用するが，高度な操作にはshutilモジュールを利用する
import os
import shutil

f = open('temp.txt', 'w')
f.write('abc')
f.close()

#存在チェック
# カレントディレクトリを基準に存在するかをチェック
print(os.path.exists('temp.txt'))
print(os.path.exists('abcd.txt'))
# ディレクトリかをチェック．カレントディレクトリ内に存在しないときはfalse
print(os.path.isdir('temp.txt'))
print(os.path.isdir('chap11'))
# ファイルかをチェック．カレントディレクトリ内に存在しないときはfalse.絶対パスを指定すれば判定できる
print(os.path.isfile('temp.txt'))
print(os.path.isfile('chap11'))
# リンクかどうかを判定
print(os.path.isdir('temp.txt'))

#ファイルの削除
# 指定がフォルダ名の時はエラーになる
os.remove('temp.txt')

#ディレクトリの作成
# すでに存在する時はエラーになる
os.mkdir('tmp')

#ディレクトリの連続作成
# 末端のディレクトリがすでに存在するときはエラーになる
os.makedirs('tmp/tmp1/tmp2')
print([os.path.exists(p) for p in ('tmp','tmp/tmp1','tmp/tmp1/tmp2')])

#ディレクトリを削除
# 指定したディレクトリを削除する．ただし，そのディレクトリは空でなければいけない
os.rmdir('tmp/tmp1/tmp2')
print([os.path.exists(p) for p in ('tmp','tmp/tmp1','tmp/tmp1/tmp2')])

#ディレクトリの連続削除
# 指定したパスのパス成分ぼディレクトリを削除する．
# 末尾のディレクトリが空でない時はエラーになり，途中のパス成分が空になるところまで削除される
os.removedirs('tmp/tmp1')
print([os.path.exists(p) for p in ('tmp','tmp/tmp1','tmp/tmp1/tmp2')])

#ディレクトリの全削除
# 指定したディレクトリを内部のファイルディレクトリ含めてすべて削除する
#os.makedirs('tmp/tmp1/tmp2')
os.makedirs('tmp/tmp1/tmp2')
f = open('tmp/tmp1/temp.txt','w')
f.write('abc')
f.close()
shutil.rmtree('tmp')
print([os.path.exists(p) for p in ('tmp','tmp/tmp1','tmp/tmp1/tmp2')])

#ファイルやディレクトリの移動
os.makedirs('tmp/tmp1/tmp2')
f = open('tmp/tmp1/temp.txt','w')
f.write('abc')
f.close()
os.rename('tmp/tmp1/temp.txt','tmp/temp.txt')
os.rename('tmp/temp.txt','tmp/Newtemp.txt')

#ファイルのコピー
# copyfile関数はファイルをコピーする
shutil.copyfile('tmp/Newtemp.txt','tmp/tmp1/copyfile.txt')
# copy関数はターゲットにディレクトリを指定すると，その直下にファイルをコピーする
shutil.copy('tmp/Newtemp.txt','tmp/tmp1')
# copy2関数は最終アクセス時間やメタデータもコピーする
shutil.copy2('tmp/Newtemp.txt','tmp/tmp1')

#カレントディレクトリの絶対パスを取得
print(os.getcwd())
#ファイルディレクトリ名のリストを取得
print(os.listdir())
#カレントディレクトリの変更
os.chdir('tmp')
print(os.getcwd())

#ディレクトリのコピー
# ディレクトリとその内容をcopy2関数でコピーする
shutil.copytree('tmp1','tmp2')
print(os.listdir())

#globモジュールでパターン検索
import glob
f = open('1.txt','w')
f.close()
print(glob.glob('./[0-9].*'))

#ファイルメタデータの取得
# stat関数はファイルやディレクトリのメタデータが入ったオブジェクトを返す
m = os.stat('1.txt')
import time
print(time.ctime(m.st_mtime))

#アクセス権限の確認
# 読み取り可能か？
print(os.access('1.txt', os.R_OK))
# 書き込み可能か？
print(os.access('1.txt', os.W_OK))
# 実行可能か？
print(os.access('1.txt', os.X_OK))

#アクセス権限の変更
import stat
print(oct(stat.S_IRWXU))
print(os.chmod('1.txt',0o700))

#環境変数の取得
# osモジュールのenviron変数に様々な環境変数が辞書型で格納されている
path=os.environ.get('PATH')
for i in path.split(';'):
    if i=='.':
        break
    print(i)

#最後に作成したフォルダ・ディレクトリを削除
os.chdir('..')
shutil.rmtree('tmp')