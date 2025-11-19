equipas = ('Real Madrid', 'Barcelona', 'Villarreal', 'Betis', 'Atlético Madrid',
           'Sevilla', 'Elche', 'Atlético Bilbao', 'Espanyol', 'Alavés', 'Getafe',
           'Osasuna', 'Levante', 'Rayo Vallecano', 'Valencia', 'Celta de Vigo',
           'Oviedo', 'Girona', 'Real sociedad', 'Mallorca')

print('5 Primeiros Classificados: ')
for indice, equipa in enumerate(equipas):
    if indice == 5:
        break
    else:
        print(f'\t{indice + 1}º - {equipa}')

print()
print('-------------------------')
print()

TAM = len(equipas)
print('4 últimos Classificados: ')
for indice, equipa in enumerate(equipas):
    if indice >= TAM -4:
        print(f'\t{indice + 1}º - {equipa}')
    else:
        continue

print()
print('-------------------------')
print()

print('Equipas por ordem alfbéfica:')
for equipa in sorted(equipas):
    print('\t', equipa)

print()
print('-------------------------')
print()

print('Posição da equipa Las Palmas:')

esta_la = False
indice_las_palmas = ''

for indice, equipa in enumerate(equipas):
    if equipa == 'Las Palmas':
        esta_la = True
        indice_las_palmas = indice

if esta_la == True:
    print(f'Las Palmas -> {indice_las_palmas + 1}º lugar')
else:
    print('Las Palmas não está classificado.')
