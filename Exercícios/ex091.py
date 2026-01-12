class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def mostrar(self):
        print(f'O livro com o título "{self.titulo}" foi escrito pelo autor {self.autor}.\n')


livro1 = Livro('A Cicatriz', 'Maria Francisca Gama')
livro2 = Livro('Isto Começa Aqui', 'Colleen Hoover')
livro3 = Livro('A Criada', 'Freida McFadden')

livro1.mostrar()
livro2.mostrar()
livro3.mostrar()