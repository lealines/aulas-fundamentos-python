def analisar_aluno(nome, notas):

    soma = 0

    for nota in notas:

        soma = soma + nota

    if len(notas) == 0:

        media = 0

    else:

        media = soma / len(notas)

    if media >= 10:

        situacao = 'APROVADO(A)'

    else:

        situacao = 'REPROVADO(A)'

    print('\n--- Resultado Final ---')

    print(f'\nNome do Aluno: {nome}')
    print(f'Média: {media:.2f}')
    print(f'Situação: {situacao}')


nome_input = input('Digite o nome do/a aluno/a: ')

lista_notas = []

qtd_notas = int(input(f'Quantas notas deseja inserir para o/a aluno/a {nome_input}? '))

for i in range(qtd_notas):

    nota = float(input(f'Digite a {i + 1}ª nota: '))

    lista_notas.append(nota)

analisar_aluno(nome_input, lista_notas)