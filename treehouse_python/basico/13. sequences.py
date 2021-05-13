my_name = "Rafael"
groceries = ['roast beef', 'cucumbers', 'lettuce', 'dog food']

for letter in my_name:
    print(letter)

"""
index = 1
for item in groceries:
    print(f'{index}.{item}')
    index+=1
"""

# Enumerate
for index, item in enumerate(groceries, 1):
    print(f'{index}.{item}')

# Ranges - 3 argumentos
# ranges excludem o valor de stop

for i in range(0, 10, 1):
    print(i)

for i in range(10): # default
    print(i)

