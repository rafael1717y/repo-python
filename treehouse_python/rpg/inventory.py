class Inventory:

    def __init__(self):
        self.slots = []

    def add(self, item):
        self.slots.append(item)

    def __len__(self):
        return len(self.slots)

    def __contains__(self, item):
        return item in self.slots

    def __iter__(self):
        """Para iterar no objeto"""
        #for item in self.slots:
        #    yield item
        yield from self.slots