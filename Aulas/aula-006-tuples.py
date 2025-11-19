# estante = input('Digite uma consola: '), input('Digite outra consola: ')

nomes = ('Nádia', 'Laura', 'Alexandra', 'Telmo', 'Victor',
        'Rafael', 'Daniel', 'Leticia', 'Roman', 'Pedro',
        'Francisca', 'Inês')

for c in range(0, len(nomes)):
    print(f'No índice {c} está o nome: {nomes[c]}')

# OU

contador = 0

for nome in nomes:
    print(f'No índice {contador} está o nome: {nomes[contador]}')
    contador += 1

# -----------------------------------------------------------------------------

nomes = ('Nádia', 'Laura', 'Alexandra', 'Telmo', 'Victor',
        'Rafael', 'Daniel', 'Leticia', 'Roman', 'Pedro',
        'Francisca', 'Inês')

tamanho_variavel = len(nomes)

for c in range(0, tamanho_variavel):
    print(f'{c} -> {nomes[c]}')

# OU

for nome in nomes:
    print(nome)

for indice, nome in enumerate(nomes):
    print(f'No índice {indice} o valor é {nome}.')