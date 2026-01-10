def main():
    print('--- CALCULADORA DE DIVISÃO ---')

    while True:
        try:

            entrada1 = input('\nInsira o primeiro número: ')
            num1 = float(entrada1)


            entrada2 = input('\nInsira o segundo número: ')
            num2 = float(entrada2)


            resultado = num1 / num2


            print(f'\nO resultado de {num1} / {num2} é: {resultado}')

            break

        except ValueError:

            print('Erro: Entrada inválida. Por favor, insira um número válido (ex: 5, 10.5).')

        except ZeroDivisionError:

            print('Erro: Não é possível dividir por zero. O segundo número não pode ser 0.')

        except Exception as e:

            print(f'Ocorreu um erro inesperado: {e}')

        if input('\nDeseja tentar novamente? (s/n): ').lower() != 's':
            break


if __name__ == '__main__':
    main()