expressao = input('Digite uma expressão matemática: ')

if expressao.count('(') == expressao.count(')'):
    print('A expressão está correta.')

else:
    print('A expressão está incorreta.')