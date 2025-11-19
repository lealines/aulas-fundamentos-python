from time import sleep
import random

numero = random.randint(0, 7)
numero_utilizador = int(input('Digite um número de 1 a 7: '))

sleep(1)
print()
print(numero)

if numero == numero_utilizador:
    print('VENCEU!')

else:
    print('PERDEU!')