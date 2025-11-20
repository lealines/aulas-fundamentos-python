aluno1 = ['Telmo', 14]
aluno2 = ['Solinho', 17]
aluno3 = ['Pedro', 16]
aluno4 = ['Letícia', 15]

turma = list()

turma.append(aluno1[:])
turma.append(aluno2[:])
turma.append(aluno3[:])
turma.append(aluno4[:])

for aluno in turma:
    print(f'O/A aluno/a {aluno[0]} tem média de {aluno[1]} valores.')
