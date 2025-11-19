total_numeros = 0
soma_numeros = 0

print("--- Insira Números e some-os ---")

while True:

    numero_str = input("Digite um número inteiro: ")
    numero = int(numero_str)

    soma_numeros = soma_numeros + numero
    total_numeros = total_numeros + 1

    continuar = input("Deseja inserir mais um número? Digite [S] para Sim ou outra tecla para Parar: ")

    if continuar not in 'Ss':
        break

print("Programa finalizado! Resultados: ")
print(f"O utilizador inseriu um total de {total_numeros} números.")
print(f"A soma entre todos os números inseridos é: {soma_numeros}")
