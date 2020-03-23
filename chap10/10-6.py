#Unicode文字列と文字コード変換
# pythonには通常の文字列であるバイト文字列とUnicode文字列の2種類ある
# デフォルトはバイト文字列だが，日本語や中国語などマルチバイト文字の境界を正しく認識できない
# 実行結果は正しく認識できているが，最新版では認識できるのか
print(len('abc'))
print(len('日本語'))

#キャラクターコード文字列は文字コードに相互変換できる
# 文字を文字コードに変換する
print(ord('a'))
# Unicodeも同様に変換できる
print(ord(u'a'))
# 文字コードを文字に変換できる
print(chr(97))

#python3からはデフォルトの文字列がUnicodeになり，
# それまでのバイト文字列がbytes型とbytearray型として新たに定義された

#bytes型
# 文字列型との連結時には明示的にエンコードを指定して文字列型かbytes型に統一する必要がある
print(b"abc")
print(bytes('あいう','utf8'))

#bytearray型
# 変更可能なバイト文字列として追加された．主にバイナリの扱いに利用される
# strは文字コードの指定が必要
a = bytearray('abc', 'utf8')
print(a)
#append, remove, popなどリストのようなこともできる
b = bytearray(a)
b.append(100)
print(a.pop(2))
print(a)
print(b)