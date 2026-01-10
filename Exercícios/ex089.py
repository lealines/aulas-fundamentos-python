import sqlite3

def cabecalho(txt: str) -> None:

    print(f'\n--- {txt} ---')

def conectar():

    try:

        return sqlite3.connect('loja.db')

    except Exception as e:

        print(f'Erro ao iniciar ligação à base de dados: {str(e)}')

        return ''

def adicionar_novoproduto():

    cabecalho('ADICIONAR NOVO PRODUTO')
    nome_produto = input('\nNome: ').strip()
    preco_produto = float(input('Preço: '))
    stock_produto = int(input('Stock: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO produtos (nome, preco, stock) VALUES (?, ?, ?)", (nome_produto, preco_produto, stock_produto))
    conn.commit()
    conn.close()
    input(f'\nProduto "{nome_produto}" adicionado com sucesso.')


def ver_produtos():

    cabecalho('VER PRODUTOS')
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM produtos")
    loja = cursor.fetchall()
    conn.close()

    for produto in loja:
        print('---------------------------------------------------------------')
        print(f'ID: {produto[0]} | DESCRIÇÃO: {produto[1]} | PREÇO: {produto[2]} | STOCK: {produto[3]} | ')

    input()


def alterar_produto():

    cabecalho('ALTERAR PRODUTO')
    id_produto = input('\nDigite o ID do produto: ')
    nome_produto1 = input('Digite o nome do novo produto: ')
    preco_produto1 = float(input('Digite o preço do produto: '))
    stock_produto1 = int(input('Digite o stock do novo produto: '))

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "UPDATE produtos SET nome = ?, preco = ?, stock = ? WHERE id = ?",
        (nome_produto1, preco_produto1, stock_produto1, int(id_produto))
    )

    conn.commit()
    conn.close()

    print('Alteração concluida.')


def menu():

    while True:

        cabecalho('---------------')
        cabecalho('MENU BASE DADOS')
        print('\n[ 1 ] - Adicionar Novo Produto')
        print('[ 2 ] - Ver Produtos')
        print('[ 3 ] - Alterar Produto')
        cabecalho('---------------')

        opcao = int(input('\n--> '))

        match opcao:

            case 1:

                adicionar_novoproduto()

            case 2:

                ver_produtos()


            case 3:

                alterar_produto()

            case _:

                print('Opção inválida...')

if __name__ == '__main__':
    menu()