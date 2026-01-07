import sqlite3

def conectar():
    try:
        return sqlite3.connect('loja.db')
    except Exception as e:
        print(f'Erro ao iniciar ligação à base de dados: {str(e)}')
        return ''

def inserir_produtos():
    conn = conectar()
    cursor = conn.cursor()

    codigo_sql = '''
        INSERT INTO produtos (nome, preco, stock)
        VALUES (?, ?, ?)
        '''

    lista_produtos = [
        ('Teclado', 120.99, 10),
        ('Rato', 59.99, 25),
        ('Monitor', 899.99, 5),
        ('Auscultadores', 45.99, 20),
        ('Pen-Drive 128g', 49.99, 15),
        ('Mesa Gaming', 129.99, 60),
        ('Telemóvel', 499.99, 45),
        ('Carregador Telemóvel', 59.99, 10),
        ('Cadeira Gaming', 119.99, 25),
        ('PC', 599.99, 5)
    ]

    cursor.executemany(codigo_sql, lista_produtos)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    inserir_produtos()
    conectar()