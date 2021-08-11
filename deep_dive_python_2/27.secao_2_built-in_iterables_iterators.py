# ITERABLES

r = range(10)
print(r)

print('__iter__' in dir(r))
print('__next__' in dir(r))

print(iter(r))

for num in r:
    print(num)

# ITERATOR

z = zip([1,2, 3], 'abc')

print('__iter__' in dir(z))

print(list(z))
print(list(z))

f = open('cars.csv')
print(next(f))
print(f.__next__())
print(f.readline())
f.close()

with open('cars.csv') as f:
    for row in f:
        print(row, end='')


with open('cars.csv') as f:
    print(type(f))
    print('__iter__' in dir(f))
    print('__next__' in dir(f))

# Verificando se é um iterator
with open('cars.csv') as f:
    print(iter(f) is f)


l = [1, 2, 3]
print(iter(l) is l)

# Menos eficiente
with open('cars.csv') as f:
    l = f.readlines()
print(l)

origins = set()
with open('cars.csv') as f:
    rows = f.readlines()
for row in rows[2:]:
    origin = row.strip('\n').split(';')[-1]
    origins.add(origin)

print(origins)

# Mais eficiente. Sem armazenar todos os dados.
# ---------------------------------------------

origins = set()
with open('cars.csv') as f:
    next(f)
    next(f)
    for row in f:
        origin = row.strip('\n').split(';')[-1]
        origins.add(origin)

print(origins)


e = enumerate('Python Rocks!')
print(iter(e) is e) # True

print(list(e))
print(list(e)) # esvaziou o iterator

d = {'a':1, 'b':2}
keys = d.keys()
print(iter(keys) is keys)


