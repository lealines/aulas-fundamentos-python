# range(início, fim, passo)
from time import sleep

for count in range(0,5):
    print(count + 1)
    sleep(1)

#--------------------------------------

soma = 0

for count in range(0,5):
    nota = float(input(f'Digite a {count+1}ª nota: '))
    soma += nota # é o mesmo que soma = soma + nota

print(soma/5) # média

#-------------------------------------

for count in range(5,0,-1):
    print(count)

#-------------------------------------

numero = 7

for count in range(0,10):
    print(f'{numero} x {count + 1} = {numero *
    (count + 1)}')
    input()

