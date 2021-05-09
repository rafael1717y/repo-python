"""Object = a container
contains data -> state --> attibutes
contains functionally -> behavior -> methdos
classes are themselves objects, they have attributes (e.g. classe name)
they have behavior - e.g. how to create an instance of the class

Python classes are created from the type metaclass.

Classes have behavior -> they are callable MyClass() -> this returns an instance of the class
Instances are created from classes -- their type is the class they were create from

if MyClass is a class in Python and my_obj is an instance of that class:
my_obj = MyClass()

type(my_obj) -> MyClass
isinstance(my_obj, MyClass) -> True
"""

class Person:
    pass

# Qualquer classe criada será do tipo type (metaclasse).
print(type(Person))  # type = type

print(Person.__name__) # atributo da classe
p = Person()

# A classe é callabe.
# Quando chamamos a classe, python irá criar uma instância da classe.
print(type(p)) # no main module

print(p.__class__)

print(type(p))

# O objeto p é uma instância do objeto classe Person ?
print(isinstance(p, Person))

print(isinstance(p, str)) # False

# O objeto 'hello' é uma instância da classe built-in str
print(isinstance('hello', str))

print(type(str))  # class 'type' (metaclasse



