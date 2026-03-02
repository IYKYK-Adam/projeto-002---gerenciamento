import sqlite3

# conectar o banco de dados 
def connect():
    return sqlite3.connect('bdados.db')

# inserir livro
def novo_livro_bd(titulo, autor, editora, ano):
    conn = connect()
    cursor = conn.cursor()  # cursor para manipular os dados
    
    cursor.execute('''
        INSERT INTO livros (titulo, autor, editora, ano) 
        VALUES (?, ?, ?, ?)''', (titulo, autor, editora, ano))
    conn.commit()
    print(f'Livro "{titulo}" cadastrado com sucesso!')

    conn.close()

# Inserir novo usuário
def novo_usuario_bd(nome, email, telefone, cpf):
    conn = connect()
    cursor = conn.cursor()
    
    # verificar se o usuário já existe
    cursor.execute('SELECT * FROM usuarios WHERE cpf=?', (cpf,))
    if cursor.fetchone():
        print('Já existe um usuário com esse CPF cadastrado.')
    else:
        try:
            cursor.execute('''
                INSERT INTO usuarios (nome, email, telefone, cpf)
                VALUES (?, ?, ?, ?)''', (nome, email, telefone, cpf))
            conn.commit()
            print(f'Usuário "{nome}" cadastrado com sucesso!')
        except sqlite3.Error as e:
            print(f'Já existe um usuário com esse CPF cadastrado.')
    
    conn.close()

#exibir livros
def exibir_livros_bd():
    conn = connect()
    cursor = conn.cursor()

    livros = cursor.execute('SELECT * FROM livros').fetchall()
    conn.close()
    return livros


#exibir usuarios
def exibir_usuarios_bd():
    conn = connect() 
    cursor = conn.cursor()  
    
    usuarios = cursor.execute("SELECT * FROM usuarios").fetchall() 
    conn.close() 
    return usuarios 



#realizar emprestimos
def realizar_emprestimo_bd(livro_id, usuario_id, data_emprestimo, data_devolucao=None):
    conn = connect()
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO emprestimos (livro_id, usuario_id, data_emprestimo, data_devolucao)
        VALUES (?, ?, ?, ?)
    ''', (livro_id, usuario_id, data_emprestimo, data_devolucao))  # None vira NULL
    
    conn.commit()
    conn.close()


#exibir emprestimo
def exibir_emprestimos_bd():
    conn = connect()
    cursor = conn.cursor()

    result = cursor.execute('''
        SELECT 
            emprestimos.id, 
            livros.titulo, 
            COALESCE(usuarios.nome, 'N/A') AS nome_usuario, 
            emprestimos.data_emprestimo,
            emprestimos.data_devolucao
        FROM emprestimos
        LEFT JOIN livros ON livros.id = emprestimos.livro_id
        LEFT JOIN usuarios ON usuarios.id = emprestimos.usuario_id
        WHERE emprestimos.data_devolucao IS NULL
    ''').fetchall()

    conn.close()
    return result


# Atualizar a data de devolução
def atualizar_devolucao_bd(id_emprestimo, data_devolucao):
    conn = connect()
    cursor = conn.cursor()

    cursor.execute('''
        UPDATE emprestimos SET data_devolucao = ? WHERE id = ?''', (data_devolucao, id_emprestimo))

    conn.commit()
    conn.close()


# exemplo
# novo_livro("Steven Universo: End of an Era", "Rebecca Sugar", "Harry N. Abrams", "2020-10-13")
# novo_usuario("Adam", "victoradamsantosgomes@gmail.com", "75998176909", "09966672577")
# realizar_emprestimo(1,1,'2025-03-30',None)
# atualizar_devolucao(3, '2025-04-10') - Agora não mostrará o empréstimo devolvido





