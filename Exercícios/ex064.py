aluno = dict()

aluno['Nome'] = input('Digite o nome do/a aluno/a: ')
print()
aluno['Média'] = float(input(f'Digite a média do/a {aluno["Nome"]}: '))
print()
aluno['Situação'] = 'APROVADO/A' if aluno['Média'] >= 9.5 else 'REPROVADO/A'

print(f'O aluno/a {aluno['Nome']} teve a média de {aluno['Média']} por isso foi {aluno['Situação']}.')