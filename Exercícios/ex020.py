nome = input('Digite o seu nome completo:').strip()

print(nome.upper())
print(nome.lower())
print(len(nome.replace(' ', '')))

string = nome.split() # divide as palavras em grupos
print(len(string[0])) # conta o numero de letras no grupo indicado

# OU

pEspaco = nome.find(' ') # encontro o indice do primeiro espaco
print(nome[:pEspaco]) # imprimo a string do inicio até ao indice do primeiro espaco