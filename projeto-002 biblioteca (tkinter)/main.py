from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

from tkinter import messagebox

#data
from datetime import date
from datetime import datetime

hoje = datetime.today().date()

#importando as funcões de 'view'
from view import *

# Paleta de cores --------------
cor0 = '#0D0D0D'  # preto
cor00 = '#090C02'  # preto esfumado
cor1 = '#feffff'  # branco

cor2 = '#731810'  # marrom-avermelhado escuro
cor3 = '#A64732'  # marrom-avermelhado claro
cor4 = '#F2B366'  # amarelo
cor5 = '#FDF3CC'  # amarelo claro
cor6 = '#49416D'  # violeta fraco



# Janelas
janela = Tk()
janela.title("Biblioteca de Kwangya")  
janela.geometry('770x330')
janela.configure(background=cor1)
janela.resizable(width=False, height=False)  # manter o padrão do Python

style = ttk.Style(janela)  
style.theme_use("clam")



#icon
janela.iconbitmap("img/favicon.ico")




#frames/divisões
parteCima = Frame(janela, width=770, height=50, bg=cor5, relief='flat')
parteCima.grid(row=0, column=0, columnspan=2, sticky=NSEW)

parteMenu = Frame(janela, width=200, height=265, bg=cor4, relief='solid')
parteMenu.grid(row=1, column=0, sticky=NSEW)

parteDireita = Frame(janela, width=600, height=265, bg=cor1, relief='raised')
parteDireita.grid(row=1, column=1, sticky=NSEW)




#titulo
abrir_img = Image.open('img/logo2.png')
abrir_img = abrir_img.resize((40,40))
abrir_img = ImageTk.PhotoImage(abrir_img)

img_titulo = Label(
    parteCima, image=abrir_img, 
    width=1000, 
    compound=LEFT, 
    padx=5, 
    anchor=NW, 
    bg=cor5
) 
img_titulo.image = abrir_img  
img_titulo.place(x=5, y=0)

texto_titulo = Label(
    parteCima,
    text='Sistema de Gerenciamento de Livros',
    compound=LEFT,
    padx=5,
    anchor=NW,
    font=('Times New Roman', 16, 'bold'),
    bg=cor5,
    fg=cor2
)   
texto_titulo.place(x=50, y=7)

linha_titulo = Label(
    parteCima, 
    width=770, 
    height=1, 
    padx=5, 
    anchor=NW, 
    font=('Times New Roman', 1), 
    bg=cor2, 
    fg=cor2
)
linha_titulo.place(x=0, y=47)





