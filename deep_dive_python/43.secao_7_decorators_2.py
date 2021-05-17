from functools import wraps

def counter(fn):
    count = 0
    @wraps(fn)
    def inner(*args, **kwargs):  # genérico pq inner chamará counter
        nonlocal count
        count += 1
        print('Função {0} (id={1}) foi chamada {2} vezes'.format(fn.__name__, id(fn), count))
        result = fn(*args, **kwargs) # chamar fn com o que passou para inner
        print(result)
        return result
    # ou inner = wraps(fn)(inner)
    return inner

def add(a:int, b:int=0):
    """
    Adiciona dois valores
    """
    return a + b

# add da linha 14
print(help(add))
print(id(add))

## o primeiro add é o closure retornado. São funções diferentes
add = counter(add)
print(id(add))
print(help(add))  # add -- inner function

print(add(10, 20))

print(add(20, 40))

print(add(10))

def mult(a:int, b:int, c:int=1, *, d):
    """
    multiplica cinco valores
    """
    return a * b * c * d

# M1.
print(mult(1, 2, 3, d=4))
print(mult(1, 2, d=3))

# M2 c/closure
mult = counter(mult) # o primeiro mult é o decorator da função
print(mult)
print(help(mult)) # primeiro mult é o closure. Não a função mult, mas

print(mult(1, 2, 3, d=4)) # cálculo efetuado e tbm imprimirá função mult (id=xx) foi chamada 1 x.
print(mult(1, 2, d=3))

# M3 -

def my_func(s:str, i:int) -> str:
    return s * i

my_func = counter(my_func)

@counter
def my_func(s:str, i:int) -> str:
    return s * i

my_func('a', 10)

print(help(my_func))
print(mult.__name__)


def mult(a:int, b:int, c:int=1, *, d):
    """
    multiplica cinco valores
    """
    return a * b * c * d

mult = counter(mult)
print(help(mult))
