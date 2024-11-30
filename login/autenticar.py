import psycopg2
from config.db import criar_conexao

login = None
senha = None
autenticado = False

def autenticar():
    global login, senha, autenticado
    conexao = None
    cursor = None
    try:
        if not autenticado:
            login = input("Digite o login: ")
            senha = input("Digite a senha: ")
            
            conexao = criar_conexao()
            cursor = conexao.cursor()
            query = "SELECT usuarioFuncionario, SenhaFuncionario FROM \"Projeto\".Funcionario WHERE usuarioFuncionario = %s and SenhaFuncionario = %s"
            cursor.execute(query, (login, senha))
            user_existe = cursor.fetchone()

            if user_existe:
                autenticado = True 
                return autenticado, login
            else:
                return False
        else:
            return autenticado, login
    except Exception as error:
        print(f'Erro ao acessar o banco de dados: {error}')
        return False, None
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
        
          
            
    
   