import inspect
from inspect import isfunction, ismethod, isroutine

# dummy code
i = 100

# TODO: Fix this function
# does nothing
def my_func(a: "mandatory positional",
            b: "optional positional" = 1,
            c=2,
            *args: "add extra positional here",
            kw1,
            kw2=100,
            kw3=200,
            **kwargs:"provide extra kw-only here") -> "does nothing":
    """This function doesn nothing but does have various paremeters
    and anotations.
    """
    i = 10
    j = 20
    a = i + j
    return a

print(my_func.__doc__)
print(my_func.__annotations__)
my_func.short_description = "this is a function that does nothing much"
print(my_func.__name__)

def fnc_call(f):
    print(f.__name__)

fnc_call(my_func)

print(my_func.__defaults__)
print(my_func.__kwdefaults__)
print(my_func.__code__)
print(dir(my_func.__code__))
print(my_func.__code__.co_name)
print(my_func.__code__.co_varnames)  # incluí tbm as variáveis locais
print(my_func.__code__.co_argcount)  # só considera os argumentos posicionais na contagem.


a = 10
print(isfunction(a))
print(ismethod(my_func))
print(isfunction(my_func))

class MyClass:

    def f(self):
        pass

print(isfunction(MyClass.f))
my_obj = MyClass()
print(isfunction(my_obj.f))
print(ismethod(my_obj.f))
print(isroutine(my_obj.f))

print(inspect.getsource(my_func))

print(inspect.getmodule(my_func))
print(inspect.getmodule(print))

import math
print(inspect.getmodule(math.sin))
print(inspect.getcomments(my_func))

print(inspect.signature(my_func))
print(dir(inspect.signature))

print(my_func.__annotations__)
print(inspect.signature(my_func).return_annotation)


sig = inspect.signature(my_func)
print(sig)

print(sig.parameters)

# Verificação do tipo de parâmetros

for param in sig.parameters.values():
    #print(k, type(v))
    #print(dir(v))
    print('Name:', param.name)
    print('Default', param.default)
    print('Annotatin', param.annotation)
    print('Kind', param.kind)
    print('----------------------------')

print(help(divmod))

print(divmod(4, 3))


for param in inspect.signature(divmod).parameters.values():
    print(param.kind)
