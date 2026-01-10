import sqlite3

def conectar():

    try:

        return sqlite3.connect('loja.db')

    except Exception as e:

        print(f'Erro ao iniciar ligação à base de dados: {str(e)}')

        return ''

def update_preco():

    conn = conectar()
    cursor = conn.cursor()

    precos = [
        (59.99, 5),
        (139.99, 6),
        (479.99, 7)
    ]

    cursor.executemany('''
                    UPDATE produtos
                    SET preco = ?
                    WHERE id = ?
                ''', precos)


    conn.commit()
    conn.close()

if __name__ == '__main__':
    update_preco()
    conectar()