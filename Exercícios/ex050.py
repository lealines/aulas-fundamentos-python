maiores = 0
menores = 0
menores_masc = 0
mulheres = 0
homens = 0

resposta = ''

while True:
    idade = int(input('\nDigite a idade: '))

    while True:
        sexo = input('Digite o sexo [M/F]: ').strip().lower()

        if sexo != 'm' and sexo != 'f':
            print('Por favor, digite M ou F.')
        else:
            break

    if idade > 25:
        maiores += 1

    if sexo == 'm' and idade < 17:
        menores_masc += 1

    if sexo == 'f':
        mulheres += 1

    if idade < 18:
        menores += 1

    while True:
        resposta = input('Quer continuar a registar? [sim/nao]: ').strip().lower()
        if resposta in ('sim', 'nao'):
            break
        print('Resposta inválida. Por favor, digite "sim" ou "nao".')

    if resposta == 'nao':
        break

print(f'Pessoas com mais de 25 anos: {maiores}')
print(f'Pessoas com menos de 18 anos: {menores}')
print(f'Menores de 18 anos do sexo masculino (M<17): {menores_masc}')
print(f'Pessoas do sexo feminino registadas: {mulheres}')