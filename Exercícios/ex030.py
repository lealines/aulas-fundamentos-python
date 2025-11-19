from time import sleep

import random

opcoes = ['pedra', 'papel', 'tesoura']

escolha_computador = random.choice(opcoes)
escolha_jogador = input('Escolha Pedra, Papel ou Tesoura: ').lower()

print()
sleep(1)
print(escolha_computador.title())

if escolha_jogador == escolha_computador:
    print('EMPATE!')

elif escolha_jogador == 'tesoura' and escolha_computador == 'papel' or escolha_jogador == 'pedra' and escolha_computador == 'tesoura' or escolha_jogador == 'papel' and escolha_computador == 'pedra':
    print('VENCESTE!')

else:
    print('PERDESTE!')
