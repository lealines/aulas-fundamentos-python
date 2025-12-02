from pathlib import Path # classe Path que dá métodos/funções típicas de ficheiro

# Informar qual é o caminho do ficheiro
# Criar a variável que representa o caminho do ficheiro
caminho = Path(r'ficheiros/teste.txt')

# O Python cria  ficheiro se ele não existir
# Podemos abrir o ficheiro em modo:
# Write - 'w'
# Read - 'r' (se o ficheiro não existir ele não abre em modo read)
# Append - 'a'

with caminho.open('w', encoding='utf-8', errors='ignore') as file:
    file.write('Olá turma!')
    file.write('Olá novamente!')