#funcao novo usuario
def novo_usuario():

    global salvar_img

    def add():
        nome = e_nome.get()
        email = e_email.get()
        telefone = e_telefone.get()
        cpf = e_cpf.get()

        lista = [nome, email, telefone, cpf]

        #verificar campos vazios
        for i in lista:
            if i =="":
                messagebox.showerror('Error 000:', 'Preencha todos os campos')
                return

        #enviar dados pro banco de dados
        novo_usuario_bd(nome, email, telefone, cpf)

        messagebox.showinfo('LETS GOUR', 'Usuário cadastrado com sucesso!')

        #limpando os campos de entrada dps q valores forem inseridos
        e_nome.delete(0,END)
        e_email.delete(0,END)
        e_telefone.delete(0,END)
        e_cpf.delete(0,END)

    titulo_novo_usuario = Label(
        parteDireita, 
        text='CADASTRE UM NOVO USUÁRIO',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_novo_usuario.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )

    #nome
    l_nome = Label(
        parteDireita, 
        text='Nome completo:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    
    l_nome.grid(
        row=2, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_nome = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    
    e_nome.grid(
        row=2, column=1, padx=5, pady=5, sticky=NSEW
    )

    # email
    l_email = Label(
        parteDireita, 
        text='E-mail:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_email.grid(
        row=3, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_email = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_email.grid(
        row=3, column=1, padx=5, pady=5, sticky=NSEW
    )

    # telefone
    l_telefone = Label(
        parteDireita, 
        text='Telefone:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_telefone.grid(
        row=4, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_telefone = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_telefone.grid(
        row=4, column=1, padx=5, pady=5, sticky=NSEW
    )

    # CPF
    l_cpf = Label(
        parteDireita, 
        text='CPF:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_cpf.grid(
        row=5, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_cpf = Entry(
        parteDireita, width=25, justify='left', relief='solid'
    )
    e_cpf.grid(
        row=5, column=1, padx=5, pady=5, sticky=NSEW
    )

    #salvar
    salvar_img = Image.open('img/salvar.jpg')
    salvar_img = salvar_img.resize((18,18))
    salvar_img = ImageTk.PhotoImage(salvar_img)

    b_salvar = Button(
        parteDireita,
        command=add,
        image=salvar_img,
        width=150,  
        height=15,  
        compound=LEFT,  
        text='salvar',  
        bg=cor3,
        fg=cor1,
        font=('Arial', 11, 'bold'),
        overrelief=RIDGE,
        relief=GROOVE,
        padx=5,  
        pady=5
    )

    b_salvar.grid(
        row=6, column=0, columnspan=2, pady=10 
    )


#funcao novo livro
def novo_livro():

    global salvar_img

    def add():
        titulo = e_titulo.get()
        autor = e_autor.get()
        editora = e_editora.get()
        ano = e_ano.get()

        lista = [titulo, autor, editora, ano]

        #verificar campos vazios
        for i in lista:
            if i =="":
                messagebox.showerror('Error 000:', 'Preencha todos os campos')
                return

        #enviar dados pro banco de dados
        novo_livro_bd(titulo, autor, editora, ano)

        messagebox.showinfo('LETS GOUR', 'Livro cadastrado com sucesso!')

        #limpando os campos de entrada dps q valores forem inseridos
        e_titulo.delete(0,END)
        e_autor.delete(0,END)
        e_editora.delete(0,END)
        e_ano.delete(0,END)

    titulo_novo_livro = Label(
        parteDireita, 
        text='CADASTRE UM NOVO LIVRO',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_novo_livro.grid(
        row=0, column=0, columnspan=3, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=3, sticky=NSEW
    )

    #titulo do livro
    l_titulo = Label(
        parteDireita, 
        text='Título do livro:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    
    l_titulo.grid(
        row=2, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_titulo = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    
    e_titulo.grid(
        row=2, column=1, padx=5, pady=5, sticky=NSEW
    )

    # autor
    l_autor = Label(
        parteDireita, 
        text='Autor(a):',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_autor.grid(
        row=3, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_autor = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_autor.grid(
        row=3, column=1, padx=5, pady=5, sticky=NSEW
    )

    # editora
    l_editora = Label(
        parteDireita, 
        text='Editora:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_editora.grid(
        row=4, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_editora = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_editora.grid(
        row=4, column=1, padx=5, pady=5, sticky=NSEW
    )

    # ano
    l_ano = Label(
        parteDireita, 
        text='Data de publicação:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_ano.grid(
        row=5, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_ano = Entry(
        parteDireita, width=25, justify='left', relief='solid'
    )
    e_ano.grid(
        row=5, column=1, padx=5, pady=5, sticky=NSEW
    )

    #salvar
    salvar_img = Image.open('img/salvar.jpg')
    salvar_img = salvar_img.resize((18,18))
    salvar_img = ImageTk.PhotoImage(salvar_img)

    b_salvar = Button(
        parteDireita,
        command=add,
        image=salvar_img,
        width=150,  
        height=15,  
        compound=LEFT,  
        text='salvar',  
        bg=cor3,
        fg=cor1,
        font=('Arial', 11, 'bold'),
        overrelief=RIDGE,
        relief=GROOVE,
        padx=5,  
        pady=5
    )

    b_salvar.grid(
        row=6, column=0, columnspan=2, pady=10 
    )


#funcao exibir usiarios
def exibir_usuarios():

    titulo_exibir_usuarios = Label(
        parteDireita, 
        text='EXIBIR USUARIOS CADASTRADOS',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_exibir_usuarios.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )

    dados = exibir_usuarios_bd()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Nome','Email','Telefone','CPF']
    
    global tree

    tree = ttk.Treeview(parteDireita, selectmode="extended",
                        columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parteDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parteDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parteDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw"]
    h=[20,150,178,75,75,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


#funcao exibir livro
def exibir_livros():

    titulo_exibir_livros = Label(
        parteDireita, 
        text='EXIBIR LIVROS CADASTRADOS',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_exibir_livros.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )

    dados = exibir_livros_bd()

    #creating a treeview with dual scrollbars
    list_header = ['ID','Título','Autor(a)','Editora','Data de publicação']
    
    global tree

    tree = ttk.Treeview(parteDireita, selectmode="extended", columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parteDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parteDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parteDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw"]
    h=[20,169,96,100,111,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


#funcao emprestimo
def realizar_emprestimo():

    global salvar_img

    def add():
        id_usuario = e_id_usuario.get()
        id_livro = e_id_livro.get()

        lista = [id_usuario, id_livro]

        # Verificar campos vazios
        for i in lista:
            if i == "":
                messagebox.showerror('Erro 000', 'Preencha todos os campos')
                return

        # Verificar se o ID do usuário existe
        conn = connect()
        cursor = conn.cursor()

        cursor.execute("SELECT id FROM usuarios WHERE id = ?", (id_usuario,))
        if cursor.fetchone() is None:
            messagebox.showerror("Erro", f"Usuário com ID {id_usuario} não encontrado.")
            conn.close()
            return

        # Verificar se o ID do livro existe
        cursor.execute("SELECT id FROM livros WHERE id = ?", (id_livro,))
        if cursor.fetchone() is None:
            messagebox.showerror("Erro", f"Livro com ID {id_livro} não encontrado.")
            conn.close()
            return

        # Enviar dados pro banco de dados
        realizar_emprestimo_bd(id_livro, id_usuario, hoje, None)

        messagebox.showinfo('Sucesso', 'Empréstimo realizado com sucesso!')

        # Limpar campos de entrada depois
        e_id_usuario.delete(0, END)
        e_id_livro.delete(0, END)

        conn.close()


    titulo_novo_usuario = Label(
        parteDireita, 
        text='FAZER EMPRESTIMO',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_novo_usuario.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )


    # ID livro
    l_id_livro = Label(
        parteDireita, 
        text='Digite o ID do livro:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_id_livro.grid(
        row=3, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_id_livro = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_id_livro.grid(
        row=3, column=1, padx=5, pady=5, sticky=NSEW
    )


    #ID usuario
    l_id_usuario = Label(
        parteDireita, 
        text='Digite o ID do Usuário:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    
    l_id_usuario.grid(
        row=2, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_id_usuario = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    
    e_id_usuario.grid(
        row=2, column=1, padx=5, pady=5, sticky=NSEW
    )

    
    #salvar
    salvar_img = Image.open('img/salvar.jpg')
    salvar_img = salvar_img.resize((18,18))
    salvar_img = ImageTk.PhotoImage(salvar_img)

    b_salvar = Button(
        parteDireita,
        command=add,
        image=salvar_img,
        width=150,  
        height=15,  
        compound=LEFT,  
        text='salvar',  
        bg=cor3,
        fg=cor1,
        font=('Arial', 11, 'bold'),
        overrelief=RIDGE,
        relief=GROOVE,
        padx=5,  
        pady=5
    )

    b_salvar.grid(
        row=6, column=0, columnspan=2, pady=10 
    )


#exibir emprestimos
def exibir_emprestimos():

    titulo_exibir_emprest = Label(
        parteDireita, 
        text='LIVROS EMPRESTADOS NO MOMENTO',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_exibir_emprest.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )

    ###
    dados = []
    emprestados = exibir_emprestimos_bd()
    for livro in emprestados:
        # Garante que os elementos ausentes sejam preenchidos com "N/A"
        dado = [livro[i] if i < len(livro) else "N/A" for i in range(5)]
        dados.append(dado)

    #creating a treeview with dual scrollbars
    list_header = ['ID','Título','Usuário','D.Emprestimo','D.Devolução']
    
    global tree

    tree = ttk.Treeview(parteDireita, selectmode="extended", columns=list_header, show="headings")
    #vertical scrollbar
    vsb = ttk.Scrollbar(parteDireita, orient="vertical", command=tree.yview)

    #horizontal scrollbar
    hsb = ttk.Scrollbar(parteDireita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)

    tree.grid(column=0, row=2, sticky='nsew')
    vsb.grid(column=1, row=2, sticky='ns')
    hsb.grid(column=0, row=3, sticky='ew')
    parteDireita.grid_rowconfigure(0, weight=12)

    hd=["nw","nw","nw","nw","nw"]
    h=[21,175,120,90,90,100]
    n=0

    for col in list_header:
        tree.heading(col, text=col, anchor='nw')
        #adjust the column's width to the header string
        tree.column(col, width=h[n],anchor=hd[n])
        
        n+=1

    for item in dados:
        tree.insert('', 'end', values=item)


# devolução
def devolucao():

    global salvar_img

    def add():
        id_emprestimo = e_id_emprestimo.get()
        data_devolucao = e_data_devolucao.get()

        lista = [id_emprestimo, data_devolucao]

        #verificar campos vazios
        for i in lista:
            if i =="":
                messagebox.showerror('Error 000:', 'Preencha todos os campos')
                return

        #enviar dados pro banco de dados
        atualizar_devolucao_bd(id_emprestimo, data_devolucao)

        messagebox.showinfo('LETS GOUR', 'Devolução realizada com sucesso!')

        #limpando os campos de entrada dps q valores forem inseridos
        e_id_emprestimo.delete(0,END)
        e_data_devolucao.delete(0,END)
     

    titulo_dev = Label(
        parteDireita, 
        text='DEVOLUÇÃO DE LIVRO',
        width=50, 
        padx=5, 
        pady=10, 
        font=('Arial', 12, "bold"), 
        bg=cor1, 
        fg=cor3
    )
    
    titulo_dev.grid(
        row=0, column=0, columnspan=4, sticky=NSEW
    )

    #linha
    linha_titulo = Label(
        parteDireita, 
        width=400, 
        height=1,  
        anchor=NW, 
        font=('Times New Roman', 1, "bold"), 
        bg=cor2, 
        fg=cor2
    )
    linha_titulo.grid(
        row=1, column=0, columnspan=4, sticky=NSEW
    )

    #ID emprestimo
    l_id_emprestimo = Label(
        parteDireita, 
        text='Digite o ID do Emprestimo:',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    
    l_id_emprestimo.grid(
        row=2, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_id_emprestimo = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    
    e_id_emprestimo.grid(
        row=2, column=1, padx=5, pady=5, sticky=NSEW
    )

    # data devolução
    l_data_devolucao = Label(
        parteDireita, 
        text='Digite a data de devolução (yyyy-mm-dd):',
        anchor=NW,  
        font=('Arial', 10, "bold"), 
        bg=cor1, 
        fg=cor0
    )
    l_data_devolucao.grid(
        row=3, column=0, padx=5, pady=5, sticky=NSEW
    )

    e_data_devolucao = Entry(
        parteDireita, 
        width=25,
        justify='left',
        relief='solid'
    )
    e_data_devolucao.grid(
        row=3, column=1, padx=5, pady=5, sticky=NSEW
    )

    
    #salvar
    salvar_img = Image.open('img/salvar.jpg')
    salvar_img = salvar_img.resize((18,18))
    salvar_img = ImageTk.PhotoImage(salvar_img)

    b_salvar = Button(
        parteDireita,
        command=add,
        image=salvar_img,
        width=150,  
        height=15,  
        compound=LEFT,  
        text='salvar',  
        bg=cor3,
        fg=cor1,
        font=('Arial', 11, 'bold'),
        overrelief=RIDGE,
        relief=GROOVE,
        padx=5,  
        pady=5
    )

    b_salvar.grid(
        row=6, column=0, columnspan=2, pady=10 
    )





#controlar menu
def control(i):

    #novo usiario
    # Limpa a tela antes de carregar a nova interface
    if i == 'novo_usuario':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        novo_usuario()


    #novo livro
    # Limpa a tela antes de carregar a nova interface
    if i == 'novo_livro':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        novo_livro()


    #exibir usuarios
    # Limpa a tela antes de carregar a nova interface
    if i == 'exibir_usuarios':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        exibir_usuarios()

    #exibir livros
    # Limpa a tela antes de carregar a nova interface
    if i == 'exibir_livros':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        exibir_livros()

    #emprestimo
    # Limpa a tela antes de carregar a nova interface
    if i == 'realizar_emprestimo':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        realizar_emprestimo()

    #exibir emprestimos
    # Limpa a tela antes de carregar a nova interface
    if i == 'exibir_emprestimos':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        exibir_emprestimos()

    #devolucao
    # Limpa a tela antes de carregar a nova interface
    if i == 'devolucao':
        for widget in parteDireita.winfo_children():
            widget.destroy()
        #chamar função
        devolucao()




#menu

#novo usuario
usuario_img = Image.open('img/add.jpg')
usuario_img = usuario_img.resize((18,18))
usuario_img = ImageTk.PhotoImage(usuario_img)

b_usuario = Button(
    parteMenu,
    command=lambda:control('novo_usuario'),
    image=usuario_img,
    compound=LEFT, 
    anchor= NW, 
    text=' novo usuário',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_usuario.grid(
    row=0,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)

#novo livro
novo_livro_img = Image.open('img/add.jpg')
novo_livro_img = novo_livro_img.resize((18,18))
novo_livro_img = ImageTk.PhotoImage(novo_livro_img)

b_novo_livro = Button(
    parteMenu,
    command=lambda:control('novo_livro'),
    image=novo_livro_img,
    compound=LEFT, 
    anchor= NW, 
    text=' novo livro',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_novo_livro.grid(
    row=1,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)

#exibir livros
livros_img = Image.open('img/livro.jpg')
livros_img = livros_img.resize((18,18))
livros_img = ImageTk.PhotoImage(livros_img)

b_livros = Button(
    parteMenu,
    command=lambda:control('exibir_livros'),
    image=livros_img,
    compound=LEFT, 
    anchor= NW, 
    text=' exibir os livros cadastrados',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_livros.grid(
    row=2,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)

#exibir usuarios
usuarios_img = Image.open('img/usuario.png')
usuarios_img = usuarios_img.resize((18,18))
usuarios_img = ImageTk.PhotoImage(usuarios_img)

b_usuarios = Button(
    parteMenu,
    command=lambda:control('exibir_usuarios'),
    image=usuarios_img,
    compound=LEFT, 
    anchor= NW, 
    text=' exibir os usuários cadastrados',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_usuarios.grid(
    row=3,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)

#realizar emprestimo
novo_emp_img = Image.open('img/add.jpg')
novo_emp_img = novo_emp_img.resize((18,18))
novo_emp_img = ImageTk.PhotoImage(novo_emp_img)

b_novo_emp = Button(
    parteMenu,
    command=lambda:control('realizar_emprestimo'),
    image=novo_emp_img,
    compound=LEFT, 
    anchor= NW, 
    text=' realizar um empréstimo',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_novo_emp.grid(
    row=4,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)


#devolução
devolucao_img = Image.open('img/dev.jpg')
devolucao_img = devolucao_img.resize((18,18))
devolucao_img = ImageTk.PhotoImage(devolucao_img)

b_devolucao = Button(
    parteMenu,
    command=lambda:control('devolucao'),
    image=devolucao_img,
    compound=LEFT, 
    anchor= NW, 
    text=' devolução de emprestimo',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_devolucao.grid(
    row=5,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)

#exibir emprestimos
exibir_emp_img = Image.open('img/emprest.jpg')
exibir_emp_img = exibir_emp_img.resize((18,18))
exibir_emp_img = ImageTk.PhotoImage(exibir_emp_img)

b_exibir_emp = Button(
    parteMenu,
    command=lambda:control('exibir_emprestimos'),
    image=exibir_emp_img,
    compound=LEFT, 
    anchor= NW, 
    text=' livros emprestados no momento',
    bg=cor3,
    fg=cor1,
    font=('Arial', 11), 
    overrelief=RIDGE,
    relief=GROOVE
)
b_exibir_emp.grid(
    row=6,
    column=0,
    sticky=NSEW,
    padx=5,
    pady=6
)


janela.mainloop()