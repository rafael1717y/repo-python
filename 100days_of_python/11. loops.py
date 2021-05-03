notas_estudantes = input("Entre com uma lista de notas de estudantes").split()

##
for n in range(0, len(notas_estudantes)):
    notas_estudantes[n] = int(notas_estudantes[n])
print(notas_estudantes)

#  1
for nota in notas_estudantes:
    nota_alta = nota# --> nota alta = 1
    if nota > nota_alta:
        resultado = nota
    else:
        resultado = nota_alta

print('linha 15', resultado)