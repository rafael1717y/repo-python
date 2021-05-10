a = 10

def my_func(n):
    c = n ** 2
    return c

def my_func2(n):
    print('global a:', a)
    c = a ** n
    return c

print(my_func2(2))


def my_func3(n):
    a = 20
    c = a ** n
    return c

print(a)
my_func(2)
print(my_func3(2))


def my_func4(n):
    global a
    a = 20
    c = a ** n
    return c

print(my_func4(2))
print(a)

def my_func5():
    global var
    var = 'hello world'
    return

my_func5()


# Agora a variável existe após a chamada da função
print(var)

a = 10

def my_func6():
    global a
    a = 'hello'
    print('global a:', a)

my_func6()

####
"""
a = 10
def my_func7():
    print('global a:', a) # não encontra a no escopo local
    a = 'hello world'  # a será considerado como local
    print(a)

my_func7()
"""
a = 10
f = lambda  n: print(a**n)
f(2)

# Obs.:
for i in range(10):
    x = 2 * i

# x existe fora do loop. Diferente de alguns java, por exemplo.
print(x)































