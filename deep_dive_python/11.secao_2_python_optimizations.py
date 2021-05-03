"""
Optimazation strategy - small integer show up often
At startup, cpython preloads (caches) a global list of integers in the range [-5, 256]

When we write a = 10
python just has to point to the existing reference for 10

But if we write a = 257 - python does not use that global list and a new object is created
every time.
"""

# 01. Msm objeto uma vez que 10 está no range de -5 a 256.
a = 10
b = 10
print(id(a))
print(id(b))

a = -5
b = -5
print(id(a))
print(id(b))

a = 257000
b = 257000
print(a is b) # até versão 3.6 era False

a = 10
b = int(10)
c = int('10')
d = int('1010', 2)
print(a, b, c, d)
print(id(a), id(b), id(c), id(d))

"""Some strings are also automatically interned - but not all
Not all strings are automatically interned by Python. But you can force strings to be interned by using the sys.intern() method.
Usar qdo: dealing with a large number of strings that could have high repetition, lots os string comparisons. 
"""
# 01. hello será internalizado pois se parece com um identificador
a = 'hello'
b = 'hello'
print(id(a))
print(id(b))

# 02. Pode não acontecer
a = 'hello world'
b = 'hello world'
print(id(a))
print(id(b))

print(a == b)
print(a is b)

a = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
b = '_this_is_a_long_string_that_could_be_used_as_an_identifier'
print(a is b)

# 03. forçando string internalization

import sys
a = sys.intern('hello world')
b = sys.intern('hello world')
c = 'hello world'
print(id(a), id(b), id(c))

print(a == b) ## compara caracteres com caracteres -- é mais lento.

# 04.

def compare_using_equals(n):
    a = 'a long string that is not interned' * 200
    b = 'a long string that is not interned' * 200

    for i in range(n):
        if a == b:
            pass

def compare_using_interning(n):
    a = sys.intern('a long string that is not interned' * 200)
    b = sys.intern('a long string that is not interned' * 200)

    for i in range(n):
        if a is b:
            pass

import time

# 1.47
start = time.perf_counter()
compare_using_equals(10000000)
end = time.perf_counter()
print('equality', end - start)


# 0.25
start = time.perf_counter()
compare_using_interning(10000000)
end = time.perf_counter()
print('equality', end - start)
