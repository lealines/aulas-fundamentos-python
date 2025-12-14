def ler(txt):

    while True:

        valor = input(txt)

        if valor.isnumeric():
            return int(valor)

        else:
            print("\nDigite apenas números!")

n = ler('Digite um número: ')
print(f"O número introduzido foi {n}.")