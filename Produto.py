
class Produto:

    def __init__(self, codigo: int, descricao:str, preco: float, quantidade_estoque:float)->None:
        self.__codigo = codigo
        self.__descricao = descricao
        self.__preco = preco
        self.__quantidade_estoque = 0


    #   Metodos
    def entrada_estoque(self, quantidade: float)->None:
        self.__quantidade_estoque += quantidade

    def saida_estoque(self, quantidade: float)->None:
        self.__quantidade_estoque -= quantidade

    def visualizar_quantidade_estoque(self)->None:
        print(f'A quantidade em estoque é {self.__quantidade_estoque}')


    #   Get e Set
    @property
    def codigo(self)->int:
        return self.__codigo

    @property
    def descricao(self)->str:
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao: str)->None:
        self.__descricao = descricao

    @property
    def preco(self)->float:
        return self.__preco

    @preco.setter
    def set_preco(self, preco: float)->None:
        if preco <= 0:
            print("Erro: preço deve ser um valor positivo.")
        else:
            self.__preco = preco

    @property
    def quantidade_estoque(self)->float:
        return self.__quantidade_estoque


if __name__ == "__main__":
    um_produto = Produto(1, "Som automotivo", 574.20, 0)
    outro_produto = Produto(2, "Cera líquida", 15.0, 0)
    print(um_produto.preco)
    print(outro_produto.preco)


    """
    um_produto.entrada_estoque(4.0)
    um_produto.visualizar_quantidade_estoque()
    um_produto.saida_estoque(2)
    um_produto.visualizar_quantidade_estoque()
    print(f"código: {um_produto.get_codigo()}")
    print(f"descrição: {um_produto.get_descricao()}")
    print(f"preço: {um_produto.get_preco()}")
    """





