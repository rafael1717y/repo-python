import csv, pickle
from contato import Contato

def csv_para_contatos(caminho, encoding):
    contatos = []

    with open(caminho, encoding=encoding) as arquivo:
        leitor = csv.reader(arquivo)

        for linha in leitor:
            ## desempacotamento ##
            id, nome, email = linha
            contato = Contato(id, nome, email)
            contatos.append(contato)

    return contatos

def contatos_para_pickle(contatos, caminho):
    #salvando os arquivos
    with open(caminho, mode='wb') as arquivo: #abrir arq binário no modo de escrita
        pickle.dump(contatos, arquivo)

def pickle_para_contatos(caminho):
    with open(caminho, mode='rb') as arquivo:
        contatos = pickle.load(arquivo)

    return contatos
