s = 'I sleep all night, and I work all day'

for char in s:
    print(char)

iter_s = iter(s)
print(iter_s)

print(next(iter_s))
print(iter_s.__next__())

# Iterando num arquivo sem colocar tudo numa memória
"""
with open('cars.csv') as file:
    for line in file:
        print(line, end='')
"""

with open('cars.csv') as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            # header_row
            headers = line.strip('\n').split(';')
            print('headers', headers)
        elif row_index == 1:
            # data type row
            data_tyes = line.strip('\n').split(';')
            print('types', data_tyes)
        else:
            # data row
            data = line.strip('\n').split(';')
            print(data)
        row_index += 1

# 3


def cast(data_type, value):
    if data_type == 'DOUBLE':
        return float(value)
    elif data_type == 'INT':
        return int(value)
    else:
        return str(value)


data_types = ['STRING', 'DOUBLE', 'INT', 'DOUBLE', 'DOUBLE', 'DOUBLE', 'DOUBLE', 'INT', 'CAT']
data_row = ['Chevrolet Chelle Malibu', '18.0', '8', '307.0', '130.0', '3504.', '12.0', '70', 'US']

print(list(zip(data_types, data_row)))


def cast_row(data_types, data_row):
    return [cast(data_type, value)
            for data_type, value in zip(data_types, data_row)]


from collections import namedtuple
cars = []

with open('cars.csv') as file:
    row_index = 0
    for line in file:
        if row_index == 0:
            # header_row
            headers = line.strip('\n').split(';')
            Car = namedtuple('Car', headers)
        elif row_index == 1:
            # data type row
            data_tyes = line.strip('\n').split(';')
            print('types', data_tyes)
        else:
            # data row
            data = line.strip('\n').split(';')
            data = cast_row(data_tyes, data)
            car = Car(*data)
            cars.append(car)
        row_index += 1

print(cars)

#4 - Usando iterators manually

from collections import namedtuple
cars = []

with open('cars.csv') as file:
    file_iter = iter(file) # file é um iterator
    headers = next(file_iter).strip('\n').split(';')                 # primeira linha é o cabeçalho
    Car = namedtuple('Car', headers)
    data_types = next(file_iter).strip('\n').split(';')              # date tipes segunda filha
    ## já consumiu os outros elementos..começa loop da 3a. linha
    for line in file_iter:
        data = line.strip('\n').split(';')
        data = cast_row(data_tyes, data)
        car = Car(*data)
        cars.append(car)

print(cars)
