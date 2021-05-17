def counter(initial_value=0):
    def inc(increment=1):
        nonlocal initial_value
        initial_value += increment
        return initial_value
    return inc

counter1 = counter()
print(counter1())
print(counter1())

def counter(fn):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        print('{0} has benn called {1} times'.format(fn.__name__, cnt))
        return fn(*args, **kwargs)
    return inner

def add(a, b,):
    return a + b

def mult(a, b):
    return  a * b

counter_add = counter(add)
print(counter_add.__closure__)
print(counter_add.__code__.co_freevars)

result = counter_add(10, 20)
print(result)

counter_mult = counter(mult)
print(counter_mult(2,5))


counters = dict()

def counter(fn, counters):
    cnt = 0
    def inner(*args, **kwargs):
        nonlocal cnt
        cnt += 1
        counters[fn.__name__] = cnt
        return fn(*args, **kwargs)
    return inner

def fact(n):
    product = 1
    for i in range(2, n+ 1):
        product *= 1
    return product

print(fact(3))
