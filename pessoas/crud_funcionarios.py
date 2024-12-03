from config.db import criar_conexao
from criptografar.cripto_senha import criptografar
from validação.validar_cpf import validar_cpf
from validação.validar_numero import validar_numero
import bcrypt
import psycopg2


def criar_funcionario():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        nome = input("Digite o nome do funcionario: ")
        usuario = input("Digite o usuário do funcionario: ")
        cpf = input("Digite o cpf do funcionario: ")
        if validar_cpf(cpf):
           print("CPF válido. Continuando...")
        else:
            print(f'cpf não está na formatação correta, exemplo: "123456789-10"')
            return False
        endereco = input("Digite o endereço do funcionario: ")
        celular = input("Digite o celular do funcionario: ")
        if validar_numero(celular):
           print("Numero válido. Continuando...")
        else:
            print(f'o número não está na formatação correta, exemplo: "ddd912345678"')
            return False
        senha = input("Digite a senha do usuário:")
        NivelPermissao = input("Digite o nivel de permissão: ")
        data_admissao = input("Digite a data que o funcionario está sendo cadastrado: ")
        cursor.execute("Select cpffuncionario from \"Projeto\".funcionario where cpffuncionario = %s", (cpf,))
        funcionario_existe = cursor.fetchone()
        if funcionario_existe:
            print(f"O Funcionario de cpf '{cpf}' já existe")
            return False
        else:
            senha_hash = criptografar(senha)
            cursor.execute("INSERT INTO \"Projeto\".funcionario(nomeFuncionario, UsuarioFuncionario, cpfFuncionario, enderecoFuncionario, celularFuncionario, SenhaFuncionario, NivelPermissao, admissao) values(%s, %s, %s, %s, %s, %s, %s, %s)", (nome, usuario, cpf, endereco, celular, senha_hash, NivelPermissao, data_admissao))
            conexao.commit()
            print(f"Funcionário criado com sucesso!")
            return True
    except Exception as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def relatorio_funcionarios():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario")
        listaFunc = cursor.fetchall()
        print("Funcionarios Registrados:")
        for idfuncionario, nomefuncionario in listaFunc:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario ")
        relatorio_funcionario = cursor.fetchall()
        print("Funcionarios:")
        for idfuncionario, nomefuncionario in relatorio_funcionario:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False 

    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def editar_funcionario():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario")
        listaFunc = cursor.fetchall()
        print("Funcionarios Registrados:")
        for idfuncionario, nomefuncionario in listaFunc:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        id = int(input("Digite o id do funcionario: "))
        nome = input("Digite o nome atualizado do funcionario: ")
        usuario = input("Digite o usuario atualizado do funcionario: ")
        cpf = input("Digite o cpf atualizado do funcionario: ")
        if validar_cpf(cpf):
           print("CPF válido. Continuando...")
        else:
            print(f'cpf não está na formatação correta, exemplo: "123456789-10"')
            return False
        endereco = input("Digite o endereço atualizado do funcionario: ")
        celular = input("Digite o celular atualizado do funcionário: ")
        if validar_numero(celular):
           print("Numero válido. Continuando...")
        else:
            print(f'o número não está na formatação correta, exemplo: "ddd912345678"')
            return False
        senha = input("Digite a senha atualizada do funcionario: ")
        NivelPermissao = input("Digite o nivel de permissão atualizado do funcionario: ")
        data_admissao = input("Digite a data que o funcionario foi cadastrado atualizada: ")
        cursor.execute("SELECT * FROM \"Projeto\".funcionario where idFuncionario = %s", (id,))
        func_existe = cursor.fetchone()
        
        if func_existe:
            cursor.execute("Select cpffuncionario from \"Projeto\".funcionario where cpffuncionario = %s", (cpf,))
            funcionario_igual = cursor.fetchone()
            if funcionario_igual:
                print(f"O funcionario de cpf '{cpf}' já existe")
                return False
            
            else:
                cursor.execute("Select UsuarioFuncionario from \"Projeto\".funcionario where UsuarioFuncionario = %s", (usuario,))
                user_igual = cursor.fetchone()
                if user_igual:
                    print(f"Um funcionario já está usando o nome de user: '{usuario}'")
                    return False
                else:
                    senha_update_hash = criptografar(senha)
                    cursor.execute("UPDATE \"Projeto\".funcionario SET nomefuncionario = %s, UsuarioFuncionario = %s, cpffuncionario = %s, enderecofuncionario = %s, celularfuncionario = %s, SenhaFuncionario = %s, NivelPermissao = %s, admissao = %s WHERE idFuncionario = %s", (nome, usuario, cpf, endereco, celular, senha_update_hash, NivelPermissao, data_admissao, id))
                    conexao.commit()
                    print(f"Funcionário com ID {id} atualizado com sucesso.")
                    return True
            
        else:
            print("Falha na Alteração, Funcionario não existe")
            return False 
         
    except (Exception, psycopg2.DatabaseError) as error:
        print(f"Erro ao acessar o banco de dados: {error}")
        return False
        
    finally:
        if cursor:
            cursor.close()
        if conexao:
            conexao.close()

def excluir_funcionario():
    try:
        conexao = criar_conexao()
        cursor = conexao.cursor()
        cursor.execute("Select idfuncionario, nomefuncionario from \"Projeto\".funcionario")
        listaFunc = cursor.fetchall()
        print("Funcionarios Registrados:")
        for idfuncionario, nomefuncionario in listaFunc:
            print(f"ID: {idfuncionario} | Nome: {nomefuncionario}")
        idfuncionario = int(input("Digite o id do funcionario: "))
        confirmar_exclusao = input(f"Você tem certeza que quer excluir o funcionario {idfuncionario}? (Isso o excluirá permanentemente!)\nS/N").upper()

        if confirmar_exclusao == "S":
            cursor.execute('DELETE FROM \"Projeto\".funcionario WHERE idfuncionario = %s', (idfuncionario,))
            conexao.commit()
            print(f"Funcionario de id: {idfuncionario} excluído.")
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
     