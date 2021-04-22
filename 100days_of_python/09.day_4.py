import random

rock = 'ROCK'
paper = 'PAPER'
scissors = 'SCISSORS'

escolha = int(input("What do yu chose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
print(escolha)
selecao = ['Rock', 'Paper', 'Scissors']

if (escolha == 0 or escolha == 1) :
    comp_escolha = random.randrange(0, (len(selecao) - 1))

else:
    comp_escolha = selecao[2]

print('Escolha usuario', escolha)
print('Escolha do computador:', comp_escolha)


#rock wings against scissors
#scissors wins agains papers
#papers wings against rock




