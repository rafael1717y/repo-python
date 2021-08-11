l = [1, 2, 3, 4, 5]
print(id(l))

print(l[0:3])

# Substituição dos elementos da lista
l[0:3] = 'python'
print(id(l), l)

l = [1, 2, 3, 4, 5]
print(id(l))

print(l[2:5])

# Deletando...
l[2:5] = []
print(id(l), l)

# len('') -> 0 -- substituindo por nada.
l = [1, 2, 3, 4, 5]
print(id(l))
l[2:5] = ''
print(id(l), l)

l = [1, 2, 3, 4, 5]
print(id(l))

# Regular slice object []
print(l[2:2])
s = slice(2, 2)
print(s.start)

#
l = [1, 2, 3, 4, 5]
print(id(l))
l[2:2] = ('a', 100, 500)
print(id(l), l)

t = (1, 2, 3, 4, 5)
print(t[0:3])

# 6 - Sem garantia de ordem
l[0:3] = {100, 'X', 'a'}
print(id(l), l)

# EXTENDED SLICES

l = [1, 2, 3, 4, 5]
print(id(l))

print(l[0:5:2])

# Deve ser do mesmo tamanho
l[0:5:2] = 'abc'
print(id(l), l)

l[0:5:2] = [1, 3, 5]
print(l)

#
#l[0:5:2] = [1, 3, 5, 4]















