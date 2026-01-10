pessoas = []
dados = dict()
qtd_pessoas = 0
soma_idades = 0
qtd_mulheres = 0

while True:

    dados['nome'] = input('Digite o nome: ').strip()

    while True:

        dados['sexo'] = input('Digite o sexo [m/f]: ').strip().lower()

        if dados['sexo'] != 'm' and dados['sexo'] != 'f':

            print('Por favor introduza um sexo válido!')

        else:

            break

    if dados['sexo'] == 'f':

        qtd_mulheres += 1

    dados['idade'] = int(input('Digite a idade: '))
    soma_idades += dados['idade']

    pessoas.append(dados.copy())
    dados.clear()
    qtd_pessoas += 1


    opcao = input('Digite STOP para terminar ENTER para continuar: ').strip().lower()

    if opcao == 'stop':

        break

media_idades = round(soma_idades / qtd_pessoas, 2)
qtd_homens_acima_media = 0

for dados in pessoas:
    if dados['sexo'] == 'm':
        if dados['idade'] > media_idades:
            qtd_homens_acima_media += 1

print()
print('--------------')
print(' Informações:')
print('--------------')
print()
print(f'Foram registadas {qtd_pessoas} pessoas.')
print(f'A média de idades é {media_idades} anos.')
print(f'Foram registadas {qtd_mulheres} mulheres.')
print(f'Foram registados {qtd_homens_acima_media} homens com idade acima da média.')