import sqlite3

# Conectar ao banco de dados / criar novo banco de dados
con = sqlite3.connect('bdados.db')

# Criar tabelas
# LIVROS
con.execute('''
    CREATE TABLE IF NOT EXISTS livros(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo TEXT NOT NULL,
        autor TEXT NOT NULL,
        editora TEXT NOT NULL,
        ano DATE NOT NULL)''')

# USUÁRIOS
con.execute('''
    CREATE TABLE IF NOT EXISTS usuarios(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT UNIQUE NOT NULL,
        telefone CHAR(11),
        cpf CHAR(11))''')

# EMPRÉSTIMOS
con.execute('''
    CREATE TABLE IF NOT EXISTS emprestimos(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        livro_id INTEGER,
        usuario_id INTEGER,
        data_emprestimo DATE,
        data_devolucao DATE,
        FOREIGN KEY (usuario_id) REFERENCES usuarios(id),
        FOREIGN KEY (livro_id) REFERENCES livros(id))''')

# Confirmar as alterações no banco de dados
con.commit()
con.close()
