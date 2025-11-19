resposta= ''

while resposta != 'V' and resposta != 'F':
    resposta = input('O céu é azul?\n[V / F]: ').strip().upper()

    if resposta == 'V':
         print('Acertou!')
         break

    elif resposta == 'F':
        print('Errou!')
        break

    else:
        print('Resposta inválida!')

while True:
    resposta = input('1 + 1 = 2?\n [V / F]: ').strip().upper()

    if resposta == 'F':
        print('Acertou!')
        break

    elif resposta == 'V':
        print('Errou!')
        break

    else:
        print('Resposta inválida!')

while True:
    resposta = input('O mar é amarelo?\n [V / F]: ').strip().upper()

    if resposta == 'F':
        print('Acertou!')
        break

    elif resposta == 'V':
        print('Errou!')
        break

    else:
        print('Resposta inválida!')