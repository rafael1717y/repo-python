"""
import re
alvo1 = "INDENIZAÇÃO ESTRATEG. 01/10/2010 08:00 31/10/2020 Ativo"
alvo2 = "ADICIONAL NOTURNO 01/10/2010 08:00 10/10/2020 Ativo"
alvo3 = "PERICULOSIDADE 01/10/2010
alvo4 = "INSALUBRIDADE 01/10/2010 08:00 10/10/2020 Encerrado"

# 01. Extração das datas
#print(re.search(r'\d\d\/\d\d\/\d\d\d\d', alvo1))
datas = re.findall(r'\d{2}/\d{2}/\d{4}', alvo1)
print(datas)

hora = re.findall(r'\d{2}:\d{2}', alvo1)
print(hora)


## usar esse - duas datas
#print(re.findall(r'''(\d\d\/\d\d\/\d\d\d\d)''', alvo1))

#(?P<data_ini>\d\d\/\d\d\/\d\d\d\d)

#agora sim

#\w+\w*

### Esse regex usar

lista = []

nome = "Rafael"

linha = re.search(r'''(?P<tipo>\D{13})
                      (?P<data_ini>\d{2}/\d{2}/\d{4})
                      (?P<hora>\s\d{2}:\d{2})
                      (?P<data_fim>\s\d{2}/\d{2}/\d{4})
                      (?P<situacao>\s[a-zA-Z]+$)
''', alvo3, re.X|re.M)

#print(linha)
dicionario_do_regex = linha.groupdict()
dicionario_do_regex.update(nr = 1, nome = 'Rafael', matricula = '2093501')
lista.append(dicionario_do_regex)

print(lista)

uio
[98i]


linha = re.search(r'''(?P<tipo>[a-zA-Z](?:[a-zA-Z])\s+)
                      (?P<data_ini>\d{2}/\d{2}/\d{4})
                      (?P<hora>\s\d{2}:\d{2})
                      (?P<data_fim>\s\d{2}/\d{2}/\d{4})
                      (?P<situacao>\s[a-zA-Z]+$)
''', alvo1, re.X|re.M)

print(linha)
print(linha.groupdict())
"""





















