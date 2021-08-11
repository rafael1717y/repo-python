import math

class Circle:
    def __init__(self, r):
        self.radius = r
        self._area = None

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, r):
        self._radius = r
        self._area = None

    @property
    def area(self):
        if self._area is None:
            print("Calculating area...")
            self._area = math.pi * (self.radius ** 2)
        return self._area


c = Circle(1)
print(c.area)
print(c.radius)
c.radius = 2
print(c.area)
print(c.area)

class Factorials:
    def __iter__(self):
        return self.FactIter()

    class FactIter:
        def __init__(self):
            self.i = 0

        def __iter__(self):
            return self

        def __next__(self):
            result = math.factorial(self.i)
            self.i += 1
            return result


facts = Factorials()
fact_iter = iter(facts)
print(next(fact_iter))