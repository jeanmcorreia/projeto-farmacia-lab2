import psycopg2
from config.db import criar_conexao
from login.autenticar import autenticar

def cadastrar(Login,Senha):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        
        
        if autenticar(Login, Senha):
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
  
    

