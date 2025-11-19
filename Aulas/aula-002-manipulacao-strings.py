string = 'Python é Poderoso'

# Fatiamento de String / String Slicer

print(string[7]) # é
print(string[-1]) # último caracter
print(string[:6]) # Python
print(string[9:]) # Poderoso
print(string[::3]) # do início ao fim de 3 em 3
print(string[::-1]) # mostra a string ao contrário

# Análise de String / String Analisys

print(len(string)) # tamanho da String
print(string.count('o')) # quantas vezes aparece o 'o'
print('Python' in string) # devolve true ou false
print(string.find('é')) # devolve a posição do solicitado
print(string.find('Olé')) # não encontra e devolve -1
print(string.startswith('Python')) # devolve true ou false
print(string.endswith('Fraquinho')) # devolde true ou false


# Transformação de String / String Transfiguration

string = input('Digite uma frase:')

print(len(string)) # tamanho da string
print(len(string.strip())) # elimina os espaços em excesso para a direita e esquerda
print(len(string.rstrip())) # elimina os espaços em excesso para a direita
print(len(string.lstrip())) # elimina os espaços em excesso para a esquerda
print(string.lower()) # coloca a frase toda em minusculas
print(string.upper()) # coloca a frase toda em maiusculas
print(len(string.replace(' ', '')))