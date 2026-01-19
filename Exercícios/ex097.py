class Livro:
    def __init__(self, titulo, ano, autor, disponibilidade):
        self.__titulo = titulo
        self.__ano = ano
        self.__autor = autor
        self.__disponibilidade = disponibilidade

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, novo_titulo):
        self.__titulo = novo_titulo

    @property
    def ano(self):
        return self.__ano

    @ano.setter
    def ano(self, novo_ano):
        self.__ano = novo_ano

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, novo_autor):
        self.__autor = novo_autor

    @property
    def disponibilidade(self):
        return self.__disponibilidade

    @disponibilidade.setter
    def disponibilidade(self, nova_disponibilidade):
        self.__disponibilidade = nova_disponibilidade


livro1 = Livro('A Criada', 2023, 'Freida McFadden', True)

print(f'Título: {livro1.titulo}')
print(f'Ano: {livro1.ano}')
print(f'Autor: {livro1.autor}')
estado = 'Disponível' if livro1.disponibilidade else 'Indisponível'
print(f'Disponibilidade: {estado}')

livro1.titulo = 'A Criada - Edição Especial'
print(f'\nNovo Título: {livro1.titulo}')

livro1.disponibilidade = False

estado = 'Disponível' if livro1.disponibilidade else 'Indisponível'
print(f'Disponibilidade: {estado}')