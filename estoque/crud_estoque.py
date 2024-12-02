from config.db import criar_conexao
import psycopg2


def relatorio_estoque():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select nomeproduto, quantidade from \"Projeto\".produto")
        relatorio_lote = cursor.fetchall()
        print("Estoque:")
        for nomeproduto, quantidade in relatorio_lote:
            print(f"PRODUTO: {nomeproduto} | QUANTIDADE: {quantidade}")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def editar_estoque():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idproduto, nomeproduto, quantidade from \"Projeto\".produto")
        lista_produtos = cursor.fetchall()

        for idproduto, nomeproduto, quantidade in lista_produtos:
            print(f"ID: {idproduto} | Nome: {nomeproduto} | Quantidade: {quantidade}")

        idProduto = int(input("Digite o id do produto: "))
        cursor.execute('select * from \"Projeto\".produto where idproduto = %s', (idProduto,))
        produto_existe = cursor.fetchone()

        if produto_existe:
            quantidade = int(input("Digite a nova quantidade: "))  
            cursor.execute('UPDATE \"Projeto\".produto SET quantidade = %s WHERE idproduto = %s', (quantidade, idProduto))
            conexao.commit()
            print(f"Produto {idProduto} atualizado com sucesso!")
            return True
        else:
            print(f"Produto de id: {idProduto}, não existe.")
            return False

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

     