from config.db import criar_conexao
import psycopg2


def gerar_estoque():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idproduto, nomeproduto from \"Projeto\".produto ")
        listaprod = cursor.fetchall()
        print("Produtos disponíveis:")
        for idproduto, nomeproduto in listaprod:
            print(f"ID: {idproduto} | Nome: {nomeproduto}")
        idProduto = int(input("Digite o id do produto contindo no lote: "))
        cursor.execute("Select idproduto from \"Projeto\".produto where idproduto = %s ",(idProduto,))
        prod_existe = cursor.fetchone()
        if not prod_existe:
             print("Produto não encontrado. Operação cancelada.")
             return False
        quantidade = int(input("Digite a quantidade do produto contindo no lote: "))
        validade = input("Digite a data de validade desse lote: ")
        cursor.execute("Select idproduto, idlote from \"Projeto\".detalhe_estoque where idproduto = %s and validade = %s", (idProduto, validade))
        prodlote_existe = cursor.fetchone()
        if prodlote_existe:
            print(F" o lote já existe ")
            return False
        else:
            cursor.execute("INSERT INTO \"Projeto\".detalhe_estoque(idProduto, quantidade, validade) values(%s, %s, %s)", (idProduto, quantidade, validade))
            conexao.commit()
            print(f"Estoque gerado com sucesso!")
            return True
             
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

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
        idlote = int(input("Digite o id do lote: "))
        idproduto = int(input("Digite o id atualizado do produto contindo no lote: "))
        quantidade = int(input("Digite a quantidade atualizada do produto contindo no lote: "))
        validade = input("Digite a data atualizada de validade desse lote: ")
        cursor.execute("SELECT * FROM \"Projeto\".detalhe_estoque where idLote = %s", (idlote,))
        lote_existe = cursor.fetchone()
        
        if lote_existe:
            cursor.execute("UPDATE \"Projeto\".detalhe_estoque SET idProduto = %s, quantidade = %s, validade = %s WHERE idLote = %s", (idproduto, quantidade, validade, idlote))
            conexao.commit()
            print(f"Lote '{idlote}' alterado com sucesso.")
            return True
            
        else:
            print("Falha na alteração, lote não existe")
            return False 
         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
        
    finally:
            cursor.close()
            conexao.close()

def excluir_lote():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        idlote = int(input("Digite o id do lote: "))
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o lote {idlote}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".detalhe_estoque WHERE idLote = %s', (idlote,))
            conexao.commit()
            print(f"Lote {idlote} excluído.")
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
     