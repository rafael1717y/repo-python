"""
Reducing functions in python are functions that recombine an iterable recursively,
ending up with a single retunr value.
"""

# Ex. 01 - Finding the maximum value in a iterable
l = [5, 8, 6, 10, 9]

max_value = lambda a, b : a if a >b else b

def max_sequence(sequence):
    result = sequence[0]
    for e in sequence[1:]:
        result = max_value(result, e)  # result = max(5,8)
    return result

# Como para encontrar o mínimo é semelhante é possível usar uma padrão.
# fn =  max_value

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(_reduce(lambda a, b: a if a > b else b, l )) # maximum

print(_reduce(lambda a, b: a if a < b else b, l )) # minimum

# Adding all the elemnts in a list

add = lambda a, b: a + b

l = [5, 8, 6, 10, 9]

def _reduce(fn, sequence):
    result = sequence[0]
    for x in sequence[1:]:
        result = fn(result, x)
    return result

print(_reduce(add, l))

# The functools module

from functools import reduce

l = [5, 8, 6, 10, 9]

# Usando reduce com qlq iterável
print(reduce(lambda a, b: a if a > b else b, l))
print(reduce(lambda a, b: a if a < b else b, l))
print(reduce(lambda a, b: a if a < b else b, {10, 5, 2, 4}))
print(reduce(lambda a, b: a if a < b else b, 'python'))

print(min([5, 8, 6]))
print(max([5, 8, 6]))
print(sum([5, 8, 6]))

# any(l) --- retorna True if any element in l is truthy - False otherwise
# all(l) ---

# Using reduce to reproduce any

l = [0, '', None, 100] # 100 é truthy

result = bool(0) or bool('') or bool(None) or bool(100)
print(result)

result = bool(0) # f
resul = result or bool('') #f
result = result or bool(None) # f
result = result or bool(100) # t

# == Any
print(reduce(lambda a, b : bool(a) or bool(b), l))

# Calculating the product of all elements in an iterable
# ------------------------------------------------------

l = [1, 3, 5, 6]

print(reduce(lambda a, b : a * b, l))

# Calculating n!
# --------------
# 5! = 1 * 2 * 3 * 4 * 5

range(1, 6)  # se multiplicar esses números do range encontramos o fatorial de 5

print(reduce(lambda a, b: a * b, range(1, 5+1) ))

# The reduce initializer
"""
The reduce funtion has a third (option) parameter: initializer (defaults to None).
!! Soma de uma lista usar um initializer de 0 pq nao afeterá a lista.
!! Para multiplicação usar initiailzer igual 1. 

"""

l = []
# print(reduce(lambda x, y: x + y, l)) -- > exception

l = []
print(reduce(lambda x, y: x + y, l, 1))  # initializer = 1

l = [1, 2, 3]
print(reduce(lambda x, y: x + y, l, 100))  # 106


































