from datetime import date

pessoa = dict()
ano = date.today().year

print()
print('--- CRÉDITO À HABITAÇÃO ---')
print()

pessoa['Nome'] = input('Digite o seu nome: ')
pessoa['Ano_Nascimento'] = int(input('Digite o seu ano de nascimento: '))
pessoa['Rendimentos'] = float(input('Digite os seus rendimentos mensais: '))
pessoa['Despesas'] = float(input('Digite as suas despesas mensais: '))
pessoa['Montante_Crédito'] = int(input('Digite o montante do crédito: '))
pessoa['Prazo_Anos'] = int(input('Em quantos anos deseja pagar: '))

pessoa['Idade'] = ano - pessoa['Ano_Nascimento']
pessoa['Remanescente'] = pessoa['Rendimentos'] - pessoa['Despesas']
pessoa['Crédito'] = pessoa['Montante_Crédito'] / (pessoa['Prazo_Anos'] * 12)

if pessoa['Remanescente'] > pessoa['Crédito']:
    print()
    print(f'Crédito APROVADO! O valor mensal será {pessoa['Crédito']:.2f} durante {pessoa['Prazo_Anos']} anos')

else:
    print()
    print(f'Crédito REPROVADO!')
