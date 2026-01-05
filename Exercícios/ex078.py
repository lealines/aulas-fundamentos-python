def fatorial(n, mostrar=False):
    resultado = 1
    contas = ''

    for i in range(n, 0, -1):
        resultado *= i
        if mostrar:
            contas += f'{i} x ' if i > 1 else f'{i} = {resultado}'

    if mostrar:
        print(contas)
    else:
        print(f'{n}! = {resultado}')

    with open('fatorial.txt', 'w', encoding='utf-8', errors='ignore') as file:

        file.write(f'Fatorial de {n}: {resultado}\n')

        if mostrar:

            file.write('Cálculo: ' + contas)

    return resultado

num = int(input('Número para calcular o fatorial: '))
mostrar = input('Mostrar o cálculo? (s/n): ').lower()

mostrar_contas = (mostrar == 's')

fatorial(num, mostrar_contas)