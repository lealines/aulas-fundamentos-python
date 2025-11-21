from random import randint

qtd_jogadores = int(input('Digite quantos jogadores vão jogar: '))
jogadores = {}

for c in range(qtd_jogadores):
    nome = input(f'Digite o nome do {c+1}º jogador: ')
    jogada = randint(1,6)

    jogadores[nome] = jogada

auxiliar = jogadores.copy()
ranking = list()

while auxiliar:

    maior_jogador = ''
    maior_valor = 0

    for jogador, jogada in auxiliar.items():
        if jogada > maior_valor:
            maior_jogador = jogador
            maior_valor = jogada

    ranking.append((maior_jogador, maior_valor))
    del auxiliar[maior_jogador]

for tupla in ranking:
    for elemento in tupla:
        print(f'{elemento}')