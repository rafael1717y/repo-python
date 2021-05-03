"""
In a 32-bit OS:
    memory spaces (bytes) are limited by their address number -> 32 bits
    2 ** 32 ->
How large an integer can be dependes on how many bits are used to store the number.
Java -> byte (signed 8-bit numbers) - 128,..., 127
        short - 32.768, ..., 32.767
        int signed 32-bit numbers

PYthon: the int object uses a variable number of bits.
Theoreticaly limited only by the amount of memory available.
"""
print(type(100))

import sys

# Usa-se ao menos 24 bytes para criar um int.
print(sys.getsizeof(0))
print(sys.getsizeof(1)) # + 4
print(sys.getsizeof(2 ** 1000)) # 160

import time

def calc(a):
    for i in range(10000000):
        a * 2

start = time.perf_counter()
calc(10)
end = time.perf_counter()
print(end - start)

start = time.perf_counter()
calc(2 ** 10000)
end = time.perf_counter()
print(end - start)

"""
floor(3.14) - 3
flooar(1.99( - 1
floor(-3.1) --> 4 --- floor is not quite the same as truncation!
"""

import math
print(math.floor(3.15))
print(math.floor(-3.14))
print(math.floor(-3.0000001))

a = 33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))

a = -33
b = 16
print(a/b)
print(a//b)
print(math.floor(a/b))
print(math.trunc(a/b))


a = b * (a //b) + (a % b)
a = 13
b = 4

print('{0}/{1} = {2}'.format(a, b, a/b))
print('{0}//{1} = {2}'.format(a, b, a//b))
print('{0}%{1} = {2}'.format(a, b, a%b))
print(a == b * (a //b) + (a % b))
