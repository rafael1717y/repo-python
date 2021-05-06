import random

l = [1, 5, 4, 10, 9, 6]

print(sorted(l))

l = ['c', 'B', 'D', 'a']
print(sorted(l))

# Na ordem lexográfica 'A' vem antes de 'a'.
print(ord('a'))
print(ord('A'))

# Usando um ordem que é case insensitive.

print(sorted(l, key=lambda s: s.upper()))

d = {'def': 300, 'abc': 200, 'ghi':100}
print(d)

for e in d:
    print(e)

print(sorted(d))

# Ordenando o dicionário com base nos valores

print(sorted(d, key=lambda e: d[e]))

# Números complexos. Sorted sem builtin para números complexos.

def dist_sq(x):
    return (x.real) **2 + (x.imag) **2

print(dist_sq(1+1j))

l = [3 + 3j, 1-1j, 0, 3 +0j]
print(sorted(l, key=dist_sq))

sorted(l, key=lambda  x : (x.real)**2 + (x.imag) **2)


l = ['Cleese', 'Idle', 'Palin', 'Chapman', 'Gilliam', 'Jones']
print(sorted(l))

print(sorted(l, key= lambda s: s[-1]))

# Randomizing an iterable using sorted
l  = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(sorted(l, key=lambda x: random.random()))







