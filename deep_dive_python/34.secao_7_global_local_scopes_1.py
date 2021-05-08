"""
The portion of code where that name/binding is defined is called the lexical scope
of the variable.
These bindings are stored in namespaces. Every scope has a namespace (table).
There is no concept of a truly global scope in python. The only exception to this
are some of the built-in globally available objects as True, dict, print...
Global scopes are nested inside the bult-in scope.

module1.py
print(True)  --- python does not find True or print in the current module scope
             --- So, it looks for them in the enclosing scope -> built-in
             --- finds them there - > True

module2.py
print(a)        find print, but not a -: run-time Name Error

module3.py
print = lambda x: 'hello {0}!'.format(x)
s = print('world)    --- acha print in the module scope

Variables defined inside a function are not created untill the function is called.

Nested scopes
"""

def my_func(a, b):
    c = a * b
    return c

#, b, c colocados no escopo local durante compilação.
my_func('z', 2)


a = 0

def my_func1():
    a = 100 # python interprets this as a local variable (at compile-time)
    print('linha 38', a) # the local variable a masks the global variable a

my_func1()
print(a)

a = 0

def my_func2():
    global a
    a = 100
    print('linha 48', a)


my_func2()
print('linha 52', a)

a = 10

def func3():
    print(a)

def func4():
    print(a)
    a = 100

# func4() - erro

