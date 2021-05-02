#3. Object mutability
"""
Changing the data inside the object is called modifying the internal state of the
object.
An object whose internal state can be changed is called mutable.
Com integer - muda o end memória.
Bank account - acct 1234 - balance 150
bank account - acc 1234 - balance 500

Immutable:
01. numbers (int, float, booleans, etc). Não modifica o estado interno.
--- ex my_var = 10 , my_var = 15 (ex. abaixo).
02. strings
03. tuples
04. frozen sets
05. user-defined classes

Mutable:
01. lists
02. sets
03. dictionaries
04. user-defined classes

"""

#1.
a = 10
print(hex(id(a)))

# Muda o endereço de memória com o re-assignment. São objetos diferentes
a = 15
print(hex(id(a)))

# Muda novamente
a = a + 1
print(hex(id(a)))

# 2.
# ! a e b apontando para o mesma objeto, no msm end.
# Pq python está reutilizando o mesmo endereço de memória nesse caso?

a = 10
b = 10
print(hex(id(a)))
print(hex(id(a)))

# 3.
print("=======")
my_list = [1, 2, 3]
print(id(my_list))

my_list.append(4)
print(my_list)
# O end. de memória não muda mesmo após a inserçaão de um elemento.
print(id(my_list))

my_list_1 = [1, 2, 3]
print(id(my_list_1))  # apesar de conter o msms valores a o end memória é outro.

my_list_1 = my_list_1 + [4] # não modifica o estado interno de my_list_1
print(my_list)
print(id(my_list_1)) # agora mudou o id

my_dict = dict(key1=1, key2='a')
print(id(my_dict))

my_dict['key3'] = 10.5
print(my_dict)
print(id(my_dict)) # msm end.

print("====tupla =======")
t = [1, 2, 3]
print(id(t))
print(t[0])
print(id(t[0]))

t = ([1, 2], [3, 4])
print(id(t))

# Só pq estamos lidando com um elemento imutável nao quer dizer que os elementos
# da coleção não possam ser mudados.
t[0].append(3)
print(t)  # tupla com um elemento adicionado

"""
t = (1, 2, 3) # sao ref a uma objeto imutável

a = [1, 2]
b = [3, 4]

# Criando uma lista a partir das tuplas a e b
# t é imutável mas os elementos que t contém não.
# Não confundir a imutabilidade com algo que nunca pode ser alterado.
t = (a, b)   # t = ([1, 2], [3,4])

a.append(3)

t = ([1, 2], [3, 4]) # these are references to a mutable object

"""