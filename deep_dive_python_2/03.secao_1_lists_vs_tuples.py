import sys
from dis import dis

# (1, 2, 3)
# Behind the scenes...
"""
Coloca a tupla em uma constante e retorna. Constant folding
Constant folding is the process of recognizing and evaluating constant expressions
at compile time rather than computing them at runtime.

0 LOAD_CONST 4 ((1, 2, 3, 'a'))
    2 RETURN_VALUE


Se usar uma lista
              0 BUILD_LIST               0
              2 LOAD_CONST               0 ((1, 2, 3, 'a'))
              4 LIST_EXTEND              1
              6 RETURN_VALUE

"""
from timeit import timeit
import sys

dis(compile('(1, 2, 3, "a")', 'string', 'eval'))

dis(compile('[1, 2, 3, "a"]', 'string', 'eval'))

print(timeit("(1, 2, 3, 4, 5, 6, 7, 8, 9)", number=10_000_000))

print(timeit("[1, 2, 3, 4, 5, 6, 7, 8, 9]", number=10_000_000))

def fn1():
    pass

dis(compile('(fn1, 10, 20)', 'string', 'eval'))


l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
t1 = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(id(l1), id(t1))

l2 = list(l1)
print(id(l1), id(l2))

# shallow copy of tuple
t2 = tuple(t1)
print(id(t1), id(t2))

print(timeit('tuple((1, 2, 3, 4, 5))', number=5_000_000))
print(timeit('list((1, 2, 3, 4, 5))', number=5_000_000))

# Storange Efficiency


t = tuple()
prev = sys.getsizeof(t)

for i in range(10):
    c = tuple(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i+1} items: {size_c}, delta = {delta}')

l = list()
prev = sys.getsizeof(l)
for i in range(10):
    c = list(range(i + 1))
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i + 1} items: {size_c}, delta = {delta}')


c = list()
prev = sys.getsizeof(c)
print(f'0 items: {prev}')
for i in range(255):
    c.append(i)
    size_c = sys.getsizeof(c)
    delta, prev = size_c - prev, size_c
    print(f'{i + 1} items: {size_c}, delta = {delta}')

# Retrieving elements

t = tuple(range(100_000))
l = list(t)

# implem. em cpython - acesso direto.
print(timeit('t[99_999]', globals=globals(), number=10_000_000))

# listas usam um mecanismo de acesso indireto
print(timeit('l[99_999]', globals=globals(), number=10_000_000))
























