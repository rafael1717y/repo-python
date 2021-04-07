class Calculadora:
    __area_paredes: float
    __area_teto:float

    def calcular_area_paredes(self, comodo):
        # passando o obj que já contém os valores de largura, altura, profundidade.
        self.__area_paredes =  2 * (comodo.largura + comodo.profundidade) * comodo.altura
        return self.__area_paredes

    def calcular_area_teto(self, comodo):
        self.__area_teto = comodo.largura * comodo.profundidade
        return self.__area_teto

    def calcular_litragem_necessaria(self):
        if self.__area_paredes <= 0 or self.__area_teto <= 0:
            print('Não é possível calcular a litragem com os valores informados')
            exit()
        return (self.__area_paredes + self.__area_teto) / 10