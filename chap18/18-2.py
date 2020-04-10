#JSONデータの変換
#jsonモジュール
# JSONはweb上でよく利用されるデータ形式の一つ
# python2.6以降からはjsonモジュールが利用可能

#エンコード・デコードファイル
# オブジェクトなどのストリーム上で直接jsonデータを変換する場合にはdump関数，loads関数を用いる
import json
obj = ['foo', {'bar':('baz',None,1.0,2)}]
# json形式に変換して文字列として出力
json_str = json.dumps(obj)
print(json_str)
print(type(json_str))
# json形式の文字列からpythonオブジェクトに変換
print(json.loads(json_str))

#独自のエンコード
# 処理型変換表で定義されていないPythonのデータ型はデフォルトで変換できない
# このような場合は独自の型変換を定義する必要がある
# 独自の型変換を行いながらエンコードするにはjson.JSONEncodeクラスを拡張し，
# defaultメソッドをオーバーライドして利用する
import datetime
class MyJSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, datetime.datetime):
            return str(o)
        else:
            return super(self.__class__, self).default(o)

obj = {'x':1, 'updateed':datetime.datetime.now()}
print(json.dumps(obj, cls=MyJSONEncoder))
#デフォルトだとエラー
#print(json.dumps(obj))
# TypeError: Object of type datetime is not JSON serializable