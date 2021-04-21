import random

random_integer = random.randint(1, 10)
print(random_integer)

#0.00000000  0.99999999
random_float = random.random()
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score} ")

randon_side = random.randint(0, 1)
if randon_side == 1:
    print("Heads")
else:
    print("Tails")