jogador = dict()

print('--- APROVEITAMENTO DO JOGADOR ---')
print()

jogador['Nome'] = input('Digite o nome do jogador: ')
jogador['Jogos'] = int(input('Digite a quantidade de jogos: '))
jogador['Golos'] = int(input('Digite a quantidade de golos marcados: '))
jogador['Média'] = jogador['Golos'] / jogador['Jogos']

print()
for chave, valor in jogador.items():
    print(f'{chave} --> {valor}')