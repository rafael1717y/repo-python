import random

class Character:

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Thief(Character):
    sneaky = True

    def __init__(self, name, sneaky=True, **kwargs):
        super().__init__(name, **kwargs)
        self.sneaky = sneaky


    def pickpocket(self):
        return self.sneaky and bool(random.randint(0, 1))


    def hide(self, light_level):
        return self.sneaky and light_level < 10


kenneth = Thief("Kenneth", sneaky=False, clever = True)
print('1', kenneth.sneaky)
print('2', kenneth.clever)



# Exemplo 2
# ---------

class Student:
    name = "Rafael"

    def __init__(self, name, **kwargs):
        self.name = name

        for key, value in kwargs.items():
            setattr(self, key, value)

    def praise(self):
        message = "You're doing a great job, {}".format(self.name)
        return message

    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)

    def feedback(self, grade):
        if grade > 50:
            return self.praise()
        else:
            return self.reassurance()


estudante = Student("rafa", outro = 'xyz')
print(estudante.name)
print(estudante.praise())
print(estudante.feedback(51))
#print(estudante.outro)


class RaceCar:

    def __init__(self, color, fuel_remaining, laps, **kwargs):
        self.color = color
        self.fuel_remaining = fuel_remaining
        self.laps = 0

        for key, value in kwargs.items():
            setattr(self, key, value)


    def run_lap(self, length):
        self.laps += 1
        return self.fuel_remaining - (length * 0.125)


car1 = RaceCar('blue', 10, 0, outro = 'xyz')
#print(car1.color)
print(car1.outro)

print(car1.run_lap(1))
print(car1.run_lap(1))
print(car1.laps)










