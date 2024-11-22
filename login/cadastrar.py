import psycopg2
from config.db import criar_conexao


def cadastrar():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        Login = input("Digite o seu login: ")
        Senha = input("Digite sua senha: ")
        query = "SELECT usuario, password FROM \"Projeto\".usuario where usuario = %s or password = %s"
        cursor.execute(query,(Login, Senha))  
        usuario_existe = cursor.fetchone()
        
        if usuario_existe:
            print("Falha no cadastro, usuario e/ou senha já existem.")
            return False  
        else:
            cursor.execute("INSERT INTO \"Projeto\".usuario (Usuario, Password) VALUES (%s, %s)", (Login, Senha))
            print("Cadastro realizado com sucesso.")
            conexao.commit()
            return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        

    finally:
            cursor.close()
            conexao.close()
  
    

