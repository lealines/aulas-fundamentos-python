from time import sleep # serve para utilizar o sleep, ou seja, retardar o aparecimento das strings

print('--- REGISTO DE UTILIZADOR ---')
print()
nome = input('Digite o seu primeiro e último nome: ').strip().lower()
print()
sleep(1)

print(f'Olá {nome.title()}, o seu registo está completo.') # title serve para pôr as primeiras letras em maiúsculas
print()
sleep(0.5)
print('A gerar o seu email...')
sleep(1)

p_nome = nome[0] # para receber a primeira letra da string nome
indice_espaco = nome.find(' ') + 1 # procura o primeiro espaço mais 1, mais 1 serve para começar a seguir ao espaço
u_nome = nome[indice_espaco:] # ultimo nome recebe o nome a partir do espaço até ao fim
print()
email = f'{p_nome}.{u_nome}@empresa.pt'

print(f'O seu email é {email}')

