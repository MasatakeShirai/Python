#データベースの利用
#リレーショナルデータベースを利用する方法
# 直接接続する場合，SQLLite3ならばsqllite3モジュール，MySQLならMySQLdbを使うのが一般的
#DBファイル作成（SQLite3）
# カレントディレクトリ上に新規にDBファイルを作成
# パスの指定やオンメモリ上に作成することができる
import sqlite3
print(sqlite3.connect('temp.db'))

#基本的な操作（SQLite3）
# データベースへ接続
connection = sqlite3.connect('temp.db')
# カーソルオブジェクトを生成（実際の操作はこれが行う）
cursor = connection.cursor()
# executeでsql文を実行する
cursor.execute('''CREATE TABLE products (name text, price integer);''')
cursor.execute('''INSERT INTO products (name, price) VALUES ('apple', 198);''')
cursor.execute('''INSERT INTO products (name, price) VALUES ('orange', 100);''')
cursor.execute('''INSERT INTO products (name, price) VALUES ('grape', 200);''')
# データのコミット
connection.commit()

#データ抽出（SQLite3）
# fetchallは複数行の抽出，fetchoneは1行の実の抽出
cursor.execute('''SELECT * FROM products;''')
print(cursor.fetchone())
print(cursor.fetchall())

cursor.execute('''SELECT * FROM products WHERE name = "apple";''')
print(cursor.fetchone())

# コネクションを削除
connection.close()

import os
os.remove('temp.db')
