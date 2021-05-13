class Car:
    #class attibutes
    wheels = 4
    doors = 3
    engine = True

    ## Colocando um valor como default
    def __init__(self, model, year, make="Ford"):
        self.make = make
        self.model = model
        self.year = year
        self.gas = 100
        self.is_moving = False

    def __str__(self):
        return f'{self.make} {self.model} {self.year}'

    def __eq__(self, other):
        """Compara se duas instâncias são iguais."""
        return self.make == other.make and self.model == other.model

    def stop(self):
        if self.is_moving:
            print("The car has stopped.")
            self.is_moving == False
        else:
            print('The car has alrealdy stopped.')


    def go(self, speed):
        if self.use_gas():
            if not self.is_moving == False:
                print('The car starts moving')
                self.is_moving == True
            print(f'The car is going {speed}')
        else:
            print('You have run out of gas')
            self.stop()

    def use_gas(self):
        self.gas -= 60
        if self.gas <= 0:
            return False
        else:
            return True

class Dealership:

    def __init__(self):
        self.cars = []

    def __iter__(self):
        """yeld from vai pegar todoos elementos de um iterável e retorná-los"""
        yield from self.cars


    def add_car(self, car):
        self.cars.append(car)

# Instanciação da classe
#my_car = Car()
car_one = Car("Model T", 1908)
car_four = Car("Fusion", 1990)

if car_one == car_four:
    print('equal')
else:
    print('not equal')


my_dealership = Dealership()
my_dealership.add_car(car_one)
my_dealership.add_car(car_four)

for car in my_dealership:
    print(car)




print(car_one)
print(str(car_one))
car_one.stop()
car_one.go('slow')
car_one.go('fast')
car_one.stop()
car_one.stop()
print(dir(car_one))

car_two = Car("Phantom", 2020)

print(car_one.make)
print(car_two.make)

car_one.year = 2015
print(car_one.year)
print(car_two.year)

print(f'car_one {car_one.doors}')
print(id(car_one.doors))
print(f'car_two {car_two}')
print(id(car_two.doors))
print(f'Car {Car.doors}')
print(id(Car.doors))


"""
Car.doors = 3
car_one.doors = 6
print(f'car_one {car_one.doors}')
print(f'car_two {car_two.doors}')
print(f'Car - {Car.doors}')

#print(car_two.doors)
#print(Car.doors)
"""

# Verificando se um objeto é uma instância de uma classe
#print(my_car)
#print(type(my_car))
#print(isinstance(my_car, Car))