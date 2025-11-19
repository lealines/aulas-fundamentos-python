from time import sleep

numeros = []

print('Insira 5 números: ')
sleep(1)
print()

for c in range(0, 5):
    numero = input(f'{c + 1}ª --> ')
    numeros.append(numero)

maior = max(numeros)
menor = min(numeros)

posicao_maior = numeros.index(maior)
posicao_menor = numeros.index(menor)

sleep(1)
print()

print(f'O número maior é {maior} e está em {posicao_maior + 1}ª posição.')

sleep(1)
print()

print(f'O número menor é {menor} e está em {posicao_menor + 1}ª posição.')
