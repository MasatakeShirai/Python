#キー値を指定して値を呼び出し
#一致するキーがないときは例外が発生
a = {'you':'that', 'me':'this'}
print(a['you'])

#getメソッドを利用して呼び出し
#一致するキーがないときはNoneを返すか，デフォルトに設定した値を返す
print(a.get('me'))
print(a.get('him'))
print(a.get('her','new'))

#キーと値のリストを取得する
print(a.keys())
print(a.values())
print(a.items())

#キーの存在を確認する
print('me' in a)
print('her' in a)
print('him' in a.keys())

#辞書の構成要素数を取得
print(len(a))
