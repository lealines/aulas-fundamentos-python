from time import sleep

custo_dia = 60
custo_km = 0.456

print('--- RENTACAR ---')

km_percorridos = float(input('Digite o número de kms percorridos: \n--> '))
qtd_dias = int(input('Digite quantos dias teve o carro: \n--> '))

total = custo_dia * qtd_dias + custo_km * km_percorridos

sleep(1)
print('A calcular custos', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.', end='')
sleep(1)
print('.')
sleep(1)

print('Total a pagar:', float(total), '€' )