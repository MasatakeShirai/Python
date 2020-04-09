#正規表現
#reモジュールの基本
# 基本的な流れ
import re
# 正規パターンをコンパイルし，正規表現オブジェクトを作成
pattern = re.compile('Python')
# 文字列に対して検索を行い，マッチオブジェクトを取得
result = pattern.search('The Zen of Python, by Tim Peters')

#結果を利用する
if result is None:
    print('NG')
else:
    print('OK')

#正規表現オブジェクトを生成
# 文字列をコンパイルして，正規表現オブジェクトを生成する
pattern = re.compile('[pP]ython')
print(pattern.search('Python'))

# コンパイルする手順を省きたければreモジュール直下に定義された同名の関数群が有用
print(re.search('[pP]ython', 'python'))

#検索：search
# 存在しない時はNoneになる
print(pattern.search('Java, python, C'))
print(pattern.search('PHP, Java, C'))

#match：照合
# 正規表現パターンで照合する．searchと違い，文字列の先頭のみにマッチする
print(pattern.match('python, Java, C'))
print(pattern.match('PHP, python, C'))

#sub：置換
# 正規表現パターンでマッチした部分を置換する
print(pattern.sub('py', 'python, Java, C'))

#修飾子
# 正規表現修飾子とは正規表現ぱｗの判定を変更するためのオプション．compileの引数として利用できる
# 大文字小文字を区別しない
pattern = re.compile('[a-z]',re.I)
print(pattern.sub('*', 'abC-dEf'))

#raw string記法
# \文字が含まれる場合にはraw string記法を用いると読みやすくなる
regex = re.compile(r'\\')
print(regex.sub('E', r'\a\b\c'))

#部分一致
# 正規表現の中で（）で囲んだ部分がグループとなり，部分一致として抽出される
pattern = re.compile(r'(\d+)\.(\d+)\.(\d+)\.(\d+)')
result = pattern.search('192.168.0.1')
print(result.groups())

# それぞれの部分一致に名前をつける機能がある．
pattern = re.compile('(?P<first_name>[a-z]+) (?P<last_name>[a-z]+)',re.I)
result = pattern.search('Johne Lennon')
print(result.group('first_name'))
print(result.group('last_name'))
print(result.groupdict())
print(result.groups())

#後方参照
# 部分一致内容を直後の置換で利用する機能のこと
# 置換文字列に\1,\2...と記述することで取得できる
pattern = re.compile(r'(\d{3})(\d{4})')
print(pattern.sub(r'\1-\2', '1010021'))

#findall(手軽に部分一致)
# 部分一致したキーワードを手軽に抽出する
html = '<a href="http://www.python.org/">Python official Website</a>'
print(re.findall('<a href="(http://[^"]+?)">([^<]+?)</a>', html))

#spit(正規表現で文字列分割)
# 正規表現で一致した文字列の部分で文字列全体を分割
pattern = re.compile(' +')
print(pattern.split('aaa bbb ccc ddd'))

#escape(メタ文字をエスケープ)
# すべてのメタ文字をエスケープ↓文字列を返す．
# 動的に正規表現パターンを生成するような場合に有効
print(re.escape('abc123^$?+*'))

#先読みと後読み
# 先読み
pattern =re.compile('lookahead(?=,)')
print(pattern.search('lookahead'))
print(pattern.search('lookahead,'))
# 後読み
pattern =re.compile('(?<=,)lookbehind')
print(pattern.search('lookbehind'))
print(pattern.search(',lookbehind'))
