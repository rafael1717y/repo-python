"""Exceções IO

"""

try:
    arquivo_contatos = open('/home/rafael/PycharmProjects/repo-python/python_io/contat.csv', encoding='latin_1', mode='w+')
    for linha in arquivo_contatos:
        print(linha, end='')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
finally:
    arquivo_contatos.close()
