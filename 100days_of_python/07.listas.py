import random

states_of_america = ["Delaware", "Pennsylvani", "New Jersey", "Georgia"]
#print(states_of_america[0])
states_of_america[1] = "Pencilvania"
states_of_america.append("New State")
states_of_america.extend(["Angeland", "Jack Land"])
#print(states_of_america)

str_inp = "Hello, from, AskPython"
op = str_inp.split(",")
print(op)

names_string = input("Give me everybody's names, seperated by a comma. ")
names = names_string.split(",")
elemento_aleatorio = random.randint(0, (len(names) -1))
pessoa_escolhida = names[elemento_aleatorio]
print(f'{pessoa_escolhida} is going to buy the meal!')


