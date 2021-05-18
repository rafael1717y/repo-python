def logged(fn):
    from functools import wraps  # aqui para qdo importar a função
    from datetime import datetime, timezone

    @wraps(fn)
    def inner(*args, **kwargs):
        run_dt = datetime.now(timezone.utc)
        result = fn(*args, **kwargs)
        print('{0}:called {1}'.format(run_dt, fn.__name__))
        return result

    return inner

@logged
def func_1():
    pass

@logged
def func_2():
    pass

func_1()
func_2()
print("========")
def timed(fn):
    from functools import wraps
    from time import perf_counter

    @wraps(fn)
    def inner(*args, **kwargs):
        start = perf_counter()
        result = fn(*args, **kwargs)
        end = perf_counter()
        print('{0} ran for {1:.6f}s'.format(fn.__name__, end-start))
        return result
    return inner

@logged
@timed
def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

print(fact(3))

# ------------------------
# Igual a @logged, @timmed

def fact(n):
    from operator import mul
    from functools import reduce

    return reduce(mul, range(1, n+1))

fact = logged(timed(fact))

print("====")
fact(3)

# Novo Exemplo
# ------------

def dec_1(fn):
    def inner():
        print('Running dec_1')
        return fn()
    return inner

def dec_2(fn):
    def inner():
        print('Running dec_2')
        return fn()
    return inner

@dec_1
@dec_2
@dec_1
@logged
@timed
def my_func():
    print("Running my_func")

#my_func = dec_1(dec_2(my_func))

my_func()

"""
A ordem dos decorators pode fazer diferença em casos como:

@auth
@logged
def save_resource():
    pass

save_resource = auth(logged(save-resource))
# Se autenticação falhar não executará o restante.
# Se auth -> innerfunction, else return error.
"""
