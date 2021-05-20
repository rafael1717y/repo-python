"""
@timed
def my_func():
    _

my_func = timed(my_func)

Timed is a function that returns that inner closure that contains our original
function.

@timed(10)  --- timed is a decorater factory
def my_func():
    __
"""
"""
def timed(fn):
    from time import perf_counter
    total_elapsed = 0
    def inner(*args, **kwargs):
        for i in range(10):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            elapsed = end - start
            total_elapsed = (end - start)
        avg_run_time = total_elapsed / 10
        print("Avg run time: {0:.6f}s".format(avg_run_time))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 2 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)

@timed
def fib(n):
    return calc_fib_recurse(n)

fib(20)

# forma mais completa
fib = timed(fib)
print(fib(30))

"""
#

def timed(fn, reps):
    from time import perf_counter

    def inner(*args, **kwargs):
        total_elapsed = 0
        for i in range(reps):
            start = perf_counter()
            result = fn(*args, **kwargs)
            end = perf_counter()
            total_elapsed += (end - start)

        avg_run_time = total_elapsed / reps
        print("Avg run time: {0:.6f}s".format(avg_run_time, reps))
        return result
    return inner

def calc_fib_recurse(n):
    return 1 if n < 2 else calc_fib_recurse(n-2) + calc_fib_recurse(n-1)


def fib(n):
    return calc_fib_recurse(n)

fib = timed(fib, 5)
fib(28)


def dec(fn):
    print("running dec")

    def inner(*args, **kwargs):
        print("running inner")
        return fn(*args, **kwargs)
    return inner

"""
@dec
def my_func():
    print("running my func")
"""

def my_func():
    print("running my func")

my_func = dec(my_func)  # running pq só chamaou o decorator

print("========")
my_func()


def dec_factory():
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            return fn(*args, **kwargs)

        return inner

    return dec

print("====")
# o decorator será retornada pela factory
dec = dec_factory()


print("========")

@dec  # dec factory
def my_func():
    print("running my_func")

my_func()

# ou ... ou

@dec_factory()
def my_func():
    print("running my_func")

my_func = dec_factory()(my_func)


def dec_factory(a, b):
    print("running dec_factory")

    def dec(fn):
        print("running dec")

        def inner(*args, **kwargs):
            print("running inner")
            print("a={0}, b={1}".format(a, b))
            return fn(*args, **kwargs)

        return inner
    return dec

print("@@@")
dec = dec_factory(10, 20)

@dec
def my_func():
    print("running my_func")

my_func()

@dec_factory(100, 200)
def my_func():
    print("running my_func")

my_func = dec_factory(150, 250)(my_func)
my_func()