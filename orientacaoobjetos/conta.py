from cliente import Cliente

class Conta:

    def __init__(self, numero, titular, saldo, limite):
        # self é a referência que sabe onde encontrar o objeto que guardou o endereço em memória.
        print("Construindo o objeto ...{}".format(self))
        # self tem o endereco e vai até  lá e até acessa o objeto
        # atributos o que um obj têm e cpto o que faz.
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de R$ {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def transfere(self, valor, destino):
        ##chamando um método a partir do self tbm
        self.saca(valor)
        destino.deposita(valor)

    def get_saldo(self):
        return self.__saldo

    def get_titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @limite.setter
    def limite(self, limite):
        self.__limite = limite



#conta, conta2 é a referência.
#conta1 = Conta(123, "Rafael", 100, 1000.0)
#conta2 = conta1
conta = Conta(4444, "José", 200, 500)
conta2 = Conta(5555, 'Maria', 100, 100)

conta2.transfere(10.0, conta)
print(conta2.extrato())
print(conta.get_saldo())
conta.limite(888888)
print(conta.limite())

cliente = Cliente("marco")
print(cliente.nome)
cliente.nome = "marco"
conta.limite


"""
outraRef = None
#print(conta1)
# a variável (conta) sabe onde está o objeto .(vai) até ele
#print(conta1.limite)
#print(conta2.extrato())
print(conta1.extrato())
print(conta1.deposita(100))
print('===========')
print(conta2.extrato())
print(conta2.saca(50))
print(conta2.extrato())
print('==@@@')
print(outraRef)
conta1.saldo = 0
print(conta1.saldo)
"""