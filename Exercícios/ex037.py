numero = int(input('Digite um número: '))

contador = 0

for count in range(0, numero):

    if numero % (count + 1) == 0:
        contador += 1

if contador == 2:
    print(f'O número {numero} é primo.')

else:
    print(f'O número {numero} não é primo.')