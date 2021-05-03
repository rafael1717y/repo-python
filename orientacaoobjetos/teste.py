import csv


def qual_nome_funcao():
    with open('/home/rafael/PycharmProjects/repo-python/orientacaoobjetos/teste.csv' as csv_file':
        csv_reader = csv_file.reader('/home/rafael/PycharmProjects/repo-python/orientacaoobjetos/teste.csv', delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            print(row[0])

qual_nome_funcao()