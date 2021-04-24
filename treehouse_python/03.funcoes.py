import math

def split_check(total, number_of_people):
    if number_of_people <= 1:
        raise ValueError("More than 1 person is required to split the check.")
    return math.ceil(total / number_of_people)

try:
    total_due = float(input("what is the total? "))
    number_of_people = int(input("how many people? "))
    amont_due = split_check(total_due, number_of_people)
except ValueError as err:
    print("Oh no! That's not a valid value. Try again!")
    print(f'{err}')

else:
    print(f'Each person owes {amont_due}')
