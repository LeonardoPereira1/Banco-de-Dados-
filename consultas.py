import configBD as db

db.conectar()

key= True

while key:

    valor= int(input('Qual consulta deseja fazer ? 1-Soma dos preços, 2-Média dos preços, 3-Máximo dos preços, 4-Mínimo dos preços, 5-Ordernar produto por preco(Menor-Maior), 6-Ordernar produtos por nome(A-Z), 7-Ordernar usuarios por nome(A-Z), 8-Buscar produto, 9-Buscar usuario, 10-Inserir produto, 11-Inserir usuario, 12-Atualizar dados de produto, 13-Atualizar dados de usuário,14-Deletar usuario, 15-Deletar produtos, 16-Selecionar dados dos Usuarios por CPF, 17-Selecionar dados de produto por ID, 0-PARA ENCERRAR AS CONSULTAS: '))

    print('-='*30)
    
    

    if valor == 0:
        key = False

    elif valor == 1 :
        db.soma_PrecoProdutos()

    elif valor == 2 :
        db.media_Preco()

    elif valor == 3 :
        db.max_Preco()
    
    elif valor == 4:
        db.min_Preco()
    
    elif valor == 5 :
        db.ordernar_Preco()

    elif valor == 6 :
        db.ordernar_NomeProduto()

    elif valor == 7 :
        db.ordernar_NomeUsuario()

    elif valor == 8 :
        id_produto= int(input('Insira o ID do produto: '))

        db.buscar_Produto(id_produto)
    
    elif valor == 9:
        cpf=int(input('Insira o CPF do usuario: '))

        db.buscar_Usuario(cpf)
    
    elif valor == 10:
        nome=input('Digite o nome do produto: ')
        preco=input('Insira o preco do produto: ')

        db.insira_Produto(nome,preco)

        print('Produto inserido com sucesso !')

    elif valor == 11:
        cpf=input('Digite o cpf do usuario: ')
        nome=input('Digite o nome do usuario: ')
        email=input('Digite o email do usuario: ')
        senha=input('Digite a senha do usuario: ')
        endereco=input('Digite o endereco do usuario: ')

        db.insira_Usuario(cpf,nome,email,senha,endereco)

        print('Usuario inserido com sucesso !')

    elif valor == 12:

        id_produto= int(input('Insira o ID do produto: '))
        novo_preco= float(input('Digite o novo preço do produto: '))

        db.atualizar_Produto(id_produto,novo_preco)

    elif valor == 13:
        cpf=input('Digite o cpf do usuario: ')
        novo_email=input('Digite o email do usuario: ')
        nova_senha=input('Digite a senha do usuario: ')

        db.atualizar_Usuario(cpf,novo_email,nova_senha)

    elif valor == 14:
        cpf=input('Digite o cpf do usuario: ')

        db.deletar_Usuario(cpf)

    elif valor == 15:
        id_produto= int(input('Insira o ID do produto: '))

        db.deletar_Produto(id_produto)
    
    elif valor == 16:
        cpf=input('Digite o cpf do usuario: ')

        db.buscar_Usuario(cpf)

    elif valor == 17:
        id_produto= int(input('Insira o ID do produto: '))

        db.buscar_Produto(id_produto)

    else: 
        valor= int(input('Valor inválido, porfavor escolha entre ---> 1-Soma dos preços, 2-Média dos preços, 3-Máximo dos preços, 4-Mínimo dos preços, 5-Ordernar produto por preco(Menor-Maior), 6-Ordernar produtos por nome(A-Z), 7-Ordernar usuarios por nome(A-Z), 8-Buscar produto, 9-Buscar usuario, 10-Inserir produto, 11-Inserir usuario, 12-Atualizar dados de produto, 13-Atualizar dados de usuário,14-Deletar usuario, 15-Deletar produtos, 16-Selecionar dados dos Usuarios por CPF, 17-Selecionar dados de produto por ID, 0-PARA ENCERRAR AS CONSULTAS: '))

db.fechar_Banco()
