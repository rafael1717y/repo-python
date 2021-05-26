"""How to copy a sequence
"""

s = [10, 20, 30]

# non-pythonic!

cp = []
for e in s:
    cp.append(e)

# list comprehension

cp = [e for e in s]


# copy method

cp = s.copy()
print(cp)

# slicing

cp = s[0:len(s)] # cp = s[:]

# list

list_2 = list(s)

# obj diferentes
l1 = [1, 2, 3]
l2 = list(l1)
print(id(l1), id(l2))

# msm objeto
t1 = (1, 2, 3)
t2 = tuple(t1)
print(id(t1), id(t2))

# Shallow copies
"""Essentialy copies all the object references from one sequence to another."""
s = [10, 20, 30]
cp = s.copy()
cp[0] = 100
print(cp)

s = [[10, 20], [30, 40]]
cp = s.copy()
cp[0] = 'python'
print(cp)
print(s)

cp[1][0] = 100
print(cp)
print(s)

# Referência circular

a = [10, 20]
b = [a, 30]
a.append(b)

# Deep copy
from copy import copy, deepcopy

class MyClass:
    def __init__(self, a):
        self.a = a

x = [10, 20]
obj = MyClass(x)
cp_shallow = copy(obj)
cp_deep = deepcopy(obj)





















