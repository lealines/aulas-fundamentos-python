def soma(lista: list) -> int:
   soma1 = 0
   for numero in lista:
        soma1 += numero
   return soma1


notas = [10,20,30,40,50]
media = soma(notas) / len(notas)
print(media)












