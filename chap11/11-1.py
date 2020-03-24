#ファイルの基本操作
# ファイル書き込みの基本
f = open('temp.txt', 'w')
f.write('abc')
f.close()

# ファイル読み込みの基本
f = open('temp.txt', 'r')
print(f.read())
f.close()

# 行ごとに書き込む
# ・wtriteを連続で実行する，
# ・writelinesメソッドにイテラブルなオブジェクトを渡す．
f = open('temp.txt', 'w')
f.write('abc\n')
f.write('def\n')
f.writelines(['abc\n', 'def\n'])
f.close()

# 行ごとに読み込む
# ・readlineメソッドを連続で利用する
f = open('temp.txt', 'r')
print(f.readline())
print(f.readline())
print(f.readline())
print(f.readline())
f.close()
# ・readlinesメソッドによって行のリストを得る
f = open('temp.txt', 'r')
print(f.readlines())
f.close()
# ・ファイルオブジェクトをイテレータで回す
f = open('temp.txt', 'r')
print([line for line in f])
f.close()

#ポインタを移動する
# 以下の例では，一度読みだしたファイルをもう一度読み出せるようにしている
f = open('temp.txt', 'r')
print([line for line in f])
f.seek(0)
print([line for line in f])
f.close()

#ファイルの追加書き込み
f = open('temp.txt','r')
print(f.readlines())
f = open('temp.txt', 'a')
f.write('ghi\n')
f = open('temp.txt','r')
print(f.readlines())
f.close() 

#バイナリモードで開く
f = open('temp.txt','rb')
print(f.readlines())
 
