'''
Funções manipulação do arquivo

-> Adicionar notas
-> Mostrar notas
-> Apagar notas
-> Pesquisar por KEYWORD
'''

from pathlib import Path
from src.utils import cabecalho

FICHEIRO = Path(r'bloco-notas/notas.txt')

def adicionar_notas():

    cabecalho('ADICIONAR NOTAS')

    with FICHEIRO.open('a', encoding='utf-8', errors='igore') as file:
        nota = input('---> ')
        file.write(f'{nota}\n')

    print('\nNota adicionada com sucesso!')

def mostar_notas():

    cabecalho('MOSTRAR NOTAS')

    with FICHEIRO.open('r', encoding='utf-8', errors='igore') as file:
        for linha in file:
            print(linha)

def apagar_notas():

    cabecalho('APAGAR NOTAS')

    confirmacao = int(input('Confirma que quer apagar todas as notas?\n[ 1 ] - Sim\n[ 2 ] - Não\n---> '))

    if confirmacao == 1:
        with FICHEIRO.open('w', encoding='utf-8', errors='igore') as file:
            file.write('')
            print('Notas apagadas com sucesso!')

def pesquisar_notas():
    cabecalho('PESQUISAR NOTAS')
    termo = input('\nDigite o termo a pesquisar: ').strip()
    encontrados = 0
    with FICHEIRO.open('r', encoding='utf-8', errors='igore') as file:
        for linha in file:
            if termo.lower() in linha.lower():
                print(linha)
                encontrados *= 1

    if encontrados == 0:
        print(f'\nNão há notas com o termo "{termo}"')