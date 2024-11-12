def conectar():
    """Use essa funçao para importar as tabelas, o import do sqlite, e as variaveis necessárias"""
    import sqlite3
    
    global conexao, cursor

    conexao= sqlite3.connect('data/E-commerce.db')
    cursor= conexao.cursor()

    cursor.execute('CREATE TABLE IF NOT EXISTS Usuario (CPF INTEGER PRIMARY KEY, nome TEXT NOT NULL, email TEXT NOT NULL, senha TEXT NOT NULL, endereco TEXT NOT NULL, idLogin INTEGER NOT NULL, FOREIGN KEY(idLogin) REFERENCES Login(idLogin))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Loja (CNPJ INTEGER PRIMARY KEY, nome TEXT NOT NULL, lucro INTEGER NOT NULL, idLogin INTEGER NOT NULL, FOREIGN KEY(idLogin) REFERENCES Login(idLogin))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Produtos (ID_Produto INTEGER PRIMARY KEY, nome TEXT NOT NULL)')

    #Tabelas de relacionamento
    cursor.execute('CREATE TABLE IF NOT EXISTS Pedidos ( D_pedido INTEGER PRIMARY KEY, preco INTEGER NOT NULL, nome TEXT NOT NULL, endereco TEXT NOT NULL)')
    cursor.execute('CREATE TABLE IF NOT EXISTS Faz (ID_pedido INTEGER NOT NULL, CPF INTEGER NOT NULL, PRIMARY KEY(ID_pedido, CPF), FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido), FOREIGN KEY(CPF) REFERENCES Usuario(CPF))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Aprova (CNPJ INTEGER NOT NULL, ID_pedido INTEGER NOT NULL, PRIMARY KEY(CNPJ, ID_pedido), FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ), FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Envia (CNPJ INTEGER NOT NULL, ID_Produto INTEGER NOT NULL, PRIMARY KEY(CNPJ, ID_Produto), FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ), FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Possui (ID_Produto INTEGER NOT NULL, CNPJ INTEGER NOT NULL, PRIMARY KEY(ID_Produto, CNPJ), FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto), FOREIGN KEY(CNPJ) REFERENCES Loja(CNPJ))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Contem (ID_pedido INTEGER NOT NULL, ID_Produto INTEGER NOT NULL, PRIMARY KEY(ID_pedido, ID_Produto), FOREIGN KEY(ID_pedido) REFERENCES Pedidos(ID_pedido), FOREIGN KEY(ID_Produto) REFERENCES Produtos(ID_Produto))')
    cursor.execute('CREATE TABLE IF NOT EXISTS Login (CPF INTEGER PRIMARY KEY, idLogin INTEGER AUTO INCREMENT, FOREIGN KEY(CPF) REFERENCES Usuario(CPF))')


def insira_User(CPF, nome, email, senha, endereco):
    """Use essa função para inserir usuarios no banco de dados"""

    cursor.execute('INSERT INTO Usuarios(CPF, nome, email, senha, endereco, idLogin) VALUES(?,?,?,?))'),(CPF, nome, email, senha, endereco) 

def insira_Produto(id_Produto, nome):
    """Use essa função para inserir produtos no banco de dados"""

    cursor.execute('INSERT INTO Produtos(id_Produto, nome) VALUES(?,?,?,?))'),(id_Produto, nome)



    

    


