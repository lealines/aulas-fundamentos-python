print('---Número Fatorial---')

num = int(input('Digite um número: '))


fatorial = 1

while num >= 1:

    if num==1:
        print(num, end=' = ')
    else:
        print(num, end=' x ')

    fatorial *= num

    num -= 1

print(fatorial)