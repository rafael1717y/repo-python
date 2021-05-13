import copy

class FilledList(list):
    def __init__(self, count, value, *args, **kwargs):
        super().__init__()
        for _ in range(count):
            self.append(copy.copy(value))


        
fl = FilledList(9, 2)
print(len(fl))
print(fl)

fl2 = FilledList(2, [1, 2, 3])
print(len(fl2))
print(fl2)


fl2[0][1] = 5
print(fl2)