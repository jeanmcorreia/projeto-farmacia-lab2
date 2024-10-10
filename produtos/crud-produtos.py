import psycopg2
from config.db import criar_conexao

def criar_produtos(nome, preco, categoria, tarja): #CREATE
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM \"Projeto\".produto WHERE nome = %s', (nome,))
        produto_existente = cursor.fetchone()

        if produto_existente:
            print(f"O produto '{nome}' já existe!")
            return False
        else:
            cursor.execute("INSERT INTO \"Projeto\".produto (nome, preco, categoria, tarja) VALUES (%s, %s, %s, %s)", (nome, preco, categoria, tarja))
            conexao.commit()
            print(f"Produto {nome} criado com sucesso!")
            return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def relatorio_produtos(): #READ
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM \"Projeto\".produto')
        relatorio = cursor.fetchall()
        return relatorio
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def atualizar_produto(idProduto, novo_nome, novo_preco, nova_categoria, nova_tarja): #UPDATE
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('UPDATE \"Projeto\".produto SET nome = %s, preco = %s, categoria = %s, tarja = %s WHERE id = %s', (novo_nome, novo_preco, nova_categoria, nova_tarja, idProduto))
        conexao.commit()
        print(f"Produto {idProduto} atualizado com sucesso!")
        return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def excluir_produto(idProduto): #DELETE
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o produto {idProduto}? (Isso excluirá o produto permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".produto WHERE id = %s', (idProduto,))
            conexao.commit()
            print(f"Produto {idProduto} excluído.")
            return True
        else:
            print("Exclusão cancelada.")
            return False
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        cursor.close()
        conexao.close()