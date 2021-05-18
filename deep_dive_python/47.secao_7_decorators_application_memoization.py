def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

#fib(10)

class Fib:
    def __init__(self):
        self.cache = {1:1, 2:1}

    def fib(self, n):
        if n not in self.cache:
            print('Calculating fib({0})'.format(n))
            self.cache[n] = self.fib(n-1) + self.fib(n-2)
            print(self.cache[n])
        return self.cache[n]

f = Fib()
print(f.fib(10))
print("==============================""")
# Reescrevendo a clase como closurer

def fib():
    cache= {1:1, 2:1}

    def calc_fib(n):
        if n not in cache:
            print('Calculating fib({0})'.format(n))
            cache[n] = calc_fib(n-1) + calc_fib(n-2)
        return cache[n]

    return calc_fib

f = fib()
print(f(10))

g = fib()
g(10)

# Reescrevendo usando decorators

def memoize_fib(fib):
    cache= {1:1, 2:1}

    def inner(n):
        if n not in cache:
            cache[n] = fib(n)
        return cache[n]

    return inner

@memoize_fib
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

print("##")
fib(10)

def memoize(fn):
    cache= dict()

    def inner(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return inner


@memoize
def fib(n):
    print('Calculating fib({0})'.format(n))
    return 1 if n < 3 else fib(n-1) + fib(n-2)

fib(10)


def fact(n):
    print('Calculation {0}!'.format(n))
    return 1 if n < 2 else n * fact(n-1)

print("%%%%")
print(fact(6))

@memoize
def fact(n):
    print('Calculation {0}'.format(n))
    return 1 if n < 2 else n * fact(n-1)


from time import perf_counter
start = perf_counter()
print(fib(35))
end = perf_counter()
print(end - start)
print("&&&&&&")
print(fact(36))













