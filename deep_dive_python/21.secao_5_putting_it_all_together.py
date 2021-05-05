"""
a, b, c=10                  *args/ *                kw1, kw2= 100              **kwargs
posit. parameters           * no + posit. args      specific keyw. only args
can have default values
"""

def func1(a, b = 10):
    pass

def func2(a, b, *args):
    pass

def func3(a, b, *args, kw1, kw2=100):
    pass

def func4(a, b=10, *, kw1, kw2 = 10):
    pass

def func5(a, b, *args, kw1, kw2=100, **kwargs):
    pass

def func6(a, b=10, *, kw1, kw2=100, **kwargs):
    pass

def func7(*args):
    pass

def func8(**kwargs):
    pass

def func9(*args, **kwargs):
    pass

print(1, 2, 3, sep="-")

## Usar o keyword approach para modificar o comportamento das funções

def func10(a, b, *args):
    print(a, b, args)

func10(1, 2, 'x', 'y', 'z')

def func11(a, b=2,  c=3, *args):
    print(a, b, c, args)

func11(1, 2, 3, 'x', 'y', 'z')

func11(1, c=5)

def func12(a, b=2, *args, c=3, d):
    print(a, b, args, c, d)

func12(10, 20, 'a', 'y', 'z', c=4, d=1)

func12(10, 20, 'x', 'y', 'z', d=10)

func12(1, 'x', 'y', 'z', d= 10)

def func13(a, b, *args, c=10, d=20, **kwargs):
    print(a, b, args, c, d, kwargs)

func13(1, 2, 'x', 'y', 'z', c= 100, d=200, x=0.1, y=0.2)

#print(*args)
print(1, 2, 3, sep="-", end=' *** ')
print(4, 5, 6, sep="-")


def calc_hi_lo_avg(*args, log_to_console=False):
    hi = int(bool(args and max(args)))
    lo = min(args) if len(args) > 0 else 0
    avg = (hi + lo) / 2
    if log_to_console:
        print('high={0}, low={1}, avg={2}'.format(hi, lo, avg))
    return avg

is_debug = True
avg = calc_hi_lo_avg(1, 2, 3, 4, 5, log_to_console=True)
print(avg)

































