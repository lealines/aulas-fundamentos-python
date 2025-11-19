jogos = ('Gran Turismo 7 - Standard Edition PS5', '39,99 €',
         'The Last of Us: Parte I (Em Português)', '39,99 €',
         'EA Sports FC 26 PS5 - Oferta DLC', '69,99 €',
         'Uncharted: Coleção Legado dos Ladrões PS5', '19,99 €',
         'Final Fantasy VII Remake Intergrade PS5', '29,99 €',
         'Digimon Story: Time Stranger PS5', '64,99 €',
         'Sonic Superstars PS5', '24,99 €')

print('-' * 70)

print(f'{'TABELA DE PREÇOS DE JOGOS':^70}')

print('-' * 70)

print()

for indice in range(0, len(jogos)):

    if indice % 2 == 0:
        print(f'{jogos[indice]:.<63}', end='')
    else:
        print(f'{jogos[indice]}')

print()

print('-' * 70)