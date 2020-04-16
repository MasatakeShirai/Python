#ウェブの基本ツール
#HTTP通信を行う
#urllib2とurllibモジュール
# サーバからhttpリクエストを行い，webページやapiを利用する
import urllib.request
# リクエスト送信
response = urllib.request.urlopen('http://yahoo.co.jp/')
# コンテンツを抽出
content = response.read()
# HTTPヘッダ情報を抽出
headers = response.info()
print(headers['date'])

#GETパラメータを設定する
# dictをQuery Stringに設定する
import urllib.parse
params = {'alpha':'abc', 'space':' ', 'slash':'/'}
query_string = urllib.parse.urlencode(params)
print(query_string)
print('http://mydomein.com/?' + query_string)

#POSTリクエストを送信する
params = {'q':'keyword', 'page':'1'}
encoded_parms = urllib.parse.urlencode(params).encode('utf-8')
response = urllib.request.urlopen('http://yahoo.co.jp/',data=encoded_parms)

#HTTPヘッダの設定
opener = urllib.request.build_opener()
#opener.addheaders([....]) UserAgent設定を入れる
#response = opener.open('http://yahoo.co.jp/') 結果はurlopenと同じ

#タイムアウト時間の設定
import socket
# 初期値はNone
print(socket.getdefaulttimeout() is None)
# 30秒に設定
socket.setdefaulttimeout(30.0)
print(socket.getdefaulttimeout())

#リクエスト時のエラー処理
import urllib.error
socket.setdefaulttimeout(0.01)
try:
    response = urllib.request.urlopen('http://yahoo.co.jp/')
#サーバから404,403,500などが返されたときのエラー
except urllib.error.HTTPError as err:
    print('HTTPError')
#存在しないドメイン，サーバの問題で接続できない場合のエラー
except urllib.error.URLError as err:
    print('URLError')
    #エラーの原因がtimeoutなら，そのように表示する
    if isinstance(err.reason, socket.timeout):
        print('timeout')
else:
    print('OK')
