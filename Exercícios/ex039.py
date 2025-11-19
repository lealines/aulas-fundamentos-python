from datetime import datetime

qtd_maiores = 0
qtd_menores = 0

ano_atual = datetime.now().year


for count in range(0,7):
    ano_nascimento = int(input('Idade: '))
    idade = ano_atual - ano_nascimento

    if idade >= 18:
        qtd_maiores += 1

    else:
        qtd_menores += 1

print(f'Há {qtd_maiores} maiores de idade.')
print(f'Há {qtd_menores} menores de idade.')
