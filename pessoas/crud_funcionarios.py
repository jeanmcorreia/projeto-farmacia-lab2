from config.db import criar_conexao
import psycopg2


def criar_funcionario(nome, cpf, endereco, celular, data_admissao):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select cpf from \"Projeto\".funcionario")
        funcionario_existe = cursor.fetchone()
        if funcionario_existe:
            print(f"O Funcionario de cpf '{cpf}' já existe")
            return False
        else:
            cursor.execute("INSERT INTO \"Projeto\".funcionario values(%s, %s, %s, %s, %s)", nome, cpf, endereco, celular, data_admissao)
            conexao.commit()
            print(f"Funcionário criado com sucesso!")
            return True
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def relatorio_funcionarios():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".funcionario")
        relatorio = cursor.fetchall()
        return relatorio
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def editar_funcionario(id, nome, cpf, endereco, celular, data_admissao):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".funcionario where idFuncionario = %s", id)
        func_existe = cursor.fetchone()
        
        if func_existe:
            cursor.execute("UPDATE \"Projeto\".funcionario SET nomefuncionario = %s, cpffuncionario = %s, enderecofuncionario = %s, celularfuncionario = %s, admissao = %s WHERE idFuncionario = %s", nome, cpf, endereco, celular, data_admissao, id)
            conexao.commit()
            print(f"Funcionário com ID {id} atualizado com sucesso.")
            return True
            
        else:
            print("Falha na Alteração, Funcionario não existe")
            return False 
         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
        
    finally:
            cursor.close()
            conexao.close()

def excluir_funcionario(idfuncionario):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o funcionario {idfuncionario}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".funcionario WHERE id = %s', (idfuncionario,))
            conexao.commit()
            print(f"Funcionario de id: {idfuncionario} excluído.")
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
     