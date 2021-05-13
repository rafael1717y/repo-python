
"""
Adiciona os valores de todos os itens passados como argumento.
"""
def calculate_total(*args):
    total = sum(args)
    print(total)

calculate_total(25, 25, 20, 30, 100, 200)
calculate_total(10, 20)

"""
UNPACKING
"""

def unpacker():
    return 'hey'

var1, var2, var3 = unpacker()

print(var1)


first, last = input('Enter your full name: \n').split(' ')
print(first)
print(last)
















