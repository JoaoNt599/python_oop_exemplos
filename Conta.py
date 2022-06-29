
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    def saca(self, valor):
        self.__saldo -= valor

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)


if __name__ == "__main__":
    conta = Conta(123, "João", 55.5, 1000.0)
    print(conta._Conta__limite)
    print(conta._Conta__saldo)

    conta2 = Conta(321, "João", 100.0, 1000.0)
    conta2.tranfere(10.0, conta2, conta)
    print(conta._Conta__extrato)
