from config.db import criar_conexao
import psycopg2


def gerar_pedido(cliente, funcionario, formadepgt, datapedido):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("INSERT INTO \"Projeto\".pedido(idcliente, idfuncionario, formapagamento, datapedido) VALUES(%s, %s, %s, %s)", (cliente, funcionario, formadepgt, datapedido))
        cursor.execute("SELECT idPedido FROM \"Projeto\".pedido ORDER BY idPedido DESC LIMIT 1")
        idpedido = cursor.fetchone()[0]

        while True:
            idproduto = input(f"Digite o ID do produto ou 'F' para finalizar: ")
            if idproduto == "F":
                break
            quantidade = input(f"Digite a quantidade do produto: ")
            cursor.execute("INSERT INTO \"Projeto\".tbl_detalhe_pedidos (idpedido, idproduto, quantidade) VALUES (%s, %s, %s)", (idpedido, idproduto, quantidade))
                
        cursor.execute("UPDATE \"Projeto\".pedido SET valortotal = (SELECT SUM(preco * quantidade) FROM \"Projeto\".produto p, \"Projeto\".tbl_detalhe_pedidos dp WHERE dp.idproduto = p.idproduto AND dp.idpedido = %s)",(idpedido,))
        cursor.execute("UPDATE \"Projeto\".detalhe_estoque set quantidade = quantidade - %s where idproduto = %s ", (quantidade, idproduto))

        conexao.commit()
        print(f"Pedidos gerado com sucesso e produtos adicionados!")
        return True
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def relatorio_pedidos():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".pedido")
        relatorio = cursor.fetchall()
        print(relatorio)
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def editar_pedido(idpedido, cliente, funcionario, formadepgt, valortotal, datapedido):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT * FROM \"Projeto\".pedido where idPedido = %s", (idpedido,))
        pedido_existe = cursor.fetchone()
        
        if pedido_existe:
            cursor.execute("UPDATE \"Projeto\".pedido SET idCliente = %s,  idFuncionario = %s, formaPagamento = %s, valorTotal = %s, dataPedido = %s WHERE idPedido = %s",  (cliente, funcionario, formadepgt, valortotal, datapedido, idpedido))
            conexao.commit()
            print(f"Pedido {idpedido} alterado com sucesso.")
            return True
            
        else:
            print("Falha na alteração, pedido não existe")
            return False 
         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
        
    finally:
            cursor.close()
            conexao.close()

#def editar_produto_pedido(idpedido, idproduto, quantidade):
    #try:
        #conexao = criar_conexao()
        #cursor = conexao.cursor()
        #cursor.execute("SELECT * FROM \"Projeto\".tbl_detalhe_pedido where idPedido = %s and idProduto = %s", idpedido, idproduto)
        #pedido_produto_existe = cursor.fetchone()
        
        #if pedido_produto_existe:
            #cursor.execute("UPDATE \"Projeto\".tbl_detalhe_pedido SET quantidade = %s", quantidade)
            #conexao.commit()
            #print(f"Pedido {idpedido} alterado com sucesso.")
            #return True
            
        #else:
            #print("Falha na alteração, lote não existe")
            #return False 
         
    #except (Exception, psycopg2.DatabaseError) as error:
        #print(f"Erro ao acessar o banco de dados: {error}")
        #return False
        
    #finally:
            #cursor.close()
            #conexao.close()

def excluir_pedido(idpedido):
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o pedido {idpedido}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".pedido WHERE idpedido = %s', (idpedido,))
            cursor.execute('DELETE FROM \"Projeto\".tbl_detalhe_pedidos WHERE idpedido = %s', (idpedido,))
            conexao.commit()
            print(f"Pedido {idpedido} excluído.")
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
     