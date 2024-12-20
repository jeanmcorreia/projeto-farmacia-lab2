from config.db import criar_conexao
import psycopg2


def gerar_pedido():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute("Select idcliente, nomecliente from \"Projeto\".cliente")
        listacliente = cursor.fetchall()
        print("Clientes Registrados:")
        for idcliente, nomecliente in listacliente:
            print(f"ID: {idcliente} | Nome: {nomecliente}")
        cliente = int(input("Digite o id do cliente que fez o pedido: "))
        cursor.execute("Select idcliente from \"Projeto\".cliente where idcliente = %s ",(cliente,))
        cliente_existe = cursor.fetchone()
        if not cliente_existe:
             print("Cliente não encontrado. Operação cancelada.")
             return False
        
        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario")
        listaFunc = cursor.fetchall()
        print("Funcionarios Registrados:")
        for idfuncionario, nomefuncionario in listaFunc:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        funcionario = int(input("Digite o id do funcionario responsável pelo pedido: "))
        cursor.execute("Select idfuncionario from \"Projeto\".funcionario where idfuncionario = %s ",(funcionario,))
        Func_existe = cursor.fetchone()
        if not Func_existe:
             print("Funcionário não encontrado. Operação cancelada.")
             return False
         
        formadepgt = input("digite a forma de pagamento: ").upper()
        formas_validas = {"PIX", "CREDITO", "DEBITO"}
        if formadepgt not in formas_validas:
            print(f'Forma de pagamento: "{formadepgt}", não existente')
            return False
            
        datapedido = input("Digite a data que o pedido esta sendo efetuado: ")
        cursor.execute("INSERT INTO \"Projeto\".pedido (idcliente, idfuncionario, formapagamento, datapedido) VALUES (%s, %s, %s, %s)", (cliente, funcionario, formadepgt, datapedido))
        cursor.execute("SELECT idPedido FROM \"Projeto\".pedido ORDER BY idPedido DESC LIMIT 1")
        idpedido = cursor.fetchone()[0]
        
        id_produto_adicionado = []
        
        while True:
            cursor.execute("Select idproduto, nomeproduto, preco, quantidade from \"Projeto\".produto")
            lista_produtos = cursor.fetchall()
            print("Produtos Registrados:")
            for idproduto, nomeproduto, preco, quantidade in lista_produtos:
                print(f"ID: {idproduto} | Nome: {nomeproduto} | Preço: {preco} | Quantidade: {quantidade}")
            idproduto = int(input("Digite o ID do produto ou '0' para finalizar: "))
            if idproduto in id_produto_adicionado:
                print(f'produto de id:"{idproduto}", já foi adicionado a esse pedido')
                continue
            cursor.execute("Select idproduto from \"Projeto\".produto")
            if idproduto == 0:
                break
            
            cursor.execute("SELECT * FROM \"Projeto\".produto WHERE idProduto = %s", (idproduto,))
            produto_existe = cursor.fetchone()
            
            if produto_existe:
                quantidade = int(input(f"Digite a quantidade do produto: "))
                
                cursor.execute("SELECT quantidade FROM \"Projeto\".produto WHERE idProduto = %s", (idproduto,))
                estoque = cursor.fetchone()
                
                if estoque and estoque[0] >= quantidade:
                    cursor.execute("INSERT INTO \"Projeto\".tbl_detalhe_pedidos (idpedido, idproduto, quantidade) VALUES (%s, %s, %s)", (idpedido, idproduto, quantidade))
                    cursor.execute("UPDATE \"Projeto\".produto SET quantidade = quantidade - %s WHERE idproduto = %s", (quantidade, idproduto))
                    id_produto_adicionado.append(idproduto)
                else:
                    print(f"Quantidade solicitada ({quantidade}) não disponível em estoque.")
            else:
                print("produto não existe.")

        cursor.execute("UPDATE \"Projeto\".pedido SET valortotal = (SELECT SUM(p.preco * dp.quantidade) FROM \"Projeto\".produto p, \"Projeto\".tbl_detalhe_pedidos dp WHERE dp.idproduto = p.idproduto AND dp.idpedido = %s) where idpedido = %s", (idpedido, idpedido))
        
        conexao.commit()
        print("Pedido gerado com sucesso e produtos adicionados!")
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
        cursor.execute("Select dp.iddetalhep, pe.idcliente, c.nomecliente, dp.idproduto, p.nomeproduto, dp.quantidade from \"Projeto\".tbl_detalhe_pedidos dp inner join \"Projeto\".pedido pe ON pe.idpedido = dp.idpedido inner join \"Projeto\".produto p ON p.idproduto  = dp.idproduto inner join \"Projeto\".cliente c ON c.idcliente = pe.idcliente")
        lista_pedidos = cursor.fetchall()
        print("Pedidos:")
        for iddetalhep, idcliente, nomecliente, idproduto, nomeproduto, quantidade in lista_pedidos:
            print(f"ID: {iddetalhep} | CLIENTE: {idcliente} - {nomecliente} | PRODUTO: {idproduto} - {nomeproduto} | QTD: {quantidade}")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            cursor.close()
            conexao.close()

