import psycopg2
from config.db import criar_conexao

login = None
senha = None
autenticado = False

def autenticar():
    global login, senha, autenticado
    try:
        
        if not autenticado:
            
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            
            conexao = criar_conexao()
            cursor = conexao.cursor()
            query = "SELECT usuarioFuncionario, SenhaFuncionario FROM \"Projeto\".Funcionario where usuarioFuncionario = %s and SenhaFuncionario = %s"
            cursor.execute(query,(login, senha))
            user_existe = cursor.fetchone()
            if user_existe:
                autenticado = True  
                return login, senha, autenticado 
            else:
                return False
    except Exception as error:
        print(f'Erro ao acessar o banco de dados {error}')
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
    
        
          
            
    
   