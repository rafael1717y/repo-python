"""
Any object can be assigned to a variable including functions
Ay object can be passed to a function including functions

my_func is the name of the function
my_func() invokes the function
"""

a = 10
print(type(a))

# a é uma instância da classe int logo é possível  criar outro objeto nos moldes da instanciação de um objeto b = int(10)

b = int(10)
print(b)
print(type(b))

print(help(int))

# Int são objetos, instâncias da classe int.
c = int()
print(c)

c = int('101', base = 2)
print(c)

# Retornando funções de outras funções

def square(a):
    return a **2

print(type(square))

f = square
# mesmo id
print(id(square))
print(id(f))
print(f is square)

print(square(2))
print(f(2))

def cube(a):
    return  a ** 3

def select_function(fn_id):
    if fn_id == 1:
        return square
    else:
        return cube

f = select_function(1)

print(f is square)

f = select_function(2)
print(f is square)

a = select_function(2)(3)
print(a)

# A função exec_function recebe uma função (fn) e um parâmetro n
def exec_function(fn, n):
    return fn(n)

exec_function(cube, 3)
exec_function(square, 3)