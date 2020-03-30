#ファイルライクオブジェクト
# ファイルではないがファイルの様に扱えるオブジェクトをファイルライクオブジェクトという
# メソッドは基本的にファイルオブジェクトと同じだが，何度もすべての値を返すgetvalueメソッドを持つ
import io
output = io.StringIO('abc')
print(output.read())

output = io.StringIO()
output.write('abc\n')
output.write('def\n')
print(output.getvalue())
print(output.seek(0))
print(output.readlines())
