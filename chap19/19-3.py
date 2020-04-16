'''
CGI連携
ウェブサーバにデフォルトに備わっているCGIからPythonを呼び出す
'''
'''
Apachの設定
httpd.confもしくはhtaccessで以下のように設定を行う
#AddHander cgi-script .cgi
AddHander cgi-script .cgi .py
そしてPythonのスクリプトファイルを実行可能なものにする
'''
'''
基本的な出力方法
リクエストに対してtext/plain方式の出力を行う時，次のようにする
#!/usr/bin/python

print('Content-Type: text/plain')
print('')
print('hello')
'''
'''
デバック出力（cgitbモジュール）
cgitbモジュールのenable関数をあらかじめ呼び出して設定をすると，
例外が発生した時に，その内容をHTML形式で画面に表示するようになる
#!/usr/bin/python
import  cgitb
cgitb.enable()

print('Content-Type: text/html; charset=utf8')
print('')
'''
'''
GET・POST値の取得（cgiモジュール）
#!/usr/bin/python
import  cgi
print('Content-Type: text/plain;)
print('')
form = cgi.FieldStorage()

print('Name=%s' % form.getfirst('name',''))
print('Age=%s' % form.getfirst('age',''))
'''
'''
Cookieを読み込む
#!/usr/bin/python
import  os
form cookie import SimpleCoolie

print('Content-Type: text/plain;)
print('')

if 'HTTP_COOKIE' in os.environ:
    print(os.environ['HTTP_COOKIE']) 未加工のクッキー文字列
    cookie = SimpleCookie() クッキーオブジェクトを取得　 
    cookie.load(os.environ["HTTP_COOKIE"]) 現クッキー情報をオブジェクトへ読み込み
    if 'key' in cookie:
        print(cookie['key'].value) keyを指定して値を取り出せる
'''
'''
Cookieへ書き込む
#!/usr/bin/python
import  os
form cookie import SimpleCoolie

cookie = SimpleCookie()

if 'HTTP_COOKIE' in os.environ:
    cookie.load(os.environ["HTTP_COOKIE"]) 

cookie['key'] = value クッキーに値を入れる

print('Content-Type: text/plain')

print(cookie.output())
print('')
print('Set key=VALUE')
'''
