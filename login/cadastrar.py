import psycopg2
from config.db import criar_conexao
from criptografar.cripto_senha import criptografar
import bcrypt


def cadastrar():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        Login = input("Digite o seu nome de usuário: ")
        Senha = input("Digite sua senha: ")
        Nome =  input("Digite o seu nome completo: ")
        query = "SELECT usuarioFuncionario, SenhaFuncionario FROM \"Projeto\".Funcionario where usuarioFuncionario = %s"
        cursor.execute(query,(Login,))  
        usuario_existe = cursor.fetchone()
        
        if usuario_existe:
            print("Falha no cadastro, usuario já existe.")
            return False  
        else:
            senha_hash = criptografar(Senha)
            cursor.execute("INSERT INTO \"Projeto\".Funcionario (nomeFuncionario, usuarioFuncionario, SenhaFuncionario, NivelPermissao) VALUES (%s, %s, %s, %s)", (Nome, Login, senha_hash,'2'))
            print("Cadastro realizado com sucesso.")
            conexao.commit()
            return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
  
    

