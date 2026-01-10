def encontrar_maior(*numeros):

    if not numeros:

        return 'Nenhum valor inserido.'

    maior = numeros[0]

    for n in numeros:

        if n > maior:
            maior = n

    return maior

lista_final = []

print('--- ANALISAR NÚMEROS ---')

quantidade = int(input('Quantos números deseja analisar? '))

for i in range(quantidade):

    num = int(input(f'Digite o {i + 1}º número: '))
    lista_final.append(num)

if lista_final:

    resultado = encontrar_maior(*lista_final)

    print('\n--------------------------')
    print(f'\nNúmeros analisados: {lista_final}')
    print(f'O maior valor é: {resultado}')

else:

    print('Lista vazia.')