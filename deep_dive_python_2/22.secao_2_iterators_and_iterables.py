class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
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

cities = Cities()
print(type(cities))
print(list(enumerate(cities))) #[(0, 'Paris'), (1, 'Berlin'), (2, 'Rome'), (3, 'Madrid'), (4, 'London')]
print(list(enumerate(cities)))  # []


class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

cities = Cities()
print(len(cities))

class CityIterator:
    def __init__(self, city_obj):
        print('City itertor new object')
        self._city_obj = city_obj
        self._index = 0

    def __iter__(self):
        print('CityIterator __iter__ called')
        return self

    def __next__(self):
        print('City iterator __next__ called')
        if self._index >= len(self._city_obj):
            raise StopIteration
        else:
            item = self._city_obj._cities[self._index]
            self._index += 1
            return item

cities = Cities()
city_iterator = CityIterator(cities)
for city in city_iterator:
    print(city)

cities = Cities()
city_iterator = CityIterator(cities)
for city in city_iterator:
    print(city)

for city in city_iterator:
    print("aaa", city)


## Iterator Protocol

class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
        print('Cities __iter__ called')
        return CityIterator(self)

cities = Cities()
for city in cities:
    print(' === ' ,city)

# Sem necessidade de criar obj de novo.
for city in cities:
    print(' === ' ,city)

print("=================")

"""CHamado _iter_ métod na classe Cities que cria um CityIterator e retorna
City new object! - Depois chama __next__ em CityIterator
City iterator __next__
"""
cities = Cities()
for city in cities:
    print(city)


city_iter_1 = cities.__iter__()
city_iter_2 = cities.__iter__()

print(city_iter_1 is not city_iter_2)

for city in city_iter_1:
    print(city)


print(list(enumerate(cities)))
print(sorted(cities, key=lambda  x: len(x)))

city_iterator = cities.__iter__()

for city in city_iterator:
    print(city)

s = {'a', 100, 'x', 'X'}
print(s.__iter__())

print(iter(s))

set_iterator = iter(s)

# Iterables are consumed
# Iterators not pq retornam um novo iterator todo vez.

for item in set_iterator:
    print(item)



























