from config.db import criar_conexao
import psycopg2


def relatorio_estoque():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idlote, validade from \"Projeto\".detalhe_estoque")
        relatorio_lote = cursor.fetchall()
        print("Estoque:")
        for idlote, validade in relatorio_lote:
            print(f"ID: {idlote} | Nome: {validade}")
        
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
        cursor.execute("Select idproduto, nomeproduto, preco from \"Projeto\".produto")
        lista_produtos = cursor.fetchall()

        for idproduto, nomeproduto, preco in lista_produtos:
            print(f"ID: {idproduto} | Nome: {nomeproduto} | Preço: {preco}")

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
            cursor.close()
            conexao.close()

     