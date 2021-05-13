"""Tuples                    Lists                     Strings
containers                - containers                - containers
order matters             - order matters -           - order matters
hetegogeneous/homogenous  tendem a ser homogeneous    - homogeneous
indexable                 indexable                   - indexable
iterable                  iterable                    - iterable
imutable                  mutable                     - immutable
fixed lenght *            length con change           - fixed lenght
fixed order *            order of elem can change    -
cannot do in-place sorts  can do in-place sorts
"""

# Tuple como estrutura de dados. The position is meaning.
# Point (10, 20) - 1st. elem. is the x-coordinate e 2nd y-coordinate
# Circle (0, 0, 10)   1st. x-coordinate of the center, 2nd y-coordinate of the center, 3rd. radius
# City: ('London', 'UK', 8_780_000)

london = ('London', 'UK', 8_780_000)
new_york = ('New York', 'USA', 8_500_000)

#cities = [('London', 'UK', 8_780_000), ('New York', 'USA', 8_500_000)]

#city = london[0]
#country = london[1]

cities = [('London', 'UK', 8_780_000), ('New York', 'USA', 8_500_000)]

total_population = 0
for city in cities:
    total_population += city[2]

new_york2 = ('New York', 'USA', 8_500_000)

city, country, population = new_york2
#new_york = 'New York', 'USA', 8_500_000

# Dummy variables (_)

city, _, population = ('Beijing', 'China', 21_000_000)
print(_)

record = ('DJIA', 2018, 1, 19, 25987,35, 26071.72, 25942.83, 25071.72)
#symbol, year, month, day, open, high, low, close = record
## symbol, year, close = record[0], record[1], record[7] -  awful!

symbol, year, month, day, *_, close = record
print(symbol)


# 01. Tuples as Data Structures

a = 10, 20, 30
print(type(a))

a = 'a', 10, 200
print(a[0])

for e in a:
    print(e)

a = 'a', 10, 20

x, y, z = a
print(y)


a = 1, 2, 3, 4, 5
x, *other, y, z = a
print(x)
print(*other)

x, *_, y, z = a
print(_)

class Point2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'{self.__class__.__name__}(x={self.x}, y = {self.y})'

pt = Point2D(10, 20)
print(pt)
pt.x = 100

a = Point2D(0, 0), Point2D(10, 20)
print(a)
print(id(a[0]))
a[0].x = 100
print(a)

s = 'python'
print(id(s))
s = 'python' + ' rocks!'
print(s)
print(id(s))

pt1 = (0, 0)
pt2 = (10, 20)

# 10.25



























































