from functools import wraps

def counter(fn):
    count = 0  # local variable
    @wraps(fn)
    def inner(*args, **kwargs):
        nonlocal count # closure
        count +=1 # td vez que inner é chamado, a variávelo local lcount é incrementada em 1.
        print('Function {0} was called {1} times'.format(fn.__name__, count))
        return fn(*args, **kwargs)  # chama a função fn com os parâmetros que passamos para o closure
    return inner

def add(a, b=0):
    return a + b

# 01. Chamando counter passando a função add como parâmetro
# counter(add) retornará a inner function que requer 2 parâmetros.

add = counter(add) # recebe-se um closure de volta e assinala para o mesmo add. O 1o. add referencia o closure que criamos

result = add(1, 2)  # function add was called 1 times - resut = 3
print(result)

"""We essentially modified our add function by wrapping it inside another function that added some functionality to it
We also say that we decorated our function add with the function counter. We call counter a decorator function

Decorators:
    takes a function as an argument
    returns a closure 
    the closure usually acepts any combination of parameters
    runs some code in the inner function (closure)
    the closure fn calls the original function using the argument passed to the closue    

@counter
def add(a, b):
    return a + b

é igual a :

def add(a, b):
    return a + b
    
a = counter(add)

"""

# Executando a função add como um parâmetro da função counter.
@counter
def add(a, b):
    return a + b

"""
def add(a, b):
    return a + b

a = counter(add)
"""

@counter
def mult(a, b, c=1):
    """
    Returns the product of three values
    """
    return a * b * c

## OU... mult = counter(mult)
print(mult.__name__)  ## functional inner e não mult caso não usado @wraps
print(help(mult))
