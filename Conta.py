
class Conta:

    def __init__(self, numero, titular, saldo, limite):
        print("Construindo objeto ... {}".format(self))
        #  <__atributo> para deixar o atributo como privado
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    def extrato(self):
        print("Saldo de {} do titular {}".format(self.__saldo, self.__titular))

    def deposita(self, valor):
        self.__saldo += valor

    # deixando o metodo privado
    def __pode_sacar(self, __valor_a_sacar):
        valor_a_sacar = self.__saldo + self.__limite
        return valor_a_sacar <= valor_disponivel_a_sacar


    def saca(self, valor):
        # verificando o valor para saque
        if(self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print("O valor {} passou o limite".format(valor))

    def tranfere(self, valor, destino):
        self.saca(valor)
        destino.deposita(valor)

    # get devolve um valor
    @property
    def saldo(self):
        return self.__saldo

    @property
    def titular(self):
        return self.__titular

    @property
    def limite(self):
        return self.__limite

    @staticmethod # metodo estatico
    def codigo_banco():
        return "001"

    @staticmethod
    def codigos_bancos():
        return {
            'BB': '001',
            'Caixa': '104',
            'Bradesco': '237'
        }


    #  set altera um valor
    @limite.setter
    def set_limite(self, limite):
        self.__limite = limite

    @saldo.setter
    def set_saldo(self, saldo):
        self.__saldo = saldo

    @titular.setter
    def set_titular(self, titular):
        self.__titular = titular





if __name__ == "__main__":
  pass
