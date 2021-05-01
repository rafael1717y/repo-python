"""
my_var_1 é uma referência para o objeto armazenado em memória em 0x1000 (p. ex).
my_var_1 não é igual a 10, mas uma referência ou 'alias' para o objeto naquela localização.
In python, we can find out the memory address referenced by a variable by using
the id() function. This will return a base-10 number. Converter usando usando a
função hex().
"""
import sys
import ctypes

my_var_1 = 10

# Qual o end de memória my_var_1 se referencia? Entra na end e pega o valor.
print(my_var_1)

# Endereço de memória de my_var_1
print(id(my_var_1))

# Em hexadecimar
print(hex(id(my_var_1)))

greeting = 'hello'
print(greeting)

print(id(greeting))
print(hex(id(greeting)))

## Contagem de referências - Reference Counting / Python Manager

# Estão compartilhando a referencia para o valor de 10
other_var  = my_var_1

# Achando as referências que apontam para um objeto (find the reference count)
# passando my_var to getrefcount() creates an extra reference !

a = [1, 2, 3]

print(id(a))
print(sys.getrefcount(a))  # 2 pois há um ref e a criada pelo getrefcount

## Usando o ctypes

def ref_count(address: int):
    return ctypes.c_long.from_address(address).value

print(ref_count(id(a)))

print(ref_count(140265849332288))

print("===")

b = a
print("id de a", id(a))
print("id de b", id(b))

print(ref_count(id(a)))
print(ref_count(id(b)))

c = a

print(ref_count(id(a))) # 3

c = 10
print(ref_count(id(a)))

b = None
print(id(b))

print(ref_count(id(a)))

## Pode variar.
a_id = id(a)
a = None
print(ref_count(a_id))
