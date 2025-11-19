from random import randint

numeros = (randint(1, 20),
            randint(1, 20),
            randint(1, 20),
            randint(1, 20),
            randint(1, 20))

maior = menor = numeros[0]

for c in numeros:

    if c > maior:
        maior = c

    if c < menor:
        menor = c

for numero in numeros:
    print(f'\t{numero}', end='')

print(f'\nO maior número é {maior}.')

print(f'O menor número é {menor}.')