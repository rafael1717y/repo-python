"""Mutating an object means changing the object' states without creating
a new object. Concatenation is not mutation"""

l = [1, 2, 3, 4, 5]
print(id(l))
print(l[0])

# Apontando para o mesmo objeto com o conteúdo mutado.
l[0] = 'a'
print(l)
print(id(l))

l.clear()
print(l)
print(id(l))


suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
alias = suits
print(id(alias), id(alias))

# Acidentalmente modificando suits
alias.clear()
print(suits)

##

suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']

def something(l):
    l.append('None')


something(suits)
print(suits)

l = [1, 2, 3, 4, 5]
print(id(l))

print(l[0:2])

l[0:2] = ('a', 'b', 'c', 'd')

print(l)
print(id(l))

l = [1, 2, 3]
print(id(l))

# Muda o end. de memória.
l = l + [4]
print(l)

# O método append não muda o id. Não cria um novo objeto.
l = [1, 2, 3]
print(id(l))

result = l.append(4)
print(type(result)) # class NoneType
print(id(l))

l.append([1, 2, 3])
print(l)  # [1, 2, 3, 4, [1, 2, 3]]

# Extend

l = [1, 2, 3]
print(id(l))

l.extend([4])
print(l)

l.extend(['a', 'b', 'c', 'd'])
print(l)

# Extend com set

l = [1, 2, 3]
l.extend({'x', 'a', 'A', 100_000})
print(l) # a ordem não é garantida

l = [1, 2, 3, 4]
print(id(l))

# Pop
result = l.pop()
print(result)

print(l.pop(1))

# del

l = [1, 2, 3]
del l[1]
print(l)

# insert
l = [1, 2, 3, 4]
print(l)
l.insert(1, 'a')
print(l)

# reverse
l = [1, 2, 3]
l2 = l[::-1]
print(id(l))
print(id(l2))

l.reverse()
print(l)
print(id(l)) # msm obj com conteúdo mudado.

# copy

l = [1, 2, 3, 4]
print(id(l))
l2 = l[:]

# Slices retornam novos objetos
print(id(l))
print(id(l2))

# copy (shallow copy)
l3 = l.copy()
print(l3)
print(id(3)) # id diferente

l = [['a', 'b'], 'c', 'd']

print(id(l))
print(id(l[0]))
print(id(l[1]))

l2 = l.copy()
print(id(l2)) # dif

# A lista têm um end de memória diferente, mas os objetos que ela contém não.
# Se a cópia for modificado, a origem também será.
print(id(l2[0]), id(l2[1]))
