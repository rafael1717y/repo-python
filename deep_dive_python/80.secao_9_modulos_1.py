def func():
    a = 10
    return a

print(func)
print(func())

print(globals())

# Namespaces are dict
f = globals()['func']
print(f)

print(locals() is globals())

# Verificando que a é global
# --------------------------

a = 100
print(globals())

def func():
    a = 10
    b = 10
    print(locals())

# Imprimindo um dicionário com as variáveis locais
func()

import math

print(math)

import fractions
print(fractions)

junk = math
print(junk.sqrt(2))

print(globals())
print(globals()['math'])

mod_math = globals()['math']
print(mod_math.sqrt(2))

print(type(math))
print(id(math))

# Singleton object -- mesma referência.
import math
print(id(math))

import sys
print(sys.modules)
print(type(sys.modules))

print(sys.modules['math'])
print(id(sys.modules))


print(math.__dict__)

f = math.__dict__['sqrt']
print(f(2))


import fractions

print(sys.modules['fractions'])
print(dir(fractions))

print(fractions.__dict__)

import calendar

print(calendar)

import types
from types import ModuleType
print(isinstance(fractions, types.ModuleType))
print(isinstance(math, ModuleType))

# Criando um módulo
mod = types.ModuleType('test', 'this is a test module.')
print(isinstance(mod, ModuleType))

print(mod.__dict__)

# Colocando atributos no módulo

mod.pi = 3.14
print(mod.__dict__)

mod.hello = lambda : 'Hello!'

print(mod.hello())

hello = mod.hello

print('hello' in globals())
print('mod' in globals())

from collections import namedtuple
mod.Point = namedtuple('Point', 'x y')
p1 = mod.Point(0, 0)
print(p1)
