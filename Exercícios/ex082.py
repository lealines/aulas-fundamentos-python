def sistema_ajuda():
    print('=' * 40)
    print('--- SISTEMA DE AJUDA PYTHON ---')
    print('Digite o comando ou "SAIR" para sair')
    print('=' * 40)

    while True:

        comando = input('Comando >>> ').strip()

        if comando.upper() == 'SAIR':

            print('\nEncerrando o sistema de ajuda...')

            break
        else:

            print('\n' + '-' * 40)
            help(comando)
            print('-' * 40 + '\n')

sistema_ajuda()