def outer():
    x = [1, 2, 3]
    print(hex(id(x)))
    def inner():
        y = x
        print(hex(id(y)))
    return inner

outer()
fn = outer()
print(fn.__closure__)

def outer1():
    count = 0
    def inc():
        nonlocal count
        count += 1
        return count
    return inc

fn = outer1()
print(fn.__code__.co_freevars)
print(fn.__closure__)
print(hex(id(0))) # aponta para o msm endereço do int 0 (singleton object)

# Após a chamada... A célula ainda existe e aponta para 1 agora.
print(fn())
print(fn.__closure__)
print(hex(id(0)))

def outer2():
    # Todos as variáveis count apontam para  mesma célula apesar de estarem em diferentes escopos.
    count = 0
    def inc1():
        nonlocal count
        count += 1
        return count

    def inc2():
        nonlocal count
        count += 1
        return count

    return inc1, inc2

fn1, fn2 = outer2()
# fn1 - closure com variavéis livres
print(fn1.__code__.co_freevars)  # count
print(fn2.__code__.co_freevars)

# Os dois closures apontam para a msm célula
print(fn1.__closure__) # int object at 0x7f9b91176910
print(fn2.__closure__)

print(fn1())
print(fn1.__closure__) # int object at 0x7f9b91176930>
print(fn2.__closure__)

print(fn1())
print(fn1.__closure__) # int object at 0x7f9b91176950>
print(fn2.__closure__)

def pow(n):
    def inner(x):
        return x ** n  # n -> apontando para uma célula
    return inner

square = pow(2)
print('l 69', square.__closure__)
print(hex(id(2)))

print(square(5))

cube = pow(3)
print(cube.__closure__)
print(hex(id(3)))
print(cube(5))


def adder(n):
    def inner(x):
        return x + n
    return inner

add_1 = adder(1)
add_2 = adder(2)
add_3 = adder(3)

# 3 diferentes células
print(add_1.__closure__, add_2.__closure__, add_3.__closure__)

# global
adders = []
for n in range(1, 4):
    adders.append(lambda x: x + n)

print(adders)
print(adders[0].__closure__) # não são closures
#adders[0][10]


def create_adders():
    adders = []
    for n in range(1, 4):
        #adders.append(lambda x : x + n) # bug
        adders.append(lambda x, y=n: x + y)  #
    return adders

adders = create_adders()

#
print(adders)
print(adders[0].__closure__)
print(adders[1].__closure__)

print(adders[0](10))


























