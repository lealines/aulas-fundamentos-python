from time import sleep


def contador(inicio, fim, passo):

    if passo == 0:

        passo = 1

    if passo < 0:

        passo = passo * -1

    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')

    if inicio < fim:

        for c in range(inicio, fim + 1, passo):

            print(f'{c} ', end='')
            sleep(0.3)
    else:

        for c in range(inicio, fim - 1, -passo):

            print(f'{c} ', end='')
            sleep(0.3)

    print('FIM!')
    print('-' * 30)

contador(1, 20, 2)

contador(10, 0, 1)

print('Contagem personalizada')
inicio1 = int(input('Início: '))
fim1 = int(input('Fim:    '))
passo1 = int(input('Passo:  '))
contador(inicio1, fim1, passo1)