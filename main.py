from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_clientes, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionarios, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produto, relatorio_produtos, atualizar_produto, excluir_produto
from estoque.crud_estoque import relatorio_estoque, editar_estoque
from pedidos.crud_pedidos import gerar_pedido, relatorio_pedidos, editar_pedido, excluir_pedido
from validação.validar_acesso import validar_acesso



            
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
                            if validar_acesso() == '1':
                                criar_cliente()
                            else:
                                print("você não tem permissõa para realizar essa ação")
                                continue
                        elif opcao_cliente == 2:   
                            relatorio_clientes()
                        elif opcao_cliente == 3:
                            editar_cliente()
                        elif opcao_cliente == 4:                           
                            excluir_cliente()
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
                            criar_funcionario()
                        elif opcao_funcionario == 2:
                            relatorio_funcionarios()
                        elif opcao_funcionario == 3:                            
                            editar_funcionario()
                        elif opcao_funcionario == 4:                           
                            excluir_funcionario()
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
                print("1 - Editar estoque")
                print("2 - Relatório estoque")
                print("0 - Voltar")
                try:
                    opcao_estoque = int(input("Digite a opção desejada: "))
                except ValueError:
                    print("Digite um número inteiro válido.")
                    continue
                if opcao_estoque == 1:
                    editar_estoque()
                elif opcao_estoque == 2:
                    relatorio_estoque()
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
                    criar_produto()
                elif opcao_produto == 2:
                    relatorio_produtos()
                elif opcao_produto == 3:
                    atualizar_produto()
                elif opcao_produto == 4:                   
                    excluir_produto()
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
                    gerar_pedido()
                elif opcao_pedido == 2:
                    relatorio_pedidos()
                elif opcao_pedido == 3:
                    editar_pedido()
                elif opcao_pedido == 4:
                    excluir_pedido()
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
            if not cadastrar():
                print("Erro ao cadastrar. Tente novamente.")
                continue
            else:
                continue
                

        elif OpcEnter == 1:  
            if not autenticar():
                print("Usuário ou senha incorretos. Tente novamente.")
                continue
            else:
                break
                  
    menu_opcoes()

if __name__ == "__main__":
    main()
