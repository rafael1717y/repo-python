a = 10
b = 10

print('a is b', a is b)
print('a == b', a == b)

a = 500
b = 500

print(id(a))
print(id(b))

print('a is b', a is b)
print('a == b', a == b)

a = [1, 2, 3]
b = [1, 2, 3]

print(id(a))
print(id(b))

print('a is b', a is b) # end de memória são diferentes
print('a == b', a == b)  #conteúdo é o mesmo

a = 10
b = 10.0

print('a is b', a is b)
print('a == b', a == b)

a = 10 + 0j

print('a is b', a is b)
print('a == b', a == b)

# None operator
print(id(None))

a = None
b = None
c = None

print(a is b)
print(a is c)
