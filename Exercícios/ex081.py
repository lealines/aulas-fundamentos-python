def calcular_imc(peso, altura):

    try:

        return peso / (altura * altura)

    except ZeroDivisionError:

        return 0


def ter_classificacao(imc):

    if imc < 18.5:

        return 'Abaixo do peso'

    elif 18.5 <= imc <= 24.9:

        return 'Peso normal'

    elif 25.0 <= imc <= 29.9:

        return 'Sobrepeso'

    elif 30.0 <= imc <= 34.9:

        return 'Obesidade grau 1'

    elif 35.0 <= imc <= 39.9:

        return 'Obesidade grau 2'

    else:

        return 'Obesidade grau 3 (obesidade mórbida)'


def main():

    print('------------------')
    print('Calculadora de IMC')
    print('------------------')

    try:

        altura_str = input('\nIntroduza a sua altura em metros (ex: 1.75): ').replace(',', '.')
        peso_str = input('\nIntroduza o seu peso em kg (ex: 70): ').replace(',', '.')

        altura = float(altura_str)
        peso = float(peso_str)

        if altura <= 0 or peso <= 0:

            print('\nErro: A altura e o peso devem ser maiores que zero.')

            return

        imc = calcular_imc(peso, altura)

        classificacao = ter_classificacao(imc)


        print(f'\nO seu IMC é {imc:.2f} - {classificacao}')

        caminho_ficheiro = 'resultado_imc.txt'

        with open(caminho_ficheiro, 'w', encoding='utf-8') as f:

            f.write(f'O seu IMC é {imc:.2f} - {classificacao}')

        print(f'\nResultado gravado em "{caminho_ficheiro}"')

    except ValueError:

        print('Erro: Por favor, introduza valores numéricos válidos.')


if __name__ == '__main__':
    main()