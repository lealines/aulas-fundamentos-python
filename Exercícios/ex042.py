import random
from time import sleep

numero_inteiro = random.randint(0, 10)
resp_utilizador = int(input('Tente adivinhar o número em que o CPU está a pensar!: '))
sleep(1)
print()

contagem_tentativas = 1

while numero_inteiro != resp_utilizador:
    contagem_tentativas += 1
    if numero_inteiro > resp_utilizador:
        print('Mais acima!')

    elif numero_inteiro < resp_utilizador:
        print('Mais abaixo!')

    resp_utilizador = int(input('Tente outra vez! '))
    sleep(1)
    print()

if resp_utilizador == numero_inteiro:
    print(f'Acertas-te! Com um total de {contagem_tentativas} tentativas!')