frase = input('Digite uma frase: ').replace(' ', '').lower()

frase_reverse = ''

tam = len(frase)

for count in range(tam,0,-1):
    frase_reverse += frase[count-1]

if frase_reverse == frase:
    print('É um palíndromo!')

else:
    print('Não é um palíndromo!')