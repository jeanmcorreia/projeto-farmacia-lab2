from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_clientes, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionarios, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produto, relatorio_produtos, atualizar_produto, excluir_produto
from estoque.crud_estoque import gerar_estoque, relatorio_estoque, editar_estoque, excluir_lote
from pedidos.crud_pedidos import gerar_pedido, relatorio_pedidos, editar_pedido, excluir_pedido



            
def menu_opcoes():
    while True:
        print("\nMenu de Opções:")
        print("1 - Pessoas")
        print("2 - Estoque")
        print("3 - Produtos")
        print("4 - Pedidos")
        print("0 - Sair")

        try:
            opcao = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Digite um número inteiro válido.")
            continue
        
        if opcao == 0:
            print("Sistema encerrado!")
            break
        elif opcao == 1:
            while True:
                print("\nEscolha uma opção:")
                print("1 - Clientes")
                print("2 - Funcionários")
                print("0 - Voltar")
                try:
                    opcao_pessoas = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Digite um número inteiro válido.")
                    continue
                if opcao_pessoas == 1:
                    while True:
                        print("\nEscolha uma opção:")
                        print("1 - Criar cliente")
                        print("2 - Relatório cliente")
                        print("3 - Editar cliente")
                        print("4 - Excluir cliente")
                        print("0 - Voltar")
                        try:
                            opcao_cliente = int(input("Digite a opção desejada: "))
                        except ValueError:
                            print("Digite um número inteiro válido.")
                            continue
                        if opcao_cliente == 1:
                            nomeC = input("Digite o nome do cliente: ")
                            cpfC = input("Digite o cpf do cliente: ")
                            EnderecoC = input("Digite o endereço do cliente: ")
                            celularC = input("Digite o numero de celular do cliente: ")
                            dataCadC = input("Digite a data que o cliente está sendo cadastrado: ")
                            criar_cliente(nomeC, cpfC, EnderecoC, celularC, dataCadC)
                        elif opcao_cliente == 2:   
                            relatorio_clientes()
                        elif opcao_cliente == 3:
                            idC = int(input("Digite o id do cliente: "))
                            nomeC = input("Digite o nome atualizado do cliente: ")
                            cpfC = input("Digite o cpf atualizado do cliente: ")
                            EnderecoC = input("Digite o endereço atualizado do cliente: ")
                            celularC = input("Digite o numero de celular atualizado do cliente: ")
                            dataCadC = input("Digite a data que o cliente foi cadastrado atualizada: ")
                            editar_cliente(idC, nomeC, cpfC, EnderecoC, celularC, dataCadC)
                        elif opcao_cliente == 4:
                            idC = int(input("Digite o id do cliente que deseja excluir: "))
                            excluir_cliente(idC)
                        elif opcao_cliente == 0:
                            break
                        else:
                            print("Escolha uma opção válida.")
                elif opcao_pessoas == 2:
                    while True:
                        print("\nEscolha uma opção:")
                        print("1 - Criar funcionário")
                        print("2 - Relatório funcionário")
                        print("3 - Editar funcionário")
                        print("4 - Excluir funcionário")
                        print("0 - Voltar")
                        try:
                            opcao_funcionario = int(input("Digite a opção desejada: "))
                        except ValueError:
                            print("Digite um número inteiro válido.")
                            continue
                        if opcao_funcionario == 1:
                            nomeF = input("Digite o nome do funcionario: ")
                            cpfF = input("Digite o cpf do funcionario: ")
                            EnderecoF = input("Digite o endereço do funcionario: ")
                            CelularF = input("Digite o celular do funcionario: ")
                            dataCadF = input("Digite a data que o funcionario está sendo cadastrado: ")
                            criar_funcionario(nomeF, cpfF, EnderecoF, CelularF, dataCadF)
                        elif opcao_funcionario == 2:
                            relatorio_funcionarios()
                        elif opcao_funcionario == 3:
                            idf = int(input("Digite o id do funcionario: "))
                            nomeF = input("Digite o nome atualizado do funcionario: ")
                            cpfF = input("Digite o cpf atualizado do funcionario: ")
                            EnderecoF = input("Digite o endereço atualizado do funcionario: ")
                            CelularF = input("Digite o celular atualizado do funcionário: ")
                            dataCadF = input("Digite a data que o funcionario foi cadastrado atualizada: ")
                            editar_funcionario(idf, nomeF, cpfF, EnderecoF, CelularF, dataCadF)
                        elif opcao_funcionario == 4:
                            idf = int(input("Digite o id do funcionario: "))
                            excluir_funcionario(idf)
                        elif opcao_funcionario == 0:
                            break
                        else:
                            print("Escolha uma opção válida.")
                elif opcao_pessoas == 0:
                    break
                else:
                    print("Escolha uma opção válida!")

        elif opcao == 2:
            while True:
                print("\nEscolha uma opção:")
                print("1 - Gerar estoque")
                print("2 - Relatório estoque")
                print("3 - Editar estoque")
                print("4 - Excluir estoque")
                print("0 - Voltar")
                try:
                    opcao_estoque = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Digite um número inteiro válido.")
                    continue
                if opcao_estoque == 1:
                    idE = int(input("Digite o id do lote: "))
                    idprodutoE = int(input("Digite o id do produto contindo no lote: "))
                    quantidadeE = int(input("Digite a quantidade do produto contindo no lote: "))
                    validadeE = input("Digite a data de validade desse lote: ")
                    gerar_estoque(idE, idprodutoE, quantidadeE, validadeE)
                elif opcao_estoque == 2:
                    relatorio_estoque()
                elif opcao_estoque == 3:
                    idE = int(input("Digite o id do lote: "))
                    idprodutoE = int(input("Digite o id atualizado do produto contindo no lote: "))
                    quantidadeE = int(input("Digite a quantidade atualizada do produto contindo no lote: "))
                    validadeE = input("Digite a data atualizada de validade desse lote: ")
                    editar_estoque(idE, idprodutoE, quantidadeE, validadeE)
                elif opcao_estoque == 4:
                    idE = int(input("Digite o id do lote: "))
                    excluir_lote(idE)
                elif opcao_estoque == 0:
                    break
                else:
                    print("Digite uma opção válida!")
        elif opcao == 3:
            while True:
                print("\nEscolha uma opção:")
                print("1 - Criar produto")
                print("2 - Relatório produto")
                print("3 - Editar produto")
                print("4 - Excluir produto")
                print("0 - Voltar")
                try:
                    opcao_produto = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Digite um número inteiro válido.")
                    continue
                if opcao_produto == 1:
                    nomeP = input("Digite o nome do produto: ")
                    precoP = input("digite o valor do produto: ")
                    categoriaP = input("Digite o id da categoria do produto: ")
                    tarjaP = input("Digite a tarja do produto(caso tenha): ")
                    criar_produto(nomeP, precoP, categoriaP, tarjaP)
                elif opcao_produto == 2:
                    relatorio_produtos()
                elif opcao_produto == 3:
                    idP = int(input("Digite o id do produto: "))
                    nomeP = input("Digite o nome do atualizado produto: ")
                    precoP = float(input("digite o valor atualizado do produto: "))
                    categoriaP = input("Digite o id atualizado da categoria do produto: ")
                    tarjaP = input("Digite a tarja atualizado do produto(caso tenha): ")
                    atualizar_produto(idP, nomeP, precoP, categoriaP, tarjaP)
                elif opcao_produto == 4:
                    idP = int(input("Digite o id do produto: "))
                    excluir_produto(idP)
                elif opcao_produto == 0:
                    break
                else:
                    print("Digite uma opção válida!")
        elif opcao == 4:
            while True:
                print("\nEscolha uma opção:")
                print("1 - Gerar pedido")
                print("2 - Relatório pedidos")
                print("3 - Editar pedido")
                print("4 - Excluir pedido")
                print("0 - Voltar")
                try:
                    opcao_pedido = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Digite um número inteiro válido.")
                    continue
                if opcao_pedido == 1:
                    ClientePE = int(input("Digite o id do cliente que fez o pedido: "))
                    FuncPe = int(input("Digite o id do funcionario responsável pelo pedido: "))
                    FormadePgtPE = input("digite a forma de pagamento: ")
                    DataPE = input("Digite a data que o pedido esta sendo efetuado: ")
                    gerar_pedido(ClientePE, FuncPe, FormadePgtPE, DataPE)
                elif opcao_pedido == 2:
                    relatorio_pedidos()
                    
                elif opcao_pedido == 3:
                    idPE = int(input("Digite o id do pedido: "))
                    ClientePE = int(input("Digite o id atualizado do cliente que fez o pedido: "))
                    FuncPe = int(input("Digite o nome atualizado do funcionario responsável pelo pedido: "))
                    FormadePgtPE = input("digite a forma de pagamento atualizada: ")
                    DataPE = input("Digite a data atualizada que o pedido foi efetuado: ")
                    editar_pedido()
                elif opcao_pedido == 4:
                    idPE = int(input("Digite o id do pedido: "))
                    excluir_pedido(idPE)
                elif opcao_pedido == 0:
                    break
                else:
                    print("Digite uma opção válida!")
        else:
            print("Digite uma opção válida.")
    
