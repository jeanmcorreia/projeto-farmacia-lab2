from config.db import criar_conexao
import psycopg2


def criar_cliente(nome, cpf, endereco, celular, dataCadastro):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select cpf from \"Projeto\".cliente")
        cliente_existe = cursor.fetchone()
        if cliente_existe:
            print(f"O cliente de cpf '{cpf}' já existe")
            return False
        else:
            cursor.execute("INSERT INTO \"Projeto\".cliente values(%s, %s, %s, %s, %s)", nome, cpf, endereco, celular, dataCadastro)
            conexao.commit()
            print(f"Cliente criado com sucesso!")
            return True
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def relatorio_clientes():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".cliente")
        relatorio = cursor.fetchall()
        return relatorio
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def editar_cliente(id, nome, cpf, endereco, celular, dataCadastro):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".cliente where id = %s", id)
        func_existe = cursor.fetchone()
        
        if func_existe:
            cursor.execute("UPDATE \"Projeto\".cliente SET nomeCliente = %s, cpfcliente = %s, enderecocliente = %s, celularcliente = %s, dataCadastro = %s WHERE id = %s", nome, cpf, endereco, celular, dataCadastro, id)
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
            cursor.close()
            conexao.close()

def excluir_cliente(idcliente):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o cliente {idcliente}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".cliente WHERE id = %s', (idcliente,))
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
        cursor.close()
        conexao.close()
     