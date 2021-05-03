# () are used to make the tuple clearer
#
a = 1, 2, 3
b = 1,
print(type(b)) #tuple

"""Packed values
Any iterable can be considered a packed value.
"""

a, b, c = [1, 2, 3]  #tupla com 3 variáveis - a = 1, b = 2, c = 3.

a, b, c = 10, 20, 'hello'
a, b = 10, 20

for e in 10, 20, 'hello':
    print(e)

# Simple application of unpacking - swapping values
a, b = b, a

d = {'key1':1, 'key2':2, 'key3': 3}

#for e in d: -- e iterates throught the keys: 'key1'....
# When upacking d, we are actually unpacking the keys of d
"""
They can be iterated, but there is no guarantee the order of the results.
a, b, c = d
# a = 'key1', b = 'key2, c = 'key3' or
# a = 'key2', b = 'key1, c = 'key3', --- 
"""

a = (1, 2, 3)

a = (1,)
print(type(a))

a = 100,
print(type(a))

a = ()  # para criar uma tupla vazia é necessário ()

a, b, c = [1, 'a', 3.14] #não é necessário homogeneidade dos elementos
print(a)
(a, b, c) = [1, 2, 3]

(a, b) = (1, 2)

a, b = 10, 20
print(a)
print(b)

a, b, c = 10, {1, 2}, ['a', 'b']

# Swapping
a, b = 10, 20
a, b = b, a
print(a)
print(b)

for e in 'XYZ':
    print(e)

a, b, c = 'XYZ'
print(a)

s = {'p', 'y', 't', 'h', 'o', 'n'}
print(s)

for e in s:
    print(e)

a, b, c, d, e, f = s
print(a)
print(b)

d = {'a':1, 'b':2, 'c':3, 'd':4}
a, b, c, d = d
print(a)

d = {'a':1, 'b':2, 'c':3, 'd':4}
d, a , b, c = d
print(d)
print(a)

for i in d:
    print(i)

d = {'a':1, 'b':2, 'c':3, 'd':4}
for i in d.values():
    print(i)

a, b, c, d = d.values()
print(a)

dict1 = {'a':1, 'b':2, 'c':3, 'd':4}
for a, b in dict1.items():
    print('key={0}, value={1}'.format(a, b))







































