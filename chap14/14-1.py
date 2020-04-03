#例外処理
#処理の分岐
# try-except文
# try-exceptで囲まれた範囲で例外が補足されると，except節で処理される
# exceptでは例外の種類を補足できる
try:
    f = open('temp.txt','r')
except IOError:
    print('ファイルを開けません : temp.txt')

#else節
# try-exceptで囲まれたコードが例外なく終了した場合にのみ実行される
collection = {'a':1, 'b':2}
for key in ('a','b','c'):
    try:
        value = collection[key]
    except KeyError:
        print('miss %s'%key)
    else:
        print('hit %s:%s'%(key,value))

#複数のexcept節
# 複数の例外が発生する時，各例外に応じて処理を書くことができる

#finaly節
# 例外の発生いかんに関わらず最後に必ず行う処理はここに書く
# python2.5からはexceptやelseと同時に利用可能
try:
    while True:
        try:
            x = 1.0 / float(input('input number:'))
        except ValueError:
            print('It is not number')
        except ZeroDivisionError:
            print('Can\'t input 0')
            break
        except:
            print('Unknown Error')
            break
        else:
            print('Reciprocal is %s'%x)
finally:
        print('Terminates processing')
    
#with文の使用
# finally節が使われるのはオブジェクトの生成と1対1になる処理が多い
# そのような処理はpython2.6で導入されたwith文を用いると簡潔に書ける
#with open('num_list.txt', 'r') as f:
#    total = sum([int(line) for line in f.readlines()])