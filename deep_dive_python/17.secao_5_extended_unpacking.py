"""
Unpacking não necessita de coleções indexáveis. É mais genérico que slicing.
"""

l = [1, 2, 3, 4, 5, 6]
a, *b = l

print(a)
print(b)

a, *b = [-10, 5, 2, 100]
print(a)   # 10
print(b)

a, *b = (-10, 5, 2, 100)
print(a)   # 10
print(b)

# Com strings

a, *b = 'XYZ'
print(a)
print(b)

a, b, *c = 1, 2, 3, 4, 5
print(a)
print(b)
print(c)

a, b, *c, d = [1, 2, 3, 4, 5]
print(a)
print(b)
print(c)
print(d)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
l = [*l1, *l2]
print(l)

"""
# não usar pq a ordem não é garantida.
s = {10, -99, 3, 'd'}
print(s)
a, *b, c = s
print(a)
print(b)
"""
d1 = {'p':1, 'y': 2}
d2 = {'t':3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}

# Desempacotando os dicionários em listas

l = [*d1, *d2, *d3]
print(l)

# Em sets
s = {*d1, *d2, d*2}

# The ** unpacking operator

d1 = {'p':1, 'y': 2}
d2 = {'t':3, 'h': 4}
d3 = {'h': 5, 'o': 6, 'n': 7}

# The ** operator cannot be used in the lhs of an assignment
# O valor de h em d3 sobrescreveu o o primeiro valor de h em d2.

d = {**d1, **d2, **d3}
print(d)

l = [1, 2, [3, 4]]

a, b, c = l
print(c)

d, e = c

# Nested unpacking

a, b, (c, d) = [1, 2, [3, 4]]

a, *b, (c, d, e) = [1, 2, 3, 'XYZ']
print(a)
print(b)
print(c)


a, *b, (c, *d) = [1, 2, 3, 'python']
print(c)
print(d)

# Slicing x Extendend unpacking
l = [1, 2, 3, 4, 5, 6]

a = l[0]
b = l[1:]
print(a)
print(b)

a, b = l[0], l[1:]
print(a)
print(b)


a, *b = l
print(a)
print(b)

# Set does not support indexing
#s = {1, 2, 3}
#s = s{0}

s = 'python'
a, *b = s
print(a)
print(b)

t = ('a', 'b', 'c')

a, *b = t
print(a)
print(b)

[a, b, c] = 'XYZ'
print(a)

a, b, *c = 'python'
print(a)
print(b)
print(c)

a, b, *c, d = s
print(a)
print(b)
print(c)
print(d)

s = 'python'

a, b, c, d  = s[0], s[1], s[2:-1], s[-1]
print(a)
print(b)
print(c)
print(d)

# Passar para lista

*c, = c
print(c)
# ou
print(list(c))

# Juntando dois iteráveis
li = [1, 2, 3]
l2 = [4, 5, 6]

l = [*l1, *l2]
print(l)

l1 = [1, 2, 3]
s = 'abc'
print(*l1, *s)

s1 ='abc'
s2 = 'cde'
print([*s1, *s2])

# Sem repetir
print({*s1, *s2})

s = {10, -99, 3, 'd'}

for c in s:
    print(c)

a, b, c, d = s

# Não útil uma vez que sets não garantem a ordem.
a, b, *c = s
print(a)

# De conjunto para lista
list(s)
*c, = s
print(c)

# Unindo sets
s1 = {1, 2, 3}
s2 = {3, 4, 5}

s = {*s1, *s2}
print(s)

print(help(set))
s1.union(s2)

s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = {5, 6, 7}
s4 = {7, 8, 9}

s1.union(s2).union(s3).union(s4)
s1.union(s2, s3, s4)

print({*s1, *s2, *s3, *s4})
print([*s1, *s2, *s3, *s4])

d1 = {'key1': 1, 'key2' : 2}
d2 = {'key2': 3, 'key4' :3}

# Unindo os dicionários
# * só para as chaves
keys = {*d1, *d2}
print(keys)

keys_values = {**d1, **d2}
print(keys_values)

print({'a': 1, 'b':2, **d1, 'c':3})

# Unpacking e slicing

a, b, e = [1, 2, 'XY']
a, b, (c, d) = [1, 2, 'XY']
a, b, (c, d, *e) = [1, 2, 'python']

l = [1, 2, 3, 4, 'python']
a, *b, (c, d, *e) = l
print(a, b, c, d, e)

a, b, c, d, e = l[0], l[1:-1], l[-1][0], l[-1][1], list(l[-1][2:])
print(a, b, c, d, e)
