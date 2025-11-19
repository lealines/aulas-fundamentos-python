from time import sleep

print(' ~*º~*º [DESENHADOR DE FORMAS] ~*º~*º ')
sleep(0.5)
print()
print(' ~*º~*º UMA PRODUÇÃO DE ~*º~*º')
sleep(0.5)
print()
print(' ~*º~*º FRANCISCA ~*º~*º')
print(' ~*º~*º   INÊS    ~*º~*º')
print(' ~*º~*º  PEDRO    ~*º~*º')
sleep(0.5)
print()
opcao = 0

while True:
    c = 0
    print('[1] Escada à esquerda')
    print('[2] Escada à direita')
    print('[3] Pirâmide')
    print('[4] Cruz')
    print('[0] Sair')
    opcao = int(input('--> '))

    if opcao == 1:
        n = 5
        for c in range(1, n + 1):
            print("*" * c) # print multiplicação das estrelas pelo valor do contador
            sleep(0.3)
        print()

    elif opcao == 2:
        print()
        n = 5 # altura da escada invertida

        for c in range(1, n + 1):
            print(' ' * (n - c) + '*' * c) #multiplica a quantidade de espaços pela altura - 1 e a quantidade de estrelas pelo contador do for
            sleep(0.3)
        print()

    elif opcao == 3:

        altura = 5 # altura da pirâmide

        for c in range(0, altura + 1):

            for espaco in range(0, altura - c): # espaços para centrar conforme o numero de estrelas (altura - contador)
                print(' ', end='')

            for estrela in range(1, 2 * c): # estrelas (o dobro do contador)
                print('*', end='')
            sleep(0.3)
            print() # nova linha, print vazio
        print()

    elif opcao == 4:
        print()

        altura = 5  # altura do x

        for c in range(altura): # contador altura

            for z in range(altura): # contador largura

                if z == c or z == altura - c - 1: # se altura = largura ou altura - altura - 1 = largura
                    print('*', end='')

                else:
                    print(' ', end='')
            sleep(0.3)
            print() # nova linha, print vazio
        print()

    elif opcao == 0:

        print()
        print('A sair.', end='')
        sleep(0.3)
        print('.', end='')
        sleep(1)
        print('.')
        sleep(1)
        print('Obrigado!')
        break

    else:
        print('Opção inválida, tente novamente!')