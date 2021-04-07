"""
Ascii2 representação de 128 caracteres pensando para o contexto americano. Sem caracteres com acento
Encoding latin-1 (pensando para países europeus). Utf-8 (caracteres arábicos, etc).
O interpretador pergunta para o SO qual o encoding ele está utilizando. Máquina usando utf-8 mas arquivo está 
em latin_1. Ao abrir um arquivo com uma codificação diferente da que ele foi escrito, alguns caracteres podem apresentar erros,
ou, em alguns SO, pode ser lançado uma exceção.
Formas -> falar para a função open abrir com um encodind diferente
"""
## Usar essa forma. Iterar diretamento sobre a variável arquivo_contatos sem invocar o método readlines()
#conteudo = arquivo_contatos.readlines() - #método readlines => arquivo com um milhão de elementos. Gera uma problema de memória.

try:
    with open('/home/rafael/PycharmProjects/repo-python/python_io/contatos.csv', encoding='latin_1') as arquivo_contatos:
        for linha in arquivo_contatos:
            print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')






"""
conteudo = arquivo_contatos.readline(10) # lerá a linha toda até encontrar um caractere \n - ler os 10 primeiros caracteres
print(conteudo)

conteudo = arquivo_contatos.readline() # lerá a linha toda até encontrar um caractere \n
print(conteudo)
"""
#for linha in conteudo:
#    print(linha, end='') #abre sem quebrar um nova linha

"""Vantagem do readline
Não carrega todo o arquivo em memória. """
