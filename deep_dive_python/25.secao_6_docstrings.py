def my_func(a):
    """documentation for my_func"""
    return a

print(my_func.__doc__)


def my_func2(a: 'a string', b: 'a positive integer') -> 'a string':
    return a + b

print(my_func2.__doc__)

def my_func3(a: str, b: [1, 2, 3]) -> str:
    return  a * b


def my_func4(a: str= 'xyz',
             *args : 'additional parameters',
             b: int = 1,
             **kwargs: 'additional keyword only params') -> str:
    pass

# Sphinx
print(my_func4.__annotations__)

def my_fun5(a, b = 1):
    """returns a * b"""
    return a + b

print(my_fun5.__doc__)


def my_fun6(a: 'annotation for a',
            b: 'annotation for b' =1) -> 'something annot':
    """documentation for my_func6"""
    return  a + b

print(my_fun6.__doc__)
print(my_fun6.__annotations__)
print(my_fun6.__name__)

def my_func7(a: str,
             b: 'int > 0' = 1,
             * args: 'some extra positional args',
             k1: 'keyword-only arg1',
             k2: 'keyword-only arg2' = 100,
             **kwargs: 'some extra keyword ony args') -> 'something':
    print(a, b, args, k1, k2, kwargs)


print(my_func7.__annotations__)
