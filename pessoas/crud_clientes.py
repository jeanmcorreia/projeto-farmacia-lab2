from config.db import criar_conexao
import psycopg2


def criar_cliente():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        nome = input("Digite o nome do cliente: ")
        cpf = input("Digite o cpf do cliente: ")
        endereco = input("Digite o endereço do cliente: ")
        celular = input("Digite o numero de celular do cliente: ")
        dataCadastro = input("Digite a data que o cliente está sendo cadastrado: ")
        cursor.execute("Select cpfcliente from \"Projeto\".cliente where cpfcliente = %s", (cpf,))
        cliente_existe = cursor.fetchone()
        if cliente_existe:
            print(f"O cliente de cpf '{cpf}' já existe")
            return False
        else:                     
            cursor.execute("INSERT INTO \"Projeto\".cliente(nomecliente, cpfcliente, enderecocliente, celularcliente, datacadastro) values(%s, %s, %s, %s, %s)", (nome, cpf, endereco, celular, dataCadastro))
            conexao.commit()
            print(f"Cliente criado com sucesso!")
            return True
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def relatorio_clientes():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idcliente, nomecliente from \"Projeto\".cliente ")
        relatorio_clientes = cursor.fetchall()
        print("Clientes:")
        for idcliente, nomecliente in relatorio_clientes:
            print(f"ID: {idcliente} | Nome: {nomecliente}")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
def editar_cliente():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        
        cursor.execute("Select idcliente, nomecliente, cpfcliente from \"Projeto\".cliente")
        listacliente = cursor.fetchall()
        print("Clientes Registrados:")
        for idcliente, nomecliente, cpfcliente in listacliente:
            print(f"ID: {idcliente} | Nome: {nomecliente} | CPF: {cpfcliente}")
        id = int(input("Digite o id do cliente: "))
        nome = input("Digite o nome atualizado do cliente: ")
        cpf = input("Digite o cpf atualizado do cliente: ")
        endereco = input("Digite o endereço atualizado do cliente: ")
        celular = input("Digite o numero de celular atualizado do cliente: ")
        dataCadastro = input("Digite a data que o cliente foi cadastrado atualizada: ")
        cursor.execute("SELECT * FROM \"Projeto\".cliente where idCliente = %s", (id,))
        cliente_existe = cursor.fetchone()
        
        if cliente_existe:
            cursor.execute("Select cpfcliente from \"Projeto\".cliente where cpfcliente = %s", (cpf,))
            cliente_igual = cursor.fetchone()
            if cliente_igual:
                print(f"O cliente de cpf '{cpf}' já existe")
                return False
            else:
                cursor.execute("UPDATE \"Projeto\".cliente SET nomeCliente = %s, cpfcliente = %s, enderecocliente = %s, celularcliente = %s, dataCadastro = %s WHERE idCliente = %s", (nome, cpf, endereco, celular, dataCadastro, id))
                conexao.commit()
                print(f"Funcionário com ID {id} atualizado com sucesso.")
                return True
            
        else:
            print("Falha na alteração, cliente não existe")
            return False 
         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def excluir_cliente():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        idcliente = int(input("Digite o id do cliente que deseja excluir: "))
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o cliente {idcliente}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".cliente WHERE idCliente = %s', (idcliente,))
            conexao.commit()
            print(f"cliente de id: {idcliente} excluído.")
            return True
        else:
            print("Exclusão cancelada.")
            return False
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
     