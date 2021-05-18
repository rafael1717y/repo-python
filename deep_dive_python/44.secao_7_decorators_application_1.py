def timed(fn):
    from time import perf_counter
    from functools import wraps

    @wraps(fn)
    def inner(*args, **kwargs): # calcula qto tempo a função demora
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        elapsed = end  - start

        args_ = [str(a) for a in args]
        kwargs_ =['{0}={1}'.format(k, v) for (k, v) in kwargs.items()]
        all_args = args_ + kwargs_
        args_str = ','.join(all_args)

        print(('{0}({1}) took {2:.6f}s to run.'.format(fn.__name__, args_str, elapsed)))
        return result
    return inner

# Calcular Fibonacci  1, 1, 2, 3, 5, 8, 13, 21 com recursion, loop e reduce...


def calc_recursive_fib(n):
    if n <= 2:
        return 1
    else:
        return calc_recursive_fib(n-1) + calc_recursive_fib(n-2)

print(calc_recursive_fib(6))


@timed
def fib_recursive(n):
    return calc_recursive_fib(n)


fib_recursive(6)
fib_recursive(20)
fib_recursive(25)
fib_recursive(30)
fib_recursive(36)

@timed
def fib_loop(n):
    fib_1 = 1
    fib_2 = 1
    for i in range(3, n+1) :
        fib_1, fib_2 = fib_2, fib_1 + fib_2
    return fib_2

print(fib_loop(36))













