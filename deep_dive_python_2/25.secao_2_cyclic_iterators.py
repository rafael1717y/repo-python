"""
1 2 3 4 5 6
N S W E

1N 2S 3W 4E 5N 6S 7W 8E 9N 10S ...
"""

# FINITO
class CyclicIteator:
    def __init__(self, lst, length):
        self.lst = lst
        self.i = 0
        self.length = length

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.lst[self.i % len(self.lst)] # 0 mod any -0 - 2 mod 4 ->2  4 modulo 4 = 0, 6 mod 4 = 2 ...
            self.i += 1
            return result

iter_cycl = CyclicIteator('NSWE', 15)

for item in iter_cycl:
    print(item)

# INFINITO

class CyclicIteator:
    def __init__(self, lst):
        self.lst = lst
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):

        result = self.lst[self.i % len(self.lst)] # 0 mod any -0 - 2 mod 4 ->2  4 modulo 4 = 0, 6 mod 4 = 2 ...
        self.i += 1
        return result

iter_cycl = CyclicIteator([10, 20, 30])

for _ in range(10):
    print(next(iter_cycl))

# 2 - Usando zip

numbers = range(10)
print(list(numbers))

iter_cycl = CyclicIteator('NSWE')
print(list(zip(list(numbers), iter_cycl)))

# 3
n = 10
i








