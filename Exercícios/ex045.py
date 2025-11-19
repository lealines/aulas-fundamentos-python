#Sequência de Fibonacci
#0 1 1 2 3 5 8 13 21

print('~*º~*º Sequência de Fibonacci º*~º*~')

antecessor = 0 # atribuo o primeiro valor da sequencia
atual = 1 # atribuo o segundo valor da sequencia
sequencia = int(input('Digite um valor: ')) # peço ao utilizador quantos valores quer ver na sequencia

if sequencia < 1: # se a seq. a ser mostrada é inferior a 1, ele não mostra e diz inválido.
    print('Inválido.')

elif sequencia == 1: # se a sequencia for 1, ele mostra o primeiro valor da seq. de fibo
    print(antecessor)

elif sequencia == 2: # se a seq. for 2, ele mostra os 2 primeiros valores da seq. de fibo
    print(f'{antecessor} -> {atual}')

else:
    print(f'{antecessor} -> {atual}',end=' ')

    sequencia = sequencia - 2 # libertamos 2 valores da seq. pq na linha anterior 2 ja foram exibidos

    while sequencia >= 1: # enquanto a seq. for superior ou igual a 1, ele repete o abaixo
        sucessor = antecessor + atual # calc o valor seguinte aos dois primeiros

        print(f'-> {sucessor} ' , end='') # mostra esse valor calculado

        antecessor = atual # transfere os valores
        atual = sucessor # transfere os valores

        sequencia -= 1 # retira 1 à sequencia pois foi exibido mais um valor

    print()

# versão alternativa:

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

    # Exemplo: Gerar os 10 primeiros números da sequência

for i in range(10):
    print(fibonacci(i))


