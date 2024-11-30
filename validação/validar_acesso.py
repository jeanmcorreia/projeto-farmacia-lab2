import psycopg2
from config.db import criar_conexao
from login.autenticar import autenticar



def validar_acesso():
    
    autenticado, login = autenticar()
    
    if not autenticado:
        return False
    
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "Select * from \"Projeto\".funcionario where UsuarioFuncionario = %s"
        cursor.execute(query,(login,))
        Permission = cursor.fetchone()
        if Permission:
            return Permission[7]
        else:
            return False
        
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close() 
    
   
   