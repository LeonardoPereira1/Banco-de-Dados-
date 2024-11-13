def conectar():
    """Use essa funçao para importar as tabelas, o import do sqlite, e as variaveis necessárias"""
    import sqlite3
    
    global conexao, cursor

    conexao= sqlite3.connect('database.db')
    cursor= conexao.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS Usuarios (
                   cpf INTEGER PRIMARY KEY, 
                   nome TEXT NOT NULL,
                   email TEXT NOT NULL,
                   senha TEXT NOT NULL,
                   endereco TEXT NOT NULL, 
                   idLogin INTEGER, 
                   FOREIGN KEY(idLogin) REFERENCES Login(idLogin))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Loja (
                   CNPJ INTEGER PRIMARY KEY, 
                   nome TEXT NOT NULL, 
                   lucro INTEGER NOT NULL, 
                   idLogin INTEGER , 
                   FOREIGN KEY(idLogin) REFERENCES Login(idLogin))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Produtos (
                   ID_Produto INTEGER PRIMARY KEY AUTOINCREMENT, 
                   nome TEXT NOT NULL,
                   preco REAL NOT NULL)''')

    #Tabelas de relacionamento
    cursor.execute('''CREATE TABLE IF NOT EXISTS Pedidos (
                   ID_pedido INTEGER PRIMARY KEY, 
                   preco INTEGER NOT NULL, 
                   nome TEXT NOT NULL, 
                   endereco TEXT NOT NULL)''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Faz (
                   ID_pedido INTEGER NOT NULL, 
                   cpf INTEGER NOT NULL, 
                   PRIMARY KEY(ID_pedido, cpf), 
                   FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido), 
                   FOREIGN KEY(cpf) REFERENCES Usuario(cpf))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Aprova (
                   CNPJ INTEGER NOT NULL, 
                   ID_pedido INTEGER NOT NULL, 
                   PRIMARY KEY(CNPJ, ID_pedido), 
                   FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ), 
                   FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Envia (
                   CNPJ INTEGER NOT NULL, 
                   ID_Produto INTEGER NOT NULL, 
                   PRIMARY KEY(CNPJ, ID_Produto), 
                   FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ), 
                   FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Possui (
                   ID_Produto INTEGER NOT NULL, 
                   CNPJ INTEGER NOT NULL, 
                   PRIMARY KEY(ID_Produto, CNPJ), 
                   FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto), 
                   FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Contem (
                   ID_pedido INTEGER NOT NULL, 
                   ID_Produto INTEGER NOT NULL, 
                   PRIMARY KEY(ID_pedido, ID_Produto), 
                   FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido), 
                   FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto))''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS Login (iLogin INTEGER PRIMARY KEY AUTOINCREMENT, 
                   cpf INTEGER, 
                   FOREIGN KEY(cpf) REFERENCES Usuario(cpf))''')


def insira_Usuario(cpf, nome, email, senha, endereco):
    """Use essa função para inserir usuarios no banco de dados"""

    cursor.execute('INSERT INTO Usuarios(cpf, nome, email, senha, endereco) VALUES(?,?,?,?,?)'
                   ,(cpf, nome, email, senha, endereco))
    conexao.commit()

def insira_Produto(nome, preco):
    """Use essa função para inserir produtos no banco de dados"""

    cursor.execute(('INSERT INTO Produtos(preco, nome) VALUES(?,?)'),
                   (preco, nome))
    conexao.commit()

def soma_PrecoProdutos():
    """Use essa função para somar o preço de todos os produtos"""

    cursor.execute('SELECT SUM(preco) FROM Produtos')
    soma_Precos= cursor.fetchone()

    print('Soma dos preços é :', soma_Precos)

def media_Preco():
    """Use essa função para saber a media do preço dos produtos"""

    cursor.execute('SELECT AVG(preco) FROM Produtos')
    media= cursor.fetchone()
    print('A media dos preços é:', media)

def max_Preco():
    """Use essa função para saber o preco máximo na tabela produtos"""

    cursor.execute('SELECT MAX(preco) FROM Produtos')
    max= cursor.fetchone()

    print('O preço mais alto é:', max)
    
def min_Preco():
    """Use essa função para saber o preco minimo na tabela produtos"""

    cursor.execute('SELECT min(preco) FROM Produtos')
    min= cursor.fetchone()

    print('O preço mais baixo é:', min)

def ordernar_Preco():
    """Use essa função para ordenar o preço menor pro maior"""

    cursor.execute('SELECT * FROM Produtos ORDER BY preco ASC')
    preco_Ord= cursor.fetchall()

    print('Os dados ordenados do maior pro menor de acordo com seu preço: ', preco_Ord)

def ordernar_NomeProduto():
    """Use essa função para ordenar o nome dos produtos de  A-Z"""

    cursor.execute('SELECT * FROM Produtos ORDER BY nome ASC')
    nome_Ord= cursor.fetchall()

    print('Os produtos ordenados de A-Z: ', nome_Ord)

def ordernar_NomeUsuario():
    """Use essa função para ordenar o nome dos usuarios de A-Z"""

    cursor.execute('SELECT * FROM Usuarios ORDER BY nome ASC')
    nome_Ord= cursor.fetchall()

    print('Os usuarios ordenados do  de A-Z: ', nome_Ord)

def buscar_Produto(ID_Produto):
    """Use essa função para buscar um produto pelo ID"""

    cursor.execute('SELECT * FROM Produtos WHERE ID_Produto = ?',(ID_Produto,))
    produto= cursor.fetchone()

    if produto:
        print(produto)
    else:
        print('Produto não encontrado')

def buscar_Usuario(cpf):
    """Use essa função para buscar um Usuário pelo CPF"""

    cursor.execute('SELECT * FROM Usuarios WHERE cpf = ?',(cpf,))
    usuario= cursor.fetchone()

    if usuario:
        print(usuario)
    else:
        print('Pessoa não encontrada')

def atualizar_Usuario(cpf,novo_email,nova_senha):
    """Use essa função para atualizar o e-mail e a senha de um usuário"""
    
    cursor.execute('UPDATE Usuarios SET email = ?, senha = ? WHERE cpf= ?',(novo_email,nova_senha,cpf))


    conexao.commit()

    print('Usuário atualizado com sucesso !')

def atualizar_Produto(ID_Produto, novo_preco):
    """Use essa função para atualizar o preço de algum produto"""
    
    cursor.execute('UPDATE Produtos SET preco = ? WHERE ID_Produto= ?',(novo_preco,ID_Produto))

    conexao.commit()

    print('Produto atualizado com sucesso !')

def deletar_Usuario(cpf):
    """Use essa função para deletar um Usuário"""

    conexao.execute('DELETE FROM Usuarios WHERE cpf= ?', (cpf,))
    conexao.commit()

    print('Usuário contratado pelo Vasco com sucesso !')

def deletar_Produto(ID_Produto):
    """Use essa função para deletar um Produto"""

    conexao.execute('DELETE FROM Produtos WHERE ID_Produto= ?', (ID_Produto,))
    conexao.commit()

    print('Produto deletado com sucesso !')

def fechar_Banco():
    """Use essa função para fechar o banco"""

    conexao.close()

    print('A conexão com o banco foi encerrada')


