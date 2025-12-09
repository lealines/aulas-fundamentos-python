try:

    num1 = int(input('Digite um número: '))
    num2 = int(input('Digite outro número: '))

    divisao = num1 / num2

except ZeroDivisionError:
    print('Não é possível dividir por 0.')

except ValueError:
    print('Per favor digite um número válido')

except KeyboardInterrupt:
    print('O utilizador encerrou o programa.')

else:
    print(f'{num1} / {num2} = {num1 / num2}')

finally:
    print('Programa encerrado!')