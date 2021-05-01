from math import sqrt

print(sqrt(4))

def func_1():
    print('running func_1')

func_1()

# Apenas para documentação
def func_2(a: int, b: int):
    return a + b

print(func_2(2, 3))
#print(func_2("a", 3))


def func_3():
    return  func_4()

def func_4():
    return 'running func4'

# func_4 ainda não existe em func_3 mas é chamada imprimindo 'running func4'.
print(func_3())

"""
# Erro uma vez que func_6 naõ está definida antes da chamada de func_5.
def func_5():
    return func_6()

print(func_5())

def func_6():
    print('running func_6')
"""

my_func = func_4()
print(my_func)

fn1 = lambda x: x **2
print(fn1)

print(fn1(2))













