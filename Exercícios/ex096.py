from statistics import mean

class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.__notas = notas
        self.__media = self.media()

    def media(self):
        return mean(self.__notas)

    def verificar_situacao(self):
        media = self.media()
        if media >= 9.5:
            return 'Aprovado'
        else:
            return 'Reprovado'

aluno1 = Aluno('Inês', [15, 13, 9])

print(f'Nome: {aluno1.nome}')
print(f'Média: {aluno1.media():.2f}')
print(f'Situação: {aluno1.verificar_situacao()}')