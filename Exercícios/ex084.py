def calculadora():
    try:
        a = float(input('Digite o primeiro número: '))
        b = float(input('\nDigite o segundo número: '))

        print('''
[1] - Soma
[2] - Subtração
[3] - Multiplicação
[4] - Divisão
        ''')

        opcao = int(input('Escolha a operação: '))

        if opcao == 1:
            print(f'Resultado: {a + b}')
        elif opcao == 2:
            print(f'Resultado: {a - b}')
        elif opcao == 3:
            print(f'Resultado: {a * b}')
        elif opcao == 4:
            print(f'Resultado: {a / b}')
        else:
            print('\nOpção inválida.')

    except ValueError:
        print('\nErro: Digite apenas números.')
    except ZeroDivisionError:
        print('\nErro: Divisão por zero não é permitida.')


def tabuada():
    try:
        n = int(input('\nDigite um número: '))
        for i in range(1, 11):
            print(f'{n} x {i} = {n * i}')
    except ValueError:
        print('\nErro: Digite um número inteiro.')


def par_ou_impar():
    try:
        n = int(input('\nDigite um número: '))
        if n % 2 == 0:
            print('\nO número é PAR.')
        else:
            print('\nO número é ÍMPAR.')
    except ValueError:
        print('\nErro: Digite um número inteiro.')


def numeros_primos():
    try:
        n = int(input('\nDigite um número: '))
        if n <= 1:
            print('\nNão é um número primo.')
            return

        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                print('\nNão é um número primo.')
                return

        print('\nÉ um número primo.')
    except ValueError:
        print('\nErro: Digite um número inteiro.')


def fatorial():
    try:
        n = int(input('\nDigite um número: '))
        if n < 0:
            print('\nErro: Não existe fatorial de número negativo.')
            return

        resultado = 1

        for i in range(1, n + 1):
            resultado *= i

        print(f'\nFatorial de {n} é {resultado}')

    except ValueError:

        print('\nErro: Digite um número inteiro.')


def menu():

    while True:

        print('''
================ MENU =================
[1] - Calculadora
[2] - Tabuada
[3] - Par ou Ímpar
[4] - Número Primo
[5] - Fatorial
[0] - Sair
======================================
        ''')

        try:

            opcao = int(input('Escolha uma opção: '))

            if opcao == 1:
                calculadora()
            elif opcao == 2:
                tabuada()
            elif opcao == 3:
                par_ou_impar()
            elif opcao == 4:
                numeros_primos()
            elif opcao == 5:
                fatorial()
            elif opcao == 0:
                print('\nEncerrando o programa...')
                break
            else:

                print('\nOpção inválida. Tente novamente.')

        except ValueError:

            print('\nErro: Digite apenas números.')


if __name__ == '__main__':
    menu()