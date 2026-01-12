class Produto:
    def __init__(self, nome, quantidade_stock):
        self.nome = nome
        self.quantidade_stock = quantidade_stock

    def mostrar(self):
        print(f'O produto {self.nome} tem {self.quantidade_stock} unidades em stock.')

    def aumentar_stock(self, valor):
        self.quantidade_stock += valor


produto = Produto('Telemóvel', 50)

produto.mostrar()
produto.aumentar_stock(70)
produto.mostrar()