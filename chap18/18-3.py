#xmlデータの利用
# 柔軟で統一的な表現ができるデータ形式として広く利用されている
# pythonからxmlにアクセスするためにlxmlやBeautifulSoupといったモジュールがよく利用される

#xmlを解析する
from lxml import etree
xml = '<root><node1 key="val">leaf</node1><node2>flower</node2></root>'
root = etree.fromstring(xml)

# タグ名を取得するにはrootオブジェクトのtag属性を参照する
print(root.tag)

# 子ノードはリスト形式で格納されている
print(root[0].tag)

# タグ名を指定して子ノードを得るにはfindメソッドを使う
print(root.find('node1').tag)

# 複数のタグを取得するにはfindallメソッドを使う
print(root.findall('node1')[0].tag)

# タグ内部のテキストを取得するにはノードオブジェクトのtext属性にアクセスする
print(root[0].text)

# xmlの属性はノードオブジェクトの属性であるattrib辞書に格納されている
print(root[0].attrib)

# ノードオブジェクトを元のテキストに戻すには，etree.tostringメソッドを用いる
print(etree.tostring(root))

#xmlを編集する
# 初めにもとになるxmlをノードオブジェクトに変換
xml = '<root><node key="val">leaf</node></root>'
root = etree.fromstring(xml)

# appendメソッドで子ノードを追加する
child = etree.fromstring('<node2>leaf2</node2>')
root.append(child)
print(etree.tostring(root))

# xml属性の変更二もノードオブジェクトのattrib辞書を使う
child.attrib['key'] = 'value'
print(etree.tostring(root))

#XPathを使う
xml = '<root><node key="value"><node>leaf</node></node></root>'
root = etree.fromstring(xml)
# 子ノードの子ノードを取り出す
nodes = root.xpath('//node/node')
for node in nodes:
    print(etree.tostring(node))

# すべてのnodeノードを取り出す
nodes = root.xpath('//node')
for node in nodes:
    print(etree.tostring(node))

# 最上位の階層の1つ下のnodeノードを取り出す
nodes = root.xpath('/root/node')
for node in nodes:
    print(etree.tostring(node))

# key属性の値が"value"であるnodeノードを取り出す
nodes = root.xpath('//node[@key="value"]')
for node in nodes:
    print(etree.tostring(node))

# すべてのテキストを取り出す
texts = root.xpath('//text()')
for text in texts:
    print(text)