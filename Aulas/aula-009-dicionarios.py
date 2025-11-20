turma = []
qtd_alunos = 5
aluno = dict()  # ou {}

for c in range(qtd_alunos):

    aluno['Nome'] = input(f'Digite o nome do {c+1}º aluno: ')
    aluno['Média'] = float(input('Digite a média: '))
    aluno['Situação'] = 'Aprovado' if aluno['Média'] >= 9.5 else 'Reprovado'

    turma.append(aluno.copy())

print(turma)