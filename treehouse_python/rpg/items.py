from inventory import Inventory

class Item:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        return '{} {}'.format(self.name, self.description)

class Weapon(Item):

    def __init__(self, name, description, power):
        super().__init__(name, description)
        self.power = power

coin = Item('coin', 'a gold coin')
sword = Item('sword', 'sharp')
inventory = Inventory()
inventory.add(coin)
inventory.add(sword)
print(len(inventory))
print(sword in inventory)
sword = Weapon('sword', 'sharp', 50)
inventory = Inventory()
inventory.add(sword)
for item in inventory:
    print(item.description)


def get_numbers():
    numbers = [4, 8, 15, 16]
    for number in numbers:
        yield number

numbers = get_numbers()
print(numbers)
print(next(numbers))
print(next(numbers))