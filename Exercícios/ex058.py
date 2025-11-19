lista = []

for c in range(0, 5):
    numero = int(input(f'Digite o {c + 1}º valor: '))

    if c == 0:
        lista.append(numero)
        print('Primeiro valor inserido com sucesso.')
        continue

    if numero > lista[-1]:
        lista.append(numero)
        print('Valor inserido na última posição')
    else:
        indice = 0
        while indice < len(lista):
            if numero <= lista[indice]:
                lista.insert(indice, numero)
                print(f'Valor inserido na posição {indice + 1}.')
                break
            indice += 1

print(lista)