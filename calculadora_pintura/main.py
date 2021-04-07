from calculadora import Calculadora
from comodo import Comodo
#Criando um objeto calculadora
calc = Calculadora()

comodo = Comodo(input('Qual a largura do comodo?'),
                input('Qual a profunidade do cômodo?'))

#calc.area_paredes= float = 2 * (largura + profundidade) * altura

print("A área das paredes é: ",
      calc.calcular_area_paredes(comodo))

print('A área do teto é:',
      calc.calcular_area_teto(comodo))

print('A litragem de tinta necessária é:',
      calc.calcular_litragem_necessaria()
)