def main():
    while True:
        print("Seja Bem Vindo !:\n1 - Login\n2 - Cadastro")
        
        try:
            OpcEnter = int(input("Digite a opção desejada: "))
        except ValueError:
            print("Entrada inválida! Por favor, insira um número (1 para Login ou 2 para Cadastro).")
            continue  
        
        while OpcEnter != 1 and OpcEnter != 2:
            try:
                OpcEnter = int(input("Opção inválida! Digite 1 para Login ou 2 para Cadastro: "))
            except ValueError:
                print("Entrada inválida! Por favor, insira um número (1 ou 2).")
                continue  

        if OpcEnter == 2:  
            Login = input("Digite seu user: ")
            Senha = input("Digite sua senha: ")
            while not cadastrar(Login, Senha):
                print("Erro ao cadastrar. Tente novamente.")
                Login = input("Digite o user desejado: ")
                Senha = input("Digite a senha desejada: ")
            print("Cadastro realizado com sucesso!")
            print("Voltando para a tela de login...")
            continue  

        elif OpcEnter == 1:  
            Login = input("Digite seu user: ")
            Senha = input("Digite sua senha: ")
            while not autenticar(Login, Senha):
                print("Usuário ou senha incorretos. Tente novamente.")
                Login = input("Digite seu user: ")
                Senha = input("Digite sua senha: ")
            print("Login realizado com sucesso!")
            break
    menu_opcoes()

if __name__ == "__main__":
    main()
