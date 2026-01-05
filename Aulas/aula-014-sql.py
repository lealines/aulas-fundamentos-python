# Estabelecer a ligação
# 1 - Importar a biblioteca necessária

import sqlite3


# 2 - Iniciar a conexão

def conectar():
    try:
        return sqlite3.connect('tarefas.db')
    except Exception as e:
        print(f'Erro ao iniciar ligação à base de dados: {str(e)}')
        return ''

# Criar uma tabela

def criar_tabela():

    # Criar conexão

    conn = conectar()

    # Criar cursor

    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            descricao TEXT NOT NULL,
            estado TEXT NOT NULL
        )   
    ''')

    conn.commit()
    conn.close()

def cabecalho(txt):
    print(f'--- {txt} ---')

def adicionar_tarefa():

    cabecalho('ADICIONAR TAREFA')

    descricao_tarefa = input('Descrição: ').strip()
    estado_tarefa = ('Pendente')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('INSERT INTO tarefas (descricao, estado) VALUES (?, ?)', (descricao_tarefa, estado_tarefa))

    conn.commit()
    conn.close()

    print(f'Tarefa "{descricao_tarefa}" adicionada com sucesso.')

def ver_tarefas():
    cabecalho('MOSTRAR TAREFAS')

    conn = conectar()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tarefas')
    tarefas = cursor.fetchall()

    for tarefa in tarefas:
        print('--------------------------------------------------------------')
        print(f'ID: {tarefa[0]} | DESCRIÇÃO: {tarefa[1]} | ESTADO: {tarefa[2]}')

    input()

def terminar_tarefa():
    cabecalho('TERMINAR TAREFA')

    id_tarefa = input('Digite o ID da tarefa: ')

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute('UPDATE tarefas SET estado = ? WHERE id = ?', ('Concluido',
    int(id_tarefa)))

    print('Tarefa concluida')

def apagar_tarefa():
    pass

def menu():
    criar_tabela()
    while True:

        print('[ 1 ] - Adicionar Tarefa')
        print('[ 2 ] - Ver Tarefas')
        print('[ 3 ] - Concluir Tarefa')
        print('[ 4 ] - Apagar Tarefa')
        print('[ 5 ] - Sair')

        opcao = int(input('--> '))

        match opcao:
            case 1:
                adicionar_tarefa()
            case 2:
                ver_tarefas()
            case 3:
                terminar_tarefa()
            case 4:
                apagar_tarefa()
            case 5:
                break




if __name__ == __name__:
    menu()