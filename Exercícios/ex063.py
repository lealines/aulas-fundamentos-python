from random import randint
from time import sleep

print('-- GERADOR DE CHAVES PARA EUROMILHÕES ---')
n_palpites = int(input('\nQuantas chaves quer que gere: '))

print(f'\nA gerar {n_palpites} palpites...\n')
sleep(1)

for c in range(1, n_palpites + 1):

    numeros = []
    estrelas = []

    while len(numeros) < 5:

        num = randint(1, 50)

        if num not in numeros:

            numeros.append(num)

    numeros.sort()

    while len(estrelas) < 2:

        est = randint(1, 12)

        if est not in estrelas:

            estrelas.append(est)

    estrelas.sort()

    print(f'Palpite {c}: ', end='')
    print(f'{numeros}'.replace('[', '').replace(']', ''), end='  * ')
    print(f'{estrelas}'.replace('[', '').replace(']', ''))
    sleep(0.3)

print('\nBoa sorte! Se sair 50% é para o desenvolvedor! :)')