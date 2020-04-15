#csvデータの読み書き
#csvモジュール
# CSVは主に表形式のデータを保存するために使われるデータ形式
# 中身は各項目をカンマで区切ったテキストファイル
#csvを読み込む
import csv
try:
    fh = open('data.csv', 'w')
    fh.write('1,apple,orenge\n2,car,train')
finally:
    fh.close()

try:
    fh = open('data.csv', 'r')
    reader = csv.reader(fh)
    for row in reader:
        print(row)
finally:
    fh.close()

#文字列をcsvとして処理
import io
csv_string = '1,taro\r\n2,jiro\r\n'
fh = io.StringIO(csv_string)    #疑似的なファイルハンドラ生成
for row in fh:
    print(row)

#csvの書式を調整する
# 独自のcsvに対応するため，書式の解釈を変更できる
class MyDialect(csv.excel):
    delimiter = '&'
csv_string = '1,taro&2,jiro&'
fh = io.StringIO(csv_string)    #疑似的なファイルハンドラ生成
reader = csv.reader(fh, dialect=MyDialect)
n=0
for row in reader:
    print(row)

#行を辞書型で受け取る
csv_string = '1,taro\r\n2,jiro\r\n'
fh = io.StringIO(csv_string)    
reader = csv.DictReader(fh, fieldnames=['id', 'name'])
for row in reader:
    print(row)

#1行目をフィールド名として解釈する
# 明示的にフィールド名を与えない場合は1行目をフィールド名として解釈する
csv_string = 'id,name\r\n1,taro\r\n2,jiro\r\n'
fh = io.StringIO(csv_string)    
reader = csv.DictReader(fh)
for row in reader:
    print(row)

#CSVを書き込む
try:
    fh = open('data.csv', 'w')
    writer = csv.writer(fh)
    writer.writerow([3,'America','Japan'])
    writer.writerow([4,'Sunny','Rain'])
finally:
    fh.close()

try:
    fh = open('data.csv', 'r')
    reader = csv.reader(fh)
    for row in reader:
        print(row)
finally:
    fh.close()


import os
os.remove('data.csv')
