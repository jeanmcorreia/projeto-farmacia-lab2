from config.db import criar_conexao
import psycopg2  


def autenticar(login, senha):
    try:
       
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT usuario, password FROM \"Projeto\".usuario")  

        
        for row in cursor.fetchall():
            usuario, password = row
            if usuario == login and password == senha:
                return True  

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")

    finally:
        
        try:
            cursor.close()  
        except:
            pass  

        try:
            conexao.close()  
        except:
            pass  

    return False  
          
            
    
   