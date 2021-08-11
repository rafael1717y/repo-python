import sys
from collections import namedtuple

class MinhaClasse():
    def __init__(self):
        self.elementos = []
        self.novos_elementos = []

    def abrir_arquivo(self):
        with open('dados.csv') as file:
            file_iter = iter(file)
            cabecalho = next(file_iter).strip('\n').split(';')
            Servidor = namedtuple('Servidor', cabecalho)
            for line in file_iter:
                data = line.strip('\n').split(';')
                servidor = Servidor(*data)
                self.elementos.append(servidor)

    def registrar_afastamento(self, nome, resultado):
        try:
            print('registrando um afastamento')
            print('linh 19', nome)
            resultado = 'ok'
            self.gravar_dados(nome, resultado)
        except:
            print('erro. Reiniciando o script')
            sys.exit()

    def gravar_dados(self, nome, resultado):
        self.novos_elementos.append(nome)
        self.novos_elementos.append(resultado)
        print('dados gravados', self.novos_elementos)

    def trabalhar_dados(self):
        for elemento in self.elementos:
            try:
                #print(elemento)
                nome = elemento.NOME
                #print(elemento.MATRICULA)
                resultado = elemento.RESULTADO
                self.registrar_afastamento(nome, resultado)
            except Exception:
                print('erro')


m = MinhaClasse()
m.abrir_arquivo()
m.trabalhar_dados()


