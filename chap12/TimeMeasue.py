#デコレーターの応用例
# 時間計測
def timing(f):
    import time
    def new_f(*args, **kwds):
        #プログラム実行前のシステム時間を取る
        t = time.time()
        #対象の実行
        result = f(*args, **kwds)
        #関数の名前と対象の実行時間を表示
        print('%s: %ss'%(f.__name__, time.time()-t))

        return result
    return new_f

@timing
def func():
    import time
    #1秒待つ
    time.sleep(1)
