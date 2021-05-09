"""
In addition to whatever attributes Python automatically creates for uns
 e.g. __name__ with a state of 'MyClass' it also has language and version attributes.

# 01. Retrieving attribute values from objects -
# getattr(object_symbol, attribute_name)
"""

class MyClass:
    language = 'Python'
    version = '3.6'

print(getattr(MyClass, 'language'))
#print(getattr(MyClass, 'x'))  # AttributeError exception
print(getattr(MyClass, 'x', 'N/A')) # retorna N/A se nao existir o atributo na classe.

# 02. dot notation (shorthand)
print(MyClass.language)
# Não como especificar um valor default caso o atributo não exista.

# 03. Setting attibute values in objects


class MyClass:
    language = 'Python'
    version = '3.6'


# setattr function
setattr(MyClass, 'version', '3.7')
MyClass.version = '3.7'  # modificada o estada da classe

print(getattr(MyClass, 'version'))

# 04. What happens if we call setattr for an attribute we did not define in our class?

setattr(MyClass, 'x', 100) # or
MyClass.x = 100

# 05. Where is the state stored? In a dictionary

print(MyClass.__dict__)  # class namespace
# Ensures keys are strings


# 06. Mutating attribues

setattr(MyClass, 'x', 100)

print(MyClass.__dict__)

# 07. Removing attributes  delattr  ou del

delattr(MyClass, 'version')

print(MyClass.__dict__)

# 08. Acessing the namespece directly

class MyClass:
    language = 'Python'
    version = '3.6'

#MyClass.language
getattr(MyClass, 'language')
print(MyClass.__dict__['language'])  # nem sempre funciona.

# Sometimes classes have attributes that don't show up in that dictionary.






















