contador_pares = 0
total_numeros = 10

for count in range(total_numeros):
    numero = int(input(f'Digite o {count + 1}º número inteiro: '))

    if numero % 2 == 0:
        contador_pares += 1

print(f"Dos {total_numeros} números digitados, {contador_pares} são pares.")