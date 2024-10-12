import psycopg2
from config.db import criar_conexao

def criar_produto(nome, preco, categoria, tarja): #CREATE
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute('SELECT * FROM \"Projeto\".categoria WHERE idcategoria = %s', (categoria,))
        categoria_existente = cursor.fetchone()

        if categoria_existente:
            try:
                cursor.execute('SELECT * FROM \"Projeto\".produto WHERE nomeproduto = %s', (nome,))
                produto_existente = cursor.fetchone()

                if produto_existente:
                    print(f"Produto {nome} já existe!")
                    return False
                else:
                    cursor.execute("INSERT INTO \"Projeto\".produto (nomeproduto, preco, idcategoria, tarja) VALUES (%s, %s, %s, %s)", (nome, preco, categoria, tarja))
                    conexao.commit()
                    print(f"Produto {nome} criado com sucesso!")
                    return True
            except (Exception, psycopg2.DatabaseError) as error:
                print(f"Erro ao acessar o banco de dados: {error}")
                return False 

            finally:
                cursor.close()
                conexao.close()
        else:
            try:
                criar = input("A categoria não existe, deseja adicioná-la? (S/N): ").upper()
                
                if criar == "S":
                    descricao = input("Digite o nome da categoria: ")
                    obs = input("Digite exemplos de produtos que se enquadrem nessa categoria: ")
                    cursor.execute("INSERT INTO \"Projeto\".categoria (descricao, obs) VALUES (%s, %s)", (descricao, obs))
                    conexao.commit()
                    print(f"Categoria {descricao} criada com sucesso!")
                    return True
                
                elif criar == "N":
                    print("Programa Encerrado")
                    return False

                else:
                    print("Opção inválida, tente novamente.")
                    return False
            except (Exception, psycopg2.DatabaseError) as error:
                print(f"Erro ao acessar o banco de dados: {error}")
                return False 

            finally:
                cursor.close()
                conexao.close()
    
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
        print(relatorio)
        
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
        cursor.execute('UPDATE \"Projeto\".produto SET nomeproduto = %s, preco = %s, idcategoria = %s, tarja = %s WHERE idproduto = %s', (novo_nome, novo_preco, nova_categoria, nova_tarja, idProduto))
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
        cursor.close()
        conexao.close()