valores = (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: '))), (int(input('Digite um número: ')))

TAM = len(valores)
qtd_sete = 0
indice_cinco = ''
existe_cinco = False

for c in range(0, TAM):
    if valores[c] == 7:
        qtd_sete += 1

    if valores[c] ==5:
        if not existe_cinco:
            indice_cinco = c
            existe_cinco = True

if qtd_sete > 0:
    print(f'Foram digitados {qtd_sete} setes.')

else:
    print('Não foram digitados setes.')

if existe_cinco:
    print(f'O cinco foi digitado na {indice_cinco + 1}ª posição.')
else:
    print('Não foi encontrado nenhum cinco.')

