class Panda:
    species = 'Ailuropoda melanoleuca'
    food = 'bamboo'


    def __init__(self, name, age):
        self.is_hungry = True
        self.name = name
        self.age = age


    def eat(self):
        self.is_hungry = False
        return f'{self.name} eats {self.food}.'

    def check_if_hungry(self):
        if self.is_hungry == True:
            self.eat()


panda = Panda('rafael', 20)
panda.eat()