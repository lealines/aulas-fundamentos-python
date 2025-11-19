numeros = list()
soma_valores_pares = 0
soma_segunda_coluna = 0
maior_terceira_linha = 0

for linha in range(0, 3):
    temp = list()

    for coluna in range(0, 3):
        num = int(input('Digite um número: '))

        if num % 2 == 0:
            soma_valores_pares += num

        if coluna == 1:
            soma_segunda_coluna += num

        if linha == 2:

            if coluna == 0:
                maior_terceira_linha == num

            else:

                if num > maior_terceira_linha:
                    maior_terceira_linha = num


        temp.append(num)

    numeros.append(temp[:])
print()

for lista in numeros:

    for valor in lista:
        print(valor, end=' ')
    print()
print()
print(f'Soma valores pares: {soma_valores_pares}')
print(f'Soma segunda coluna: {soma_segunda_coluna}')
print(f'Maior terceira linha: {maior_terceira_linha}')