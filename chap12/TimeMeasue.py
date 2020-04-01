#デコレーターの応用例
# 時間計測
def timing(f):
    import time
    def new_f(*args, **kwds):
        t = time.time()
        result = f(*args, **kwds)
        print('%s: %ss'%(f.__name__, time.time()-t))

        return result
    return new_f

@timing
def func():
    import time
    time.sleep(1)

func()
