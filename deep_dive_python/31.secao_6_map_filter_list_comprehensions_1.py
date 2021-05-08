"""High order functions:
A function that takes a funcion as a parameter and/or return a function as its return value.
Ex. sorted, map, filter

The map function
map (func, *iterables)

*iterables - a variable number of iterable objects
func - some function that takes as many arguments as there are iterable passed to iterable
map will the return an iterator that calculates the function applied to each element of the iterabe.

"""
# 01.
l = [2, 3, 4]

def sq(x):
    return x**2

print(list(map(sq, l)))  # [4, 9, 16]

# 02.
l1 = [2, 3, 4]
l2 = [10, 20, 30]

def add(x, y):
    return x + y

print(list(map(add, l1, l2)))
print(list(map(lambda x,y: x+ y, l1, l2)))

# 03. Filter
"""
filter(func, iterable)
iterable - a single iterable
func -- some function that takes a single argument
retorna um iterável. If the function is None, it simply returns the elements of iterable that are Truthy.
"""

l = [0, 1, 2, 3, 4]  # 0 é falso

print(list(filter(None, l)))

def is_even(n):
    return n %2 == 0

# filtrando os pares
print(list(filter(is_even, l)))
print(list(filter(lambda n: n % 2 == 0, l)))


"""The zip function

zip(*iterables) --- recebe um número arbitrável de iteráveis

"""
l1 = [1, 2, 3]
l2 = [10, 20, 30]
l3 = ['a','b', 'c']

print(list(zip(l1, l2, l3)))  # [(1, 10, 'a), (2, 20, 'b'), ...]

l1 = [1, 2, 3, 4, 5]
l2 = [20, 20, 30]

print(dict(zip(l1, l2)))   # deixa de fora os correspondentes e 4 e 5.

l1 = [1, 2, 3]
l2 = [10, 20, 30, 40]
l3 = 'python'

print(list(zip(l1, l3, l3)))  #[(1, 'p', 'p'), (2, 'y', 'y'), (3, 't', 't')]

# Descobrindo o índice de cada caractere na string 'abcd' para obter o índice e o caracter juntos.

l1 = range(100)
l2 = 'abcd'

print(list(zip(l1, l2)))

# LIST COMPREHENSIONS -
# [<expression1> for <varname> in <iterable> if <expression2>]

l = [2, 3, 4]

def sq(x):
    return x **2

print(list(map(sq, l)))

result = []
for x in l:
    result.append(x **2)

print([x**2 for x in l])

l1 = [1, 2, 3]
l2 = [10, 20, 30]

print(list(map(lambda x, y: x + y, l1, l2)))

print([x + y for x, y in zip(l1, l2)])

l = [1, 2, 3, 4]

print(list(filter(lambda  n: n %2 == 0, l)))
print([x for x in l if x % 2 == 0])

l = range(10)

print(list(filter(lambda y: y < 25, map(lambda x: x**2,l))))

print([x**2 for x in range(10) if x**2 < 25])