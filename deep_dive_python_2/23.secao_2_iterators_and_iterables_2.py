class Cities:
    def __init__(self):
        self._cities = ['Paris', 'Berlin', 'Rome', 'Madrid', 'London']
        self._index = 0

    def __len__(self):
        return len(self._cities)

    def __iter__(self):
         print('Cities __iter__ called')
         return self.CityIterator(self)

    def __getitem__(self, s):
        print('getting item...')
        return self._cities[s]

    class CityIterator:
        def __init__(self, city_obj):
            print('CityIterator new Object!')
            self._city_obj = city_obj
            self._index = 0

        def __iter__(self):
            print('CityIterator __iter__ called')
            return self

        def __next__(self):
            print('CityIterator __next__ called')
            if self._index >= len(self._city_obj):
                raise StopIteration
            else:
                item = self._city_obj._cities[self._index]
                self._index += 1
                return item


cities = Cities()
print(cities[0])


# Default - se não acha um __iter__ usuará __getitem__
# Hà um iterable usuando o iterable protocol?
for city in cities:
    print(city)

l = [1, 2, 3, 4]

# Perguntando pelo iterator
print(iter(l))
print(l.__iter__())

#
print(l.__getitem__(0))
print(l.__getitem__)

l_iter = iter(l)
print(l_iter)

for i  in l_iter:
    print(i)

for i  in l_iter:
    print(i)

#print(next(l_iter))

## Sets

s = {1, 2, 3}

print(iter(s))

s_iter = iter(s)
print(next(s_iter))
#print(s.__getitem__(0)) --- set nao possuem __getitem__ método.








