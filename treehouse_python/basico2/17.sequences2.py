rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']

print(rainbow[::2])
# inversão
print(rainbow[::-1])

my_name = 'Rafael'
print(my_name[:3])

student_gpas = [4.0, 2.3, 3.5, 3.7, 3.9, 2.8, 1.5, 4.0]
sliced_gpas = student_gpas[3:6]
print(sliced_gpas)

nums = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(len(nums))
print(max(nums))
print(min(nums))

my_string = 'tree'
print(len(my_string))
print(max(my_string))

mixed = 'treehouse2021'
print(max(mixed))
print(min(mixed))


docs = """tuple are imutable sequences, typically used to store collections
of heterogeneous data. Tuples are also used for cases where an inmutable
sequence of homogenous data is need. """

if 'tuple' in docs:
    print('tuple is here')
else:
    print('tuple is not here')

# Count and Index
print(docs.count('tuple'))

print(docs.index('tuple'))

teachers = ['Alena', 'Ashley', 'Nicole', 'Treasure', 'Nicole']

print(teachers.index('Nicole'))

object1 = ["1", "2", "3", "4", "5"]
object2 = [6, 7, 8, 9, 10]

object1 = object1 + object2
print(object1)

str = 'python'
print(str*5)



















