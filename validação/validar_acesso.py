import psycopg2
from config.db import criar_conexao


def validar_acesso(login, Senha):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor
        query = "Select NivelPermissao from \"Projeto\".funcionario where UsuarioFuncionario = %s and SenhaFuncionario %s"
        cursor.excute(query,(login, Senha))
        Permission = cursor.fetchone()
        if Permission:
            return Permission[7]
        else:
            return False
        
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
    finally:
        cursor.close()
        conexao.close() 
    
   
   