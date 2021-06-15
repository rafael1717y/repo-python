"""
Como há o método __iter__ implementado - chama __iter__ primeiro no for e dps __next__ .
An iterator é um objeto que implementa __iter__ e __next__
The drawback is that iterators get exhausted - become useless for iterating again.
The itertor is throw-away object.
The collection is iterable but the iterator is responsible for iterting over the collection.

An iterable is an object that implements:
__iter__ -> returns an iterator (in general, a new instance)
Iterables are thwmselvs iterables but they are iterables that become exhausted

An iterator is an object that implements:
__iter__ -> returns itself(an iterator)
__next__
An iterables on the other hand never become exhausted because they always return a new
iterator that is then used to iterate

The first thin python does when we try iterate over an object it calls iter() to obtain an iterator
then it starts iterating (using next, StopIteration, etc)
using the iterator returned by iter() .
"""

class Squares:
    def __init__(self, length):
        self.length = length
        self.i = 0

    def __next__(self):
        print('__next__ called')
        if self.i >= self.length:
            raise StopIteration
        else:
            result = self.i ** 2
            self.i += 1
            return result

    def __iter__(self):
        print('__iter__ called')
        return self

sq = Squares(3)
print(next(sq))
print(next(sq))

sq = Squares(5)
for item in sq:
    print(item)

# erro pq já iterou sobre tudo print(next(sq))

sq = Squares(5)
l = [(item, item + 1) for item in sq]
print(l)

print(l)

l = ['a', 'b', 'c']
print(list(enumerate(l)))

s = {100, 'x', 'a', 'X'}
for item in s:
    print(item)

print(list(enumerate(s)))

sq = Squares(5)
print(sorted(sq, reverse=True))

sq = Squares(9)
while True:
    try:
        item = next(sq)
        print(item)
    except StopIteration:
        break


sq = Squares(5)
sq_iterator = iter(sq)
print(id(sq), id(sq_iterator))

for item in sq:
    print(item)

sq = Squares(10)
print('======')
print([item for item in sq if item % 2 == 0])

"""
Classe com o protocol iterator implementado

class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'London']
        self._index = 0 
        
        def __iter__(self):
            return self
        
        def __next__(self):
            if self._index >= len(self._cities):
                raise StopIteration
            else:
                item = self._cities[self._index]
                self._index += 1
                return item

"""
## Dados aqui
class Cities:
    def __init__(self):
            self._cities = ['Paris', 'Berlin', 'Rome', 'London']

    def __len__(self):
        return len(self._cities)

## Operações aqui
class CityIterator:
    def __init__(self, cities):
        self._cities = cities
        self._index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self._index >= len(self._cities):
            raise StopIteration
        else:
            pass

cities = Cities()  # create an instance of the container object
city_iterator = CityIterator(cities)  # create a new iterator - but we pass in the cities instance
for city in city_iterator:
    print(city)

