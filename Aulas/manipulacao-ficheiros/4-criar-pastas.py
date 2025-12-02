import os

# Cria uma pasta
# nome_pasta = 'ficheiros'
# os.mkdir(nome_pasta)

# Cria as pastas precisas
caminho = 'ficheiros'
os.makedirs(caminho, exist_ok=True)