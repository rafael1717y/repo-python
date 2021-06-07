l1 = [1, 2, 3, 4]
l2 = [5, 6]

print(id(l1), l1)
print(id(l2), l2)

# Dif. end. memória
l1 = l1 + l2
print(id(l1), l1)

# 2.
l1 = [1, 2, 3, 4]
l2 = [5, 6]

print(id(l1), l1)
print(id(l2), l2)

# Id é o mesmo que era antes. l1 -> mutated
l1 += l2
print(id(l1), l1)

# 2.
l1 = [1, 2, 3, 4]
t1 = (5, 6)

print(id(l1), l1)
print(id(t1), t1)

# += in place concatenation
l1 += t1
print(id(l1), l1)

# extendido com o range - id é o msm
l1 += range(7, 11)
print(id(l1), l1)

#4. Sem ordem
l1 = {100, 'X', 'a'}
print(id(l1), l1)

#5. End. de memória mudou...

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(id(t1), t1)
print(id(t2), t2)

# t1 é um tipo de sequencia imutável. Cria outro obj.
t1 += t2
print(id(t1), t1)


# 6.
l1 = [1, 2, 3]
print(id(l1), l1)

l1 = l1 * 2
print(id(l1), l1)

# 7.

t1 = (1, 2, 3)
print(id(t1), t1)

t1 *= 2
print(id(t1), t1)
