frase = input('Digite uma frase:').strip()

print(frase.count('A'))
print(frase.find('A'))
print(frase.rfind('A'))
print()
# OU
print()
qtd_a = frase.count('A')
print(f'O A aparece {qtd_a} vezes.')

p_posicao = frase.find('A')
print(f'Aparece pela primeira vez na posição {p_posicao + 1}.')

u_posicao = frase.rfind('A')
print(f'Aparece pela última vez na posição {u_posicao + 1}.')