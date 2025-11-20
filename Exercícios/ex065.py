from random import randint

jogador1 = dict()
jogador2 = dict()
jogador3 = dict()
jogador4 = dict()
jogador5 = dict()

for c in range(0, 5):
    num = randint(0,6)
    jogador1['Dado'] = num
    jogador2['Dado'] = num
    jogador3['Dado'] = num
    jogador4['Dado'] = num
    jogador5['Dado'] = num

    print(jogador1)
    print(jogador2)
    print(jogador3)
    print(jogador4)
    print(jogador5)

