
class Cliente:

    def __init__(self, nome):
        self.__nome = nome

    # get
    @property # esse metodo representa uma propriedade
    def nome(self):
        return self.__nome.title() # deixando a primeira letra em maiusculo

    # set
    @nome.setter
    def nome(self, nome):
        self.__nome = nome


if __name__ == "__main__":
  pass