"""
x e y are passed by reference ie. the memory addresses of x and y are passed.
O que será assinalado para a é o endereço de memória de x , e para b o end. memória de y.

Modulo scope                                    Function Scope
x                           10 (0x13F)              a
y                           'a' (0xE345)            b

"""

# 1Forma mais comum

def my_func(a, b): # a, b - parameters
    pass

x = 10
y = 'a'
my_func(x, y) # arguments -

# 2. Com um valor default

def my_func2(a, b = 100):
    pass

my_func2(10, 20)
#my_func(10)  # a = 5, b = 100

# 3. Se colocar um valor padrão para b teria que colocar para c tbm

#def my_func3(a, b= 100, c):
#    pass

def my_func3(a, b=5, c= 10):
    pass

my_func3(1)     # a = 1, b =5, c = 10
my_func3(1, 2)    # a = 1, b= 2, c = 10
my_func3(1, 2, 3)  # a =1, b =2, c = 3

# Mas se queremos especificar o 1 e 3 e omitir o 2o. argumento?
# Os nomes dos argumentos devem corresponder aos do parâmetro

my_func3(a=1, c=2)  # a = 1, b =5, c = 2

my_func3(1, c=2)  # a = 1, b = 5, c = 2

def my_func4(a, b, c):
    pass

my_func4(1, 2, 3)
my_func4(1, 2, c=3)
my_func4(a=1, b=2, c=3)
my_func4(c=3, a=1, b=2)

# But once you used a named argument, all arguments thereafter must be named too
## my_func4(c=1, 2, 3) - sintaxa inválido
# my_func4(1, b=2, 3)

def my_func10(a, b, c):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func10(1, 2, 3)


def my_func10(a=1, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))

my_func10(10, 20, 30)
my_func10(10, 20)
my_func10(10)

def my_func10(a, b=2, c=3):
    print("a={0}, b={1}, c={2}".format(a, b, c))


my_func10(c=30, b = 20, a = 10)
my_func10(10, c=30, b=20)
my_func10(10, c= 30)





















