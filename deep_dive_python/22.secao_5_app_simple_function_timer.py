import time

# Função para calcular o tempo de execução de outra função

def time_it(fn, *args, **kwargs ):
    print(args, kwargs)

time_it(print, 1, 2, 3, sep="-", end=' *** ')


def time_it(fn, *args, rep=1, **kwargs ):
    for i in range(rep):
        fn(*args, **kwargs)

time_it(print, 1, 2, 3, sep="-", end=' ***\n', rep=5)


def time_it(fn, *args, rep=1, **kwargs ):
    start = time.perf_counter()
    for i in range(rep):
        fn(*args, **kwargs)
    end = time.perf_counter()
    return (end - start) / rep

print(time_it(print, 1, 2, 3, sep="-", end=' ***\n', rep=5))


def computer_powers_1(n, *, start=1, end):
    # using a for loop
    results = []
    for i in range(start, end):
        results.append(n**i)
    return results


print(computer_powers_1(2, end=5))

def computer_powers_2(n, *, start=1, end):
    # using a list comprehension
    return [n**i for i in range(start, end)]

print(computer_powers_2(2, end=5))


def computer_powers_3(n, *, start=1, end):
    # using generators
    return (n**i for i in range(start, end))


print(list(computer_powers_3(2, end=5)))

print(time_it(computer_powers_1, 2, start=0, end=20000, rep=5))

print(time_it(computer_powers_2, n=2, start=0, end=20000, rep=5))

print(time_it(computer_powers_3, n=2, start=0, end=20000, rep=5))


a = (2**1 for i in range(5))
print(a)
list(a)

