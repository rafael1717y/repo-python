contato_carol = '11,Carol, carol@carol.com.br\n'
contato_andreza = '12,Andreza,andreza@gmai.com\n'

with open('/home/rafael/PycharmProjects/repo-python/python_io/contatos1escrita.csv', encoding='latin_1', mode='w') as arquivo1:
    arquivo1.write(contato_carol)

with open('/home/rafael/PycharmProjects/repo-python/python_io/contatos1escrita.csv', encoding='latin_1', mode='a') as arquivo2:
    arquivo2.write(contato_andreza)



