from time import sleep

sleep(0.5)

valor1 = int(input('Insira o 1º valor: '))
valor2 = int(input('Insira o 2º valor: '))
valor3 = int(input('Insira o 3º valor: '))
sleep(1)
print()

opcao = 0

while opcao != 5:
    print('--- MENU ---')
    print('[ 1 ] - SOMAR')
    print('[ 2 ] - MULTIPLICAR')
    print('[ 3 ] - MAIOR')
    print('[ 4 ] - NOVOS NÚMEROS')
    print('[ 5 ] - SAIR DO PROGRAMA')
    sleep(1)
    print()
    opcao = int(input('Escolha uma opção: '))

    if opcao == 1:
        print()
        print('--- SOMAR ---')
        sleep(1)
        print()
        soma = valor1 + valor2 + valor3
        print(f'{valor1} + {valor2} + {valor3} = {soma}')
        break

    elif opcao == 2:
        print()
        print('--- MULTIPLICAR ---')
        sleep(1)
        print()
        soma = valor1 * valor2 * valor3
        print(f'{valor1} x {valor2} x {valor3} = {soma}')
        break

    elif opcao == 3:
        print()
        print('--- MAIOR ---')

        if valor1 >= valor2 and valor1 >= valor3:
            print()
            sleep(1)
            print(f'O maior número introduzido é {valor1}.')
            break

        elif valor2 >= valor1 and valor2 >= valor3:
            print()
            sleep(1)
            print(f'O maior número introduzido é {valor2}.')
            break

        else:
            print()
            sleep(1)
            print(f'O maior número introduzido é {valor3}.')
            break



    elif opcao == 4:
        print()
        print('--- NOVOS NÚMEROS ---')
        print()
        sleep(1)
        valor1 = int(input('Insira o 1º valor: '))
        valor2 = int(input('Insira o 2º valor: '))
        valor3 = int(input('Insira o 3º valor: '))
        print()
        sleep(1)
        print('Novos valores registados!')
        print()
        sleep(1)


    elif opcao == 5:
        print()
        sleep(1)
        print('Saindo do programa...')

    else:
        print()
        sleep(1)
        print('Opção inválida, escolha uma das opções.')