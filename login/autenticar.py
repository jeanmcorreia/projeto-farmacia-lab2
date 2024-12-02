import psycopg2
from config.db import criar_conexao
import bcrypt

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
            query = "SELECT usuarioFuncionario, SenhaFuncionario FROM \"Projeto\".Funcionario WHERE usuarioFuncionario = %s"
            cursor.execute(query, (login,))
            user_existe = cursor.fetchone()

            if user_existe:
                
                senha_hash = user_existe[1]  
                
                if isinstance(senha_hash, memoryview):
                    senha_hash = bytes(senha_hash)
                
                if bcrypt.checkpw(senha.encode('utf-8'), senha_hash):  
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
        
          
            
    
   