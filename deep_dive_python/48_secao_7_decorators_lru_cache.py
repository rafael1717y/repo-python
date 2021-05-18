from functools import lru_cache

"""
maxsize = None -> cache ilimitado
Usar cache com potência de 2
"""
@lru_cache(maxsize=8)
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(8)
print("===")
print(fib(8))
fib(9)
print(fib(9))
fib(1)