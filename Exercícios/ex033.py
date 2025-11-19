soma = 0

for count in range(0, 5):
    numero = int(input(f'Digite o {count + 1}º número inteiro: '))
    soma += numero

print()
print(f'A soma dos 5 números inteiros é {soma}.')
