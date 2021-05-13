class Inventory:

    def __init__(self):
        self.slots = []

    def add_item(self, item):
        self.slots.append(item)


class SortedInventory(Inventory):

    def add_item(self, item):
        super().add_item(item)
        list.sort(self.slots)


s = SortedInventory()
s.add_item(5)
s.add_item(1)
print(s.slots)