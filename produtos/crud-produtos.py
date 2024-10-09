import psycopg2
from config.db import criar_conexao

def criar_produtos(nome, preco, categoria, tarja):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos WHERE nome = %s' (nome,))
        produto_existente = cursor.fetchone()

        if produto_existente:
            print(f"O produto '{nome}' já existe!")
            return False
        else:
            cursor.execute("INSERT INTO \"Projeto\".produtos (nome, preco, categoria, tarja) VALUES (%s, %s, %s, %s)", (nome, preco, categoria, tarja))
            conexao.commit()
            print(f"Produto {nome} criado com sucesso!")
            return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def relatorio_produtos():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM produtos')
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()