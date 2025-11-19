from time import sleep

sleep(1)
print('--- Calculadora IMC ---')
sleep(1)
print()

peso = int(input('Digite o seu peso (kg): '))
altura_cm = int(input('Digite a sua altura (cm): '))

sleep(1)
print()
print('A calcular o seu IMC', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)
print()

altura = altura_cm / 100
imc = peso / (altura * altura)
print(f'O seu IMC é de {imc:.1f}kg/m2.')

if imc <18.5:
    print('Abaixo do peso!')

elif 18.5 <= imc <= 24.9:
    print('Peso normal!')

elif 25.0 <= imc <= 29.9:
    print('Sobrepeso!')

elif 30.0 <= imc <= 34.9:
    print('Obesidade grau 1!')

elif 35.0 <= imc <= 39.9:
    print('Obesidade grau 2!')

else:
    print('Obesidade grau 3 (obesidade mórbida)!')