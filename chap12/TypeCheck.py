#デコレータの応用例
# 引数の型チェック

#チェック基準の型をシーケンス型で受け取る
def accepts(*types):
    def _accepts(f):
        def new_f(*args,**kwds):
            #zipはイテラブルオブジェクトの要素をまとめる
            # typsには引数としてstrとintが入る
            # argsにはduplicateが呼ばれた時の引数が入る
            for arg, type_ in zip(args, types):
                #isinstanceは第1引数にオブジェクト，第二引数に型名を取る
                if not isinstance(arg, type_):
                    raise TypeError('%s -> %s'%(arg, type_))                    
            return f(*args, **kwds)
        return new_f
    return _accepts

@accepts(str, int)
def duplicate(text, count):
    return ''.join(map(lambda x: ''.join(x), zip(*(text,)*count)))

duplicate('python', 3)
duplicate('pyrhon', 3.1)
