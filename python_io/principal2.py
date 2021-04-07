import contatos_util

try:
    #contatos = contatos_util.csv_para_contatos('/home/rafael/PycharmProjects/repo-python/python_io/contatos.csv', 'latin_1')
    #contatos_util.contatos_para_pickle(contatos, '/home/rafael/PycharmProjects/repo-python/python_io/contatos.pickle')

    contatos = contatos_util.pickle_para_contatos('/home/rafael/PycharmProjects/repo-python/python_io/contatos.pickle')

    for contato in contatos:
        print(f'{contato.id} - {contato.email} - {contato.email}')
except FileNotFoundError:
    print('Arquivo não encontrado')
except PermissionError:
    print('Sem permissão de escrita')
