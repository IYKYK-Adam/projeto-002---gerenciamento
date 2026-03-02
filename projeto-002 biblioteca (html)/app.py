from flask import Flask, render_template, request, redirect, url_for
from view import *

app = Flask(__name__)

# Rota principal
@app.route('/')
def index():
    return render_template('index.html')

# Cadastrar novo livro
@app.route('/cadastrar_livro', methods=['GET', 'POST'])
def cadastrar_livro():
    if request.method == 'POST':
        titulo = request.form['titulo']
        autor = request.form['autor']
        editora = request.form['editora']
        data_publicacao = request.form['data_publicacao']

        novo_livro_bd(titulo, autor, editora, data_publicacao)
        return redirect(url_for('exibir_livros'))

    return render_template('cadastrar_livro.html')

# Exibir livros
@app.route('/livros')
def exibir_livros():
    livros = exibir_livros_bd()
    return render_template('livros.html', livros=livros)

# Cadastrar novo usuário
@app.route('/novo_usuario', methods=['GET', 'POST'])
def novo_usuario():
    if request.method == 'POST':
        nome = request.form['nome']
        cpf = request.form['cpf']
        telefone = request.form['telefone']
        email = request.form['email']

        novo_usuario_bd(nome, email, telefone, cpf)

    return render_template('novo_usuario.html')

# Listar usuários
@app.route('/listar_usuarios')
def listar_usuarios():
    usuarios = exibir_usuarios_bd()
    return render_template('listar_usuarios.html', usuarios=usuarios)

# Empréstimo
@app.route('/emprestimo', methods=['GET', 'POST'])
def realizar_emprestimo():
    if request.method == 'POST':
        usuario_id = request.form['usuario']
        livro_id = request.form['livro']
        data_emprestimo = request.form['data_emprestimo']
        data_devolucao = None  # Considerando que ainda não foi devolvido

        realizar_emprestimo_bd(livro_id, usuario_id, data_emprestimo, data_devolucao)

    return render_template('emprestimo.html')

# Devolução
@app.route('/devolucao', methods=['GET', 'POST'])
def devolucao():
    if request.method == 'POST':
        id_emprestimo = request.form['emprestimo']
        data_devolucao = request.form['data_devolucao']

        atualizar_devolucao_bd(id_emprestimo, data_devolucao)

    return render_template('devolucao.html')

# Livros emprestados no momento
@app.route('/livros_emprestados')
def livros_emprestados():
    emprestimos = exibir_emprestimos_bd()
    return render_template('livros_emprestados.html', emprestimos=emprestimos)

if __name__ == '__main__':
    app.run(debug=True)
