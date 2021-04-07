"""
Abertura no modo w trunca o arquivo. Apaga o original e começa um outro
Modo a -> apensa ao final.
No módo w o arquivo só é disponível para escrita.
Para habilitar o modo de escrita e leitura passa um mais depois do + -  w+ - mode de update
a+ -- para escrita e leitura.
"""

arquivo_contatos = open("/home/rafael/PycharmProjects/repo-python/python_io/contatos1escrita.csv", encoding='latin_1', mode='a+')

contatos = ['11,Carol,carol@carol.com.br\n',
            '12,Ana,ana@ana.com.br\n',
            '13,Tais, tais@tais.com.br\n',
            '14,Felipe,felipe@felipe.com.br\n']

for contato in contatos:
    arquivo_contatos.write(contato)

arquivo_contatos.flush()  #força a inserção dos dados dentro do arquivo e o arquivo continuará aberto.
#arquivo_contatos.close()
#input logo após o for mas escrita ainda nao está no arquivo. Quando aperta o enter o programa precisou parar para os
#conteúdos serem escritos realmente. Problema em programas que não são encerrados. A escrita só é realizada quando
#o arquivo não está mais sendo trabalhado. Por isso é importante colocar o close para indicar que o arq nao está mais sendo trabalhado.

arquivo_contatos.seek(28) # faz o ponteiro retornar para o começo do arquivo e começa a iterar a partir daí.
arquivo_contatos.write('12,Ana,ana@ana.com.br\n'.upper()) ### se colocar string maior corta da seguinte...
arquivo_contatos.flush()
arquivo_contatos.seek(0)

for linha in arquivo_contatos:
    print(linha)



#input('Pressiona <Enter> para encerrar o programa')
#arquivo_contatos.write(contato)

