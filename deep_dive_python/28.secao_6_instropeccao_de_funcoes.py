"""
__name__ -> name of function
__defaults__ -> tuple containing positional parameter defaults
__kwdefaults__ --> dictionary containing keyword-only parameters defaults
"""
import inspect

def my_func(a, b):
    return a + b

my_func.category = "math"
my_func.sub_category = 'arithmetic'

#print(my_func.category)
#print(dir(my_func))

## Fuction attributes

def my_func2(a, b=2, c=3, *, kw1, kw2=2):
    pass

#print(my_func2.__name__)
#print(my_func2.__defaults__)
#print(my_func2.__kwdefaults__)
#print(my_func2.__code__)

def my_func3(a, b=1, *args, **kwargs):
    i = 10
    b = min(i, b)
    return a * b

print(my_func3.__code__)
print(my_func3.__code__.co_varnames) # parameters names first, dps variable names
print(my_func3.__code__.co_argcount) # does not count *args and ** kwargs!

print(inspect.isfunction(my_func3))
print(inspect.ismethod(my_func3))
print(inspect.isroutine(my_func))
print(inspect.getsource(my_func))
print(inspect.getmodule(my_func3))
print(inspect.getmodule(print))

# Function Comments

# setting up variable
i = 10

# TODO: implement function
# some additional notes
def my_func(a, b=1):
    """teste"""
    # comment inside my_func
    pass

print(inspect.getcomments(my_func))

# Callable Signatures

print(inspect.signature(my_func))

