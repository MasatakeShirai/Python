#スコープ
# 関数内で定義した変数は関数内でしか参照できない
GLOBAL_VAR=123

#グローバル変数は関数内でも利用できる
def func1():
    print(GLOBAL_VAR)

#関数内で変更してもそれはローカル変数として扱われる
def func2():
    GLOBAL_VAR=345
    print(GLOBAL_VAR)

#関数内でグローバル変数を扱いたい時はglobal文で明示的に示す
def func3():
    global GLOBAL_VAR
    GLOBAL_VAR =456

func1()
func2()
print(GLOBAL_VAR)
func3()
print(GLOBAL_VAR)

#globals()でスコープ内のグローバル変数を，locals()でローカル変数を得られる
def func4():
    x=1
    y=2
    print(globals())
    print(locals())

func4()

#python3ではネスト↓関数内で親関数の変数を操作できる
def func5():
    out_var = 135
    print(out_var)
    
    def inner_func():
        nonlocal out_var
        out_var = 246
    
    inner_func()
    print(out_var)

func5()
