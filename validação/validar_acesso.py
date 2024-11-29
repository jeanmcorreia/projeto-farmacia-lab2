import psycopg2
from config.db import criar_conexao
from login.autenticar import autenticar


def validar_acesso():
    
    login, senha, autenticado = autenticar()
    
    if not autenticado:
        return False
    
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        query = "Select NivelPermissao from \"Projeto\".funcionario where UsuarioFuncionario = %s and SenhaFuncionario = %s"
        cursor.execute(query,(login, senha))
        Permission = cursor.fetchone()
        if Permission:
            return Permission[0]
        else:
            return False
        
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
    finally:
        cursor.close()
        conexao.close() 
    
   
   