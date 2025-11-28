from random import randint


def calculo(nome, notas):
    soma = 0
    for c in range(len(notas)):
        soma += notas[c]
    media = soma /(len(notas))
    print(f"Aluno: {nome}, com notas: {notas}, e média {media} foi aprovado.") if (media > 9.5) else print(f"Aluno: {nome}, com notas: {notas}, foi reprovado.")






notas = list()
for c in range(0,5):
    notas.append(randint(0,20))
calculo(input("Digite o seu nome: "), notas)