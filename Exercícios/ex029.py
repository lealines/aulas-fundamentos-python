print('--- Calculadora ---')
print('[ 1 ] – Tabuada')
print('[ 2 ] – Calculadora')
print('[ 3 ] – Números Pares')
print('[ 4 ] – Sair')

print()
opcao = int(input('--> '))

if opcao == 1:
    print('Escolheu Tabuada')

    num = int(input('Digite um número: '))

    print(num, 'x 1 =', num * 1)
    print(num, 'x 2 =', num * 2)
    print(num, 'x 3 =', num * 3)
    print(num, 'x 4 =', num * 4)
    print(num, 'x 5 =', num * 5)
    print(num, 'x 6 =', num * 6)
    print(num, 'x 7 =', num * 7)
    print(num, 'x 8 =', num * 8)
    print(num, 'x 9 =', num * 9)
    print(num, 'x 10 =', num * 10) # também se pode fazer com f' = fstring


elif opcao == 2:
    print('Escolheu Calculadora')

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))
    operacao = input('[ + - * /]: ')

    if operacao == '+':
        print(f'{num1} + {num2} = {num1 + num2}')

    elif operacao == '-':
        print(f'{num1} - {num2} = {num1 - num2}')

    elif operacao == '*':
        print(f'{num1} * {num2} = {num1 * num2}')

    elif operacao == '/':

        if num2 == 0:
            print('Não é possível dividir por 0!')
        else:
            print(f'{num1} / {num2} = {num1 / num2:.0f}')


elif opcao == 3:
    print('Números Pares')

    numero = int(input('Digite um número para descobrir se é par ou ímpar: '))

    if numero % 2 == 0:
                print('Par!')

    else:
        print('Ímpar!')

elif opcao == 4:
    print('Saindo do programa...')

else:
    print('Opção inválida!')