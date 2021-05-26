l = [1, 2, 3]
t = (1, 2, 3)
s = 'python'

print(l[0])

for c in s:
    print(c)

S = {10, 20, 30}

for e in s:
    print(e)

s = {'x', 10, 'a', 'A'}
for e in s:
    print(e)

#print(s[0]) -- set does not support indexing

l[0] = 100
print(l)

t = ([1, 2], 3, 4)

t[0][0] = 100
print(t)

print('a' in ['a', 'b', 100])
print(100 in range(200))

l = [2 + 2j, 10 + 10j, 100 + 100j]
#print(min(l))  < not support between instances of complex and complex

l = ['a', 'b', 'c']
print(min(l))

from decimal import Decimal

l = [10, 10.5, Decimal('20.3')]
print(min(l))

a = [1, 2, 3] + [3, 4, 6]
print(a)



c = list('abc') + ['d', 'e', 'f']
print(c)

d = '***'.join(['1', '2', '3'])
print(d)


e = ','.join(['1', '2', '3'])
print(e)

f = ''.join(list('abc') + ['d', 'e', 'f'])
print(f)

print('abc' * 3)

## INDEX
s = "gnu's not unix"
e = enumerate(s)
print(e)

print(list(enumerate(s)))

# Primeiro n
print(s.index('n'))

# após a posição 2
print(s.index('n', 2))

# Exception se não encontrar o elemento
#print(s.index('n', 12))

s = 'python'
l = [1, 2, 3, 4, 5, 6, 7, 8, 10]

print(l[1:4])

print(s[4:1000])
print(s[::])

l = [1, 2, 3]
l2 = l[:]
print(l is l2) #False

print(s[5:00:-1])

# String reverse
print(s[::-1])


# Caveats

a = Decimal('10.5')
b = Decimal('10.5')
print(a is b)

l = [Decimal('10.5')]
print(id(l[0]))

l2 = l * 2
print(l2)

print(id(l2[0]))
print(id(l2[1]))

l = [[0, 0 ]]
print(id(l[0]))

l2 = l * 2
print(l2)

# Cuidado com repetição de elementos... mesmo end. memória.
print(id(l2[0]), id(l2[1]))

l[0][0] = 100
print(l)
print(l2)
