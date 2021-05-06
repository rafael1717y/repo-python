"""
Anonymous functions or lambdas are not equivalent to closures.
lambda [parameter list]: expression  -> return a function object
keyword  option :(required)    expressão avaliada (body of the function)

It can be assigned to a variable, passed as an argument to another function.
Limitations:
    - The 'body' of a lambda is limited to a single expression.
    - no assignments
    - no annotations
"""
my_func = lambda x: x**2  # colocando em uma variável my_func
print(my_func(3))
print(type(lambda  x: x**2))

lambda x, y: x + y
lambda : 'hello'
lambda s : s[::-1].upper()


def apply_func(x, fn):
    return fn(x)

apply_func(3, lambda x: x**2)
apply_func(2, lambda x: x+5)
print(apply_func('abc', lambda x: x[1:] * 3))

# equivalently

def fn_1(x):
    return x[1:] * 3

def sq(x):
    return  x**2

lambda x : x**2

lambda x, y : x + y

f = sq

f(3)
sq(3)

f = lambda x : x**2
print(f(2))

g = lambda x, y=10: x * y

print(type(g))
print(g(1, 2))

f = lambda x, *args, y, **kwargs : (x, args, y, kwargs)

print(f(1, 'a', 'b', y=100, a=10, b=20))

def apply_func2(fn, *args, **kwargs):
    return fn(*args, **kwargs)

apply_func2(sq, 3)

apply_func2(lambda x : x **2, 3)

apply_func2(lambda x, y: x+y, 1, 2)

apply_func2(lambda x, *, y: x *y, 1, y=20)

print(apply_func2(lambda *args: sum(args), 1, 2, 3, 4, 5))























