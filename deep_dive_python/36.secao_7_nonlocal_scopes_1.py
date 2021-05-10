"""We can define functins from inside another function"""
a = 10

def outer_func():
    pass
    # some code

    def inner_func():
        pass

    inner_func()


outer_func()

# Both functions have access to the global e buit-in scopes as well as their respective local scopes.
# But the inner function also has access to its enclosing scope - the scope of the outer function.
# That scope is neither local (to inner_func) nor global -- its called a nonlocal scope.


def outer_func():
    x = 'hello'
    def inner_func():
        print(x)
    inner_func()


outer_func()

def outer_func2():
    x = 'hello'
    def inner1():
        def inner2():
            print(x)
        inner2()
    inner1()

outer_func2()

def outer_func3():
    x = 'hello'
    def inner():
        x = 'python'
        print('inner', x)
    inner()
    print('outer', x)

outer_func3()

###
def outer_func4():
    x = 'hello'
    def inner():
        nonlocal x
        x = 'python' # será considerado local uma vez que há uma atribuição ao menos que torne nonlocal
        print('inner linha 57', x)
    print('outer (before)', x)
    inner()
    print('outer (after)', x)  # x modificado agora.

outer_func4()

###

def outer():
    x = 'hello'
    def inner1():
        print('inner1:', x)
        def inner2():
            nonlocal x
            x = 'python'
        inner2()
    inner1()
    print(x)

outer()


def outer5():
    x = 'hello'
    print('linha 82', x) # x = hello
    def inner1():
        nonlocal x  # aponta para mais um nível
        x = 'python'
        print('linha 85', x)
        def inner2():
            nonlocal x  # aponta para uma nível acima
            x = 'monty'
        inner2()
    inner1()
    print(x) # x= monty

outer5()

x = 'python'

def outer7():
    #global x -> erro
    x = 'monty'

    def inner():
        nonlocal x
        x = 'hello'
    inner()
    print(x) # hello

outer7()
print(x)














































