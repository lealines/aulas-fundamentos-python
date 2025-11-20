from random import randint
from time import sleep

print('-- GERADOR DE CHAVES PARA EUROMILHÕES ---')
sleep(0.5)

contador = 0
n_palpites = int(input('Quantas chaves quer que gere: '))

sleep(1)

print(f'A gerar {n_palpites} palpites...')

for c in range(n_palpites):

    print('Palpite')

    palpite = []
    numeros = []
    estrelas = []

    while len(numeros) < 5:

        numero = randint(1, 50)
        numeros.append(numero)

        if numero not in numeros:
            numeros.append(numero)


    while len(estrelas) < 2:

        estrela = randint(1, 12)

        if estrela not in estrelas:
            estrelas.append(estrela)

palpite.append(numeros[:])
palpite.append(estrelas[:])

for indice, linha in enumerate(palpite):
    if indice == 0:
        for numero in linha:
            print(f'{numero} | ', endl='')