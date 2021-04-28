class Candy:
    def __init__(self, name, color):
        self.name = name
        self.color = color

    def __str__(self):
        return f'{self.color} {self.name}'

class CandyStore:
    def __init__(self):
        self.candies = []

    def __iter__(self):
        yield from self.candies

    def add_candy(self, candy):
        self.candies.append(candy)

nerds = Candy('Nerds', 'Multi')
chocolate = Candy("Hersey's Bar", 'Brown')

my_store = CandyStore()

my_store.add_candy(nerds)
my_store.add_candy(chocolate)

for candy in my_store:
    print(candy)