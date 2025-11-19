from time import sleep

limite_velocidade = 80

print('--- RADAR DE VELOCIDADE ---')
print()
sleep(1)
velocidade = int(input('---> '))
print()


sleep(1)

if limite_velocidade < velocidade:
    km_acima = velocidade - limite_velocidade
    multa = 100 + 7 * (km_acima)
    print('Multado!')
    sleep(1)
    print(f'Ultrapassou o limite em {km_acima}km/h.')
    sleep(1)
    print(f'A sua multa é de {multa:.2f}€.')

else:
    print('Não multado! Boa Viagem!')