def editar_pedido():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()

        cursor.execute("Select p.idpedido, p.idcliente, c.nomecliente from \"Projeto\".pedido p inner join \"Projeto\".cliente c ON p.idcliente = c.idcliente")
        lista_pedido = cursor.fetchall()
        print("Pedidos Registrados:")
        for idpedido, idcliente, nomecliente in lista_pedido:
            print(f"ID: {idpedido} | CLIENTE: {idcliente} - {nomecliente}")
        idpedido = int(input("Digite o id do pedido: "))
        
        cursor.execute("Select idcliente, nomecliente from \"Projeto\".cliente")
        listacliente = cursor.fetchall()
        print("Clientes Registrados:")
        for idcliente, nomecliente in listacliente:
            print(f"ID: {idcliente} | Nome: {nomecliente}")
        cliente = int(input("Digite o id atualizado do cliente que fez o pedido: "))

        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario")
        listaFunc = cursor.fetchall()
        print("Funcionarios Registrados:")
        for idfuncionario, nomefuncionario in listaFunc:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        funcionario = int(input("Digite o nome atualizado do funcionario responsável pelo pedido: "))
        formadepgt = input("digite a forma de pagamento atualizada: ")
        datapedido = input("Digite a data atualizada que o pedido foi efetuado: ")
        cursor.execute("SELECT * FROM \"Projeto\".pedido where idPedido = %s", (idpedido,))
        pedido_existe = cursor.fetchone()
        
        if pedido_existe:
            cursor.execute("UPDATE \"Projeto\".pedido SET idCliente = %s,  idFuncionario = %s, formaPagamento = %s, dataPedido = %s WHERE idPedido = %s",  (cliente, funcionario, formadepgt, datapedido, idpedido))
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


def excluir_pedido():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select p.idpedido, p.idcliente, c.nomecliente from \"Projeto\".pedido p inner join \"Projeto\".cliente c ON p.idcliente = c.idcliente")
        lista_pedido = cursor.fetchall()
        print("Pedidos Registrados:")
        for idpedido, idcliente, nomecliente in lista_pedido:
            print(f"ID: {idpedido} | CLIENTE: {idcliente} - {nomecliente}")
        idpedido = int(input("Digite o id do pedido: "))
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o pedido {idpedido}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".tbl_detalhe_pedidos WHERE idpedido = %s', (idpedido,))
            cursor.execute('DELETE FROM \"Projeto\".pedido WHERE idpedido = %s', (idpedido,))
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
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def econtrar_por_nome():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        nomecliente = input("Digite o nome do cliente: ").strip()
        if not nomecliente:
            print("Nome do cliente não pode estar vazio.")
            return False
        cursor.execute("Select p.idpedido, p.idcliente, c.nomecliente, p.formapagamento, p.valortotal from \"Projeto\".pedido p join \"Projeto\".cliente c ON p.idcliente = c.idcliente where TRIM(LOWER(c.nomecliente)) ilike %s",(f"%{nomecliente}%",))
        pedidos_cliente = cursor.fetchall()

        if pedidos_cliente:
            print("Pedidos encontrados:")
            for pedido in pedidos_cliente:
                print(f"ID Pedido: {pedido[0]}, Nome Cliente: {pedido[2]}, Forma de Pagamento: {pedido[3]}, Valor Total: {pedido[4]}")
        else:
            print("Nenhum pedido encontrado para o cliente especificado.")
            return False
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()
     