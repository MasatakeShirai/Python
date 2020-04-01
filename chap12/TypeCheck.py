#デコレータの応用例
# 引数の型チェック
def accepts(*types):
    def _accepts(f):
        def new_f(*args,**kwds):
            for arg, type_ in zip(args, types):
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
