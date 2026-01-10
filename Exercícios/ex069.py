equipa = []

while True:

    jogador = dict()
    print('-' * 30)
    jogador['Nome'] = input('Nome do jogador: ')
    total_jogos = int(input(f'Quantos jogos o {jogador["Nome"]} jogou? '))

    golos_jogo = []
    soma_golos = 0

    for c in range(total_jogos):

        golos = int(input(f'  Quantos golos na partida {c + 1}? '))
        golos_jogo.append(golos)
        soma_golos += golos

    jogador['Golos'] = golos_jogo
    jogador['Total'] = soma_golos

    if total_jogos > 0:

        jogador['Média'] = soma_golos / total_jogos

    else:

        jogador['Média'] = 0

    equipa.append(jogador.copy())

    while True:
        resposta = input('Quer continuar? [S/N] ').strip().upper()

        if resposta in 'SN':

            break

        print('Erro! Responda apenas S ou N.')

    if resposta == 'N':

        break


print('\n' + '=' * 45)
print(f'{"NOME":<15} {"GOLOS":<20} {"TOTAL":<5}')
print('-' * 45)


for j in equipa:

    print(f'{j["Nome"]:<15} {str(j["Golos"]):<20} {j["Total"]:<5}')
    print('=' * 45)


while True:

    procura = input('Digite o NOME do jogador para ver detalhes (ou "sair"): ').strip()

    if procura.lower() == 'sair':
        break

    encontrado = False

    for j in equipa:

        if j['Nome'].lower() == procura.lower():

            print(f' -- LEVANTAMENTO DO JOGADOR {j["Nome"]}:')

            for i, g in enumerate(j['Golos']):

                print(f'    No jogo {i + 1} fez {g} golos.')
            print(f'    Média de golos: {j["Média"]:.2f}')

            encontrado = True

            break

    if not encontrado:

        print(f'Erro! O jogador "{procura}" não foi encontrado na lista.')
    print('-' * 40)

print('\n<<< PROGRAMA ENCERRADO >>>')