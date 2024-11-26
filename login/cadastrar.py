import psycopg2
from config.db import criar_conexao


def cadastrar():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        Login = input("Digite o seu nome de usuário: ")
        Senha = input("Digite sua senha: ")
        Nome =  input("Digite o seu nome completo: ")
        query = "SELECT usuarioFuncionario, SenhaFuncionario FROM \"Projeto\".Funcionario where usuarioFuncionario = %s or SenhaFuncionario = %s"
        cursor.execute(query,(Login, Senha))  
        usuario_existe = cursor.fetchone()
        
        if usuario_existe:
            print("Falha no cadastro, usuario e/ou senha já existem.")
            return False  
        else:
            cursor.execute("INSERT INTO \"Projeto\".Funcionario (nomeFuncionario, usuarioFuncionario, SenhaFuncionario, NivelPermissao) VALUES (%s, %s, %s, %s)", (Nome, Login, Senha,'1'))
            print("Cadastro realizado com sucesso.")
            conexao.commit()
            return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        

    finally:
            cursor.close()
            conexao.close()
  
    

