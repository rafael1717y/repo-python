
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    @property
    def nome(self):  #msm nome do atributo. Metodos que dão acesso aos objetos. O atributo tem que ser privado
        print("chamando @property nome()")
        return self.__nome.title()

    @nome.setter
    def nome(self, nome):
        print("chamando setter nome()")
        self.__nome = nome

