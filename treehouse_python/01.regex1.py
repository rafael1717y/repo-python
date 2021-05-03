import re
alvo1 = "INDENIZAÇÃO ESTRATEG. 01/10/2010 08:00 10/10/2020 Ativo"
alvo2 = "ADICIONAL NOTURNO 01/10/2010 08:00 10/10/2020 Ativo"
alvo3 = "PERICULOSIDADE 01/10/2010 08:00 10/10/2020 Encerrado"

# match procura no começo da string, search em qlq posição.

periculosidade = r'PERICULOSIDADE'
adicional_noturno = r'ADICIONAL NOTURNO'

periculosidade  = re.match(periculosidade, alvo3)
print(re.search(adicional_noturno, alvo2))

print(periculosidade)

# Data
print(re.search(r'\d\d\/\d\d\/\d\d\d\d', alvo1))
#print(re.search(r'\d{2}\/d{2}\(/d{4})', alvo1))


# Hora
print(re.search(r'\d\d\:\d\d', alvo1))

#ulr(r'polls/(?P<id>\d+)/')  -- escape para desconsiderar () como grupo de captura.

print(re.search(r'\d', 'Johnny-5'))


def first_number(string):
    first_number = re.search(r'\d', string)
    return first_number

print(first_number('rafeael8982a a '))

def find_numbers(count, string):
    number = re.search(r'\d' * count, string)
    return number

print(find_numbers(4, alvo3))


### esta solucionou ---- /// o tipo de adicional
a = re.search(r'\w+\w*', alvo1)
print(a.group(0))
###############################################

def phone_numbes(string):
    resultado = re.findall(r'\d{3}-\d{3}-\d{4}', string)
    return resultado

print(phone_numbes("20203 ahahs 555-555-5555."))


def find_words(count, string):
    resultado = re.findall(r'\w' * count, string)
    return resultado

#print(find_words(4, "dog, cat, baby, balloon, me"))

data = "1212 d d rafael1717yy@gmail.com aladdha 1212 23"

# email
#print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))

##
#print(re.findall(r'\b[PERICULOSDA]+\b', alvo1, re.3))


print(re.findall(r'''(\d\d\/\d\d\/\d\d\d\d)'''), alvo1)



























