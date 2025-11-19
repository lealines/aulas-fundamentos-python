nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))
nota5 = float(input('5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('Média =', media)

if media >=9.5:
    print('PASSOU!')

elif media >8:
    print('Em recuperação!')

else:
    print('REPROVOU!')

#OU

nota1 = float(input('1ª nota: '))
nota2 = float(input('2ª nota: '))
nota3 = float(input('3ª nota: '))
nota4 = float(input('4ª nota: '))
nota5 = float(input('5ª nota: '))

media = (nota1 + nota2 + nota3 + nota4 + nota5) / 5
print('Média =', media)

if media >=9.5:
    print('PASSOU!')

elif media <8:
    print('REPROVADO!')

else:
    print('Em recuperação!')