class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title() # _Programa_nome - privado nao vai pra classe filha por isso usar um só underline (por convenção).
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()

    def dar_like(self):
        self._likes += 1

    def __str__(self):
        return f'{self._nome}  - {self.ano} - {self._likes} Likes'

    #def imprime(self):
        #print(f'{self._nome}  - {self.ano} - {self._likes} Likes')



class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)  #chamando a classe mãe e extendendo.
        self.duracao = duracao

    def retorna_cadastro_diferenciado(self):
        pass

    def __str__(self): #representação textual do objeto
        return  f'{self._nome}  - {self.duracao} min - {self._likes} Likes'



class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome}  - {self.ano} - {self.temporadas} temporadas - {self._likes} Likes'


class Playlist:
    def __init__(self, nome, programas):
        self.nome = nome
        self._programas = programas

    @property
    def listagem(self):
        return self._programas

    @property
    def tamanho(self):
        return len(self._programas)


    #def tamanho(self):
    #    return len(self.programas)



vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()

#print(f'{vingadores.nome} - {vingadores.duracao} : {vingadores.likes}')

atlanta = Serie('atlanta', 2018, 2)
tmep = Filme('todo mundo em panico', 1999, 100)
demolidor  = Serie('Demolidor', 2016, 2)
tmep.dar_like()
tmep.dar_like()
demolidor.dar_like()
demolidor.dar_like()

atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
atlanta.dar_like()
print(f'{atlanta.nome} - {atlanta.temporadas} : {atlanta.likes}')

filmes_e_series = [vingadores, atlanta, tmep]

playlist_fim_de_semana = Playlist('fim de semana', filmes_e_series)

#print(f'Tamanho da playlist: {len(playlist_fim_de_semana.listagem)}')


for programa in playlist_fim_de_semana.listagem:
    print(programa)


    # verificando se um objeto tem um atributo ou não (hasattr)
    #if hasattr(programa, 'duracao'):
    #    detalhes = programa.duracao
    #else:
    #    detalhes = programa.temporadas

    #print(f'{programa.nome} -{detalhes} D: {programa.likes}')

print(f'Tá ou não tá?{demolidor in playlist_fim_de_semana.listagem}')






