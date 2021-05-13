class NumString:

    def __init__(self, value):
        self.value = str(value)

    def __str__(self):
        return self.value

    def __int__(self):
        return int(self.value)

    def __float__(self):
        return float(self.value)

    def __add__(self, other):
        if '.' in self.value:
            return float(self) + other
        return int(self) + other

    def __radd__(self, other):
        return self + other

    def __iadd__(self, other):
        self.value = self + other
        return self.value

    def __mul__(self, other):
        if '.' in self.value:
            return float(self) * other
        return int(self) * other

    def __rmul__(self, other):
        return self * other

    def __imul__(self, other):
        self.value = self * other
        return self.value


five = NumString(5)
print(five)
print(type(five))
print(type(five.value))

print(int(five))
print(float(five))
print(five + 4)
print(NumString(4) + 5)
print(NumString(2.2) + 5)
#print(5 + NumString(5)) -- não funciona nesse sentido sem implementar o método __radd__
print(5 + NumString(5))
age = NumString(25)
print(age + 5)
print(5 + age)
print(10 * 2)
print(20 * 2)



class Dreamcar:


    def __init__(self, make, model):
        self.make = make
        self.model = model


    def __str__(self):
        return "My dream car is a {} {}".format(self.make, self.model)

car1 = Dreamcar('Ford', 'XX')
print(car1)










