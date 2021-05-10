"""2 diferentes escopos -- mesma variável
Closure as function plus an extended scope that contains the free variables
"""


def outer():
    ### closure
    x = 'python'

    def inner():
        print("{0} rocks!".format(x))  # msm x  free variable
    ### closure
    #inner()
    return inner  # returning the closure. We can assing that return vale to a variable name fn = outer()

#outer()

fn = outer()
print(fn)

def outer1():
    x = 'python'
    def inner():
        print(x)
    return inner

# x está em diferentes escopos, mas sempre referencia o mesmo valor.
#  Python does this by creating a cell as an intermediary object.



def outer2():
    a = 100
    x = 'python'
    def inner():
        a = 10 # local variable
        print("{0} rocks!".format(x))
    return inner

fn = outer2()  # fn-> inner + extendend scope x
print(fn.__code__.co_freevars)  # ('x')
print(fn.__closure__) #<cell at 0x7f52cf4a87f0: str object at 0x7f52cf6e6230>,)


def counter():

    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc

fn = counter()
print(fn())

f1 = counter()
f2 = counter()

## Shared Extended Scopes

def outer():

    count = 0  # free-variable ligada ao escopo extendido.

    def inc1():
        nonlocal count #count aqui tem a mesma célula de referência que count em linha 66
        count += 1
        return count

    def inc2():
        nonlocal count # idem, count está sendo compartilhad por múltiplos escopos
        count += 1
        return count

    return inc1, inc2

f1, f2 = outer()

print(f1())
print(f2())


def adder(n):
    def inner(x):
        return x + n
    return inner


add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

add_1(10)


#
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)













































