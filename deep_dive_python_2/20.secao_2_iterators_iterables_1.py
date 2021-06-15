s = {'x', 'y', 'b', 'c', 'a'}

for item in s:
    print(item)

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0  # índice


    def __len__(self):
        return self.length


    def __next__(self):
        if self.i >= self.length: # se exauriu a coleção
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

sq = Squares(3)
print(len(sq))

#print(sq.next_())
#print(sq.next_())
#print(sq.next_())
print(next(sq))
#print(sq.next_()) ## exauir a coleção

sq = Squares(10)
while True:
    try:
        print(next(sq))
    except StopIteration:
        break

import random

class RandomNumbers:
    def __init__(self, length, *, range_min=0, range_max=10):
        self.length = length
        self.range_min = range_min
        self.range_max = range_max
        self.num_requested = 0

    def __len__(self):
        return self.length

    def __next__(self):  #drawbacks --- cannot use a for loop - next there's no going back
        if self.num_requested >= self.length:
            raise StopIteration
        else:
            self.num_requested +=1
            return random.randint(self.range_min, self.range_max)

    def __iter__(self):
        return self

numbers = RandomNumbers(3)
print(next(numbers))
print(next(numbers))
print(next(numbers))
## StopIteration print(next(numbers))

while True:
    try:
        print(next(numbers))
    except StopIteration:
        break

numbers = RandomNumbers(10)
