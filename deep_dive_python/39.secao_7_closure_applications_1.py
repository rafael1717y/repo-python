from time import perf_counter

class Averager:
    def __init__(self):
        self.numbers = []

    def add(self, number):
        self.numbers.append(number)
        total = sum(self.numbers)
        count = len(self.numbers)
        return total/count

a = Averager()
print(a.add(10))
print(a.add(20))
print(a.add(30))

b = Averager()
print(b.add(10))

# Rescrevendo a classe Averager com closures

def averager():
    numbers = []
    def add(number):
        numbers.append(number) # numbers aqui é uma variável nonlocal. Não há = . add tem uma freevariable numbers.E tem uma variável local number.
        total = sum(numbers)
        count = len(numbers)
        return total/count
    return add               #  não esquecer de retornar o closure

a = averager()
print(a(10))
print(a(20))
print(a(30))

b = averager()
print(a(10))

# Vendo a célula que é usada para a variável livre do closure.

print(a.__closure__)


def averager():
    total = 0
    count = 0
    def add(number):
        nonlocal total
        nonlocal count
        total = total + number
        count = count + 1
        return total/ count
    return add


a = averager()
print(a.__closure__)
print(a.__code__.co_freevars)
print(a(10))
print(a(20))

class Averager:
    def __init__(self):
        self.total = 0
        self.count = 0

    def add(self, number):
        self.total += number
        self.count += 1
        return self.total / self.count

print(perf_counter())
print(perf_counter())

class Timer:
    def __init__(self):
        self.start = perf_counter()

    #def poll(self):
    #    return perf_counter() - self.start

    def __call__(self):
        return perf_counter() - self.start

t1 = Timer()

#Uma vez que a instância criada pela classe é callable pode-se não usar o método poll e só chamar o objento t1()
#print(t1.poll())
#print(t1.poll())

print(t1())
print(t1())

def timer():
    start = perf_counter()
    def poll():
        return perf_counter() - start
    return poll

t2 = timer()
print(t2())
