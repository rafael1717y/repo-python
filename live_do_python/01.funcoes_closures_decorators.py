# 21:25

# funções nomeada (def)
def nomeada_soma(x, y):
    """
    Função que soma dois valores.
    """
    return x + y

# funções anônimas
anonima_soma = lambda x, y: x + y

# funções de classe
class classe_soma:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # fazendo um classe se comportar como uma função
    def __call__(self, *args, **kwargs):
        return self.x + self.x

"""Funções nomeadas
"""

print(nomeada_soma(2, 2))
print(nomeada_soma.__name__) # funções tbm são objetos
print(nomeada_soma.__doc__) # faz introspecção da função
print(help(nomeada_soma))

soma_2 = (lambda x: x + 2)(2)
print(soma_2(2))
