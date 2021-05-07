"""
# Different types of callables - methodos, user-defined functions, methods, classes, generators...
#
MyClass(x, y, z)
    __new__(x, y, z) --> creates the new objetc
    __init__(self, x, y, z)
    --> returns the object(referecen)
"""


# Callable
print(callable(print))
print(callable(str.upper))
print(callable(callable))

# Não callable
print(callable(10))

result = print('hello')
print(result)

l = [1, 2, 3]
print(callable(l.append))
result = l.append(4)
print(l)
print(result)

from decimal import Decimal
print(callable(Decimal))

a = Decimal('10.5')
print(a)

class MyClass:

    def __init__(self, x=0):
        print('inicializando...')
        self.counter = x

print(callable(MyClass))

a = MyClass(100)
print(a.counter)

# A instância da classe não é callable até aqui.
print(callable(a))

# Fazendo instâncias da classe se tornarem callables através do método __call__

class MyClass:

    def __init__(self, x=0):
        print('inicializando...')
        self.counter = x

    def __call__(self, x=1):
        print('updating counter')
        self.counter += x

b = MyClass()
MyClass.__call__(b, 10)
print(b.counter)

# b agora é callable
print(callable(b))
b()
b(100)







