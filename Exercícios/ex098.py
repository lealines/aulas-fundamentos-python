class Produto:
    def __init__(self, nome, quantidade_stock):
        self.__nome = nome
        self.__quantidade_stock = quantidade_stock

    @property
    def quantidade_stock(self):
        return self.__quantidade_stock

    @quantidade_stock.setter
    def quantidade_stock(self, valor):
        if valor < 0:
            self.__quantidade_stock = 0
            print('Valor é negativo!')
        else:
            self.__quantidade_stock = valor

    def mostrar_stock(self):
        print(f'O produto {self.__nome} tem {self.__quantidade_stock} unidades em stock.\n')

    def adicionar_stock(self, quantidade):
        if quantidade > 0:
            self.quantidade_stock = self.quantidade_stock + quantidade
            print(f'Foram adicionados {quantidade} ao stock de {self.__nome}.\n')
        else:
            print('Valor negativo!')

produto = Produto('Computadores', 5)

produto.mostrar_stock()

produto.adicionar_stock(5)

produto.mostrar_stock()