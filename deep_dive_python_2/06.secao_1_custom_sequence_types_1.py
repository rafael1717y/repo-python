my_list = [0, 1, 2, 3, 4, 5]

for item in my_list:
    print(item ** 2)


index = 0
while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1

print(my_list.__len__())

# Sequencias Customizadas

my_list = [1, 2, 3, 4, 5]
print(len(my_list))
print(my_list.__len__())

print(my_list[2])
print(my_list.__getitem__(2))

print(my_list.__getitem__(slice(None, None, -1)))

for item in my_list:
    print(item ** 2)

# Iterando sem o for loop

index = 0

while True:
    try:
        item = my_list.__getitem__(index)
    except IndexError:
        break
    print(item ** 2)
    index += 1


class Silly:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        print('Called __len__')
        return self.n

    def __getitem__(self, value):
        print(f'You requested item at index {value}')
        if value < 0 or value >= self.n:
            raise IndexError
        else:
            return 'This is a silly element'

silly = Silly(10)
print(len(silly))

#print(silly.__getitem__(100))

# Sequência criada
for item in silly:
    print(item)

print([item * 2 for item in silly])


# Ex. 2

from functools import lru_cache

@lru_cache(2**10)
def fib(n):
    if n < 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

print(fib(5))
print(fib(100))

class Fib:
    def __init__(self, n):
        self.n = n

    def __len__(self):
        return self.n

    def __getitem__(self, s):
        if isinstance(s, int):
            if s < 0 :
                s = self.n + s
            if  s < 0 or s >= self.n:
                raise IndexError
            else:
                return Fib._fib(s)
        else:
            start, stop, step = s.indices(self.n)
            rng = range(start, stop, step)
            return [Fib._fib(i) for i in rng]

    @staticmethod
    @lru_cache(2 ** 10)
    def fib(n):
        if n < 2:
            return 1
        else:
            return Fib._fib(n - 1) + Fib._fib(n - 2)


f = Fib(8)
print(f[0])
print(f[7])
#print(f[9])
#print(f[-1])

for item in f:
    print(item)

"""
fib = Fib(10)
#print(list(fib))
#print(9)
print(list(range(9,6, -1)))
"""
