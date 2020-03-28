#テンポラリファイルの利用
# 一時ファイルを利用する際にはtempfilモジュールをimportする
import tempfile
#mkdtemp関数は一時ディレクトリを作成する．
# dirを指定すると指定されたディレクトリ下に作成される
# 作成したディレクト一時ディレクトリは明示的に削除する必要がある
tmpdir = tempfile.mkdtemp(dir='.')
print(tmpdir)
import os
import shutil
try:
    print(os.path.isdir(tmpdir))
finally:
    shutil.rmtree(tmpdir)

#一時ファイルの作成
# mkstemp関数，NamedTemporaryFile関数は一時ファイルを作成する
# 前者は明示的に削除する必要があるが，後者はクローズすれば自動的に消去される
tmpfd, tmpname = tempfile.mkstemp(dir='.')
print(tmpname)
f = os.fdopen(tmpfd, 'w+b')
f.close()
print(os.path.exists(tmpname))
os.remove(tmpname)

f = tempfile.NamedTemporaryFile(dir='.')
print(f.name)
f.close()
print(os.path.exists(f.name))

