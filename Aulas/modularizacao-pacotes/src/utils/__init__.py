'''

Funções userfriendly

-> Menu
-> Cabeçalho
-> Sleeps
-> Pausa

'''

from time import sleep

def delay(time: int) -> None:
    sleep(time)

def pausa(txt: str) -> None:
    _ = input(txt)

def cabecalho(txt: str) -> None:
    print('-' * len(txt))
    print(txt)
    print('-' * len(txt))

def menu() -> None:
    from src.handlers import pesquisar_notas, mostar_notas, apagar_notas, adicionar_notas
    while True:

        cabecalho('MENU')
        print('\n[ 1 ] - Adicionar Notas')
        print('[ 2 ] - Mostrar Notas')
        print('[ 3 ] - Apagar Notas')
        print('[ 4 ] - Pesquisar Notas')
        print('[ 5 ] - Sair')

        opcao = int(input('\n---> '))

        match opcao:

            case 1:
                adicionar_notas()

            case 2:
                mostar_notas()

            case 3:
                apagar_notas()

            case 4:
                pesquisar_notas()

            case 5:
                break

        pausa('\nENTER para continuar')