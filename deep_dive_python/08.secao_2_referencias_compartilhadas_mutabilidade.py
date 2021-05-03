a = "hello"
b = a

# Apontam para a mesma referência de memória
print(hex(id(a)))
print(hex(id(b)))

# Embora nao compartilhem referencias, python manager faz isso. É seguro.

a = 'hello'
b = 'hello'

print(hex(id(a)))
print(hex(id(b)))

a = [1, 2, 3]
b = a

print(hex(id(a)))
print(hex(id(b)))

b.append(100)
print(hex(id(a)))
print(hex(id(b)))
print(b)

a = 10
b = 10
print(hex(id(a))) # nao acontece sempre de ser igual
print(hex(id(b)))

a = 500
b = 500
print(hex(id(a)))
print(hex(id(b)))
