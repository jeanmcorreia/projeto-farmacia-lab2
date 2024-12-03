import psycopg2
from config.db import criar_conexao

def criar_produto(): 
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        nome = input("Digite o nome do produto: ")
        preco = input("digite o valor do produto: ")
        tarja = input("Digite a tarja do Produto(caso possua): ")
        quantidade = input("Digite a quantidade de produto em estoque: ")
        cursor.execute("select idcategoria, descricao from \"Projeto\".categoria")
        lista_categorias = cursor.fetchall()
        for idcategoria, descricao in lista_categorias:
            print(f"ID: {idcategoria} | Nome: {descricao}")
        categoria = input("Digite o id da categoria do produto: ")
        cursor.execute("select idcategoria from \"Projeto\".categoria where idcategoria = %s",(categoria,))
        categoria_existe = cursor.fetchone()
        if not categoria_existe:
            print("Categoria não existe, operação cancelada.")
            return False
        else:
            try:
                cursor.execute('SELECT * FROM \"Projeto\".produto WHERE nomeproduto = %s', (nome,))
                produto_existente = cursor.fetchone()

                if produto_existente:
                    print(f"Produto {nome} já existe!")
                    return False
                else:
                    cursor.execute("INSERT INTO \"Projeto\".produto (nomeproduto, preco, idcategoria, tarja, quantidade) VALUES (%s, %s, %s, %s, %s)", (nome, preco, categoria, tarja, quantidade))
                    conexao.commit()
                    print(f"Produto {nome} criado com sucesso!")
                    return True
            except (Exception, psycopg2.DatabaseError) as error:
                print(f"Erro ao acessar o banco de dados: {error}")
                return False 

            finally:
                if cursor:
                    cursor.close()
                if conexao:
                    conexao.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
            if cursor:
                cursor.close()
            if conexao:
                conexao.close()

def relatorio_produtos(): 
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idproduto, nomeproduto from \"Projeto\".produto ")
        listaprod = cursor.fetchall()
        print("Produtos disponíveis:")
        for idproduto, nomeproduto in listaprod:
            print(f"ID: {idproduto} | Nome: {nomeproduto}")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def atualizar_produto():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idproduto, nomeproduto, preco, quantidade from \"Projeto\".produto")
        lista_produtos = cursor.fetchall()
        print("Produtos Registrados:")
        for idproduto, nomeproduto, preco, quantidade in lista_produtos:
            print(f"ID: {idproduto} | Nome: {nomeproduto} | Preço: {preco} | Quantidade: {quantidade}")
        idProduto = int(input("Digite o id do produto: "))
        novo_nome = input("Digite o nome do atualizado produto: ")
        novo_preco = float(input("digite o valor atualizado do produto: "))
        nova_categoria = input("Digite o id atualizado da categoria do produto: ")
        nova_tarja = input("Digite a tarja atualizado do produto(caso tenha): ")
        cursor.execute('UPDATE \"Projeto\".produto SET nomeproduto = %s, preco = %s, idcategoria = %s, tarja = %s WHERE idproduto = %s', (novo_nome, novo_preco, nova_categoria, nova_tarja, idProduto))
        conexao.commit()
        print(f"Produto {idProduto} atualizado com sucesso!")
        return True
    
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def excluir_produto():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idproduto, nomeproduto, preco, quantidade from \"Projeto\".produto")
        lista_produtos = cursor.fetchall()
        print("Produtos Registrados:")
        for idproduto, nomeproduto, preco, quantidade in lista_produtos:
            print(f"ID: {idproduto} | Nome: {nomeproduto} | Preço: {preco} | Quantidade: {quantidade}")
        idProduto = int(input("Digite o id do produto: "))
        idProduto = int(input("Digite o id do produto: "))
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o produto {idProduto}? (Isso excluirá o produto permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".produto WHERE idproduto = %s', (idProduto,))
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
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()