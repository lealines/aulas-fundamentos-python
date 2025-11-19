maior_idade = menor_idade = 0

for count in range(0,10):
    idade = int(input('Digite sua idade: '))

    if count == 0:
        maior_idade = idade
        menor_idade = idade

    else:
        if idade > maior_idade:
            maior_idade = idade

        if idade < menor_idade:
            menor_idade = idade

print(f'Maior de idade inserida: {maior_idade}')
print(f'Menor de idade inserida: {menor_idade}')