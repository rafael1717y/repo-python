"""PEP 8 Style Guide

01. Must start with underscore (_) or letter(a-z A-Z) followed by any number of
underscorer, letters or digits.

var my_var index1 index_1
_var __var  __lt__

02. cannot be reserved words

03. _my_var  (private objects) -> objects named this way will not get imported
by a statement such as: from module import *

04. __my_var - used to 'mangle' class attributes

__my_var__  used for system_defined names that have a meaning to the interpreter.

05. x < y   --->  x.__lt__(y)

06. Packages - short, all-lowercase name. Preferably no underscores - utilities

07. Modulos - short, all-lower case. Can have underscores -- db_utils

08. Classes - CapWords (upper camecase) convention. BankAccount

09. Functions - snake_case --- account_id

10. Constants - all-uppercase, words separated by underscores MIN_APR
"""

"""
Multi-line string literals is just a regular string.
Multi-string are not comments, although they can be used as such, especially
with special comments called docstrings.
"""
# Escrevendo funções com múltiplas linhas

def my_func(a, # this is used to indicate...
            b, #comment
            c):
    print(a, b, c)

my_func(10, #comment
        20,
        30)

lista_a = [1,
           2,
           3]

a =  [1 #item 1
     ,2 ]

print(a)

b = {'key1': 1  #value for key 1
     ,'key2': 2 #value for key 2
     }

print(b)

a = 10
b = 20
c = 30

if a > 5 \
        and b> 10 \
               and c > 20:
    print('yes')

a = '''This is a string'''

a = '''this
    is a string 
        that is create over multiple lines'''
print(a)

b = '''some items:
        1, item 1
        2, item 2'''

print(b)

def my_func():
    a = '''a multi-line string
that is indented in the second line'''
    return a

print(my_func())

