from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_clientes, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionarios, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produto, relatorio_produtos, atualizar_produto, excluir_produto
from estoque.crud_estoque import gerar_estoque, relatorio_estoque, editar_estoque, excluir_lote
from pedidos.crud_pedidos import gerar_pedido, relatorio_pedidos, editar_pedido, excluir_pedido

'''
print("Seja Bem Vindo !:\n1 - Login\n2 - Cadastro")
OpcEnter = int(input("Digite a opção desejada: "))
while OpcEnter != 1 and OpcEnter != 2:
    OpcEnter = int(input("Opção inválida! Digite a opção desejada (1 para Login ou 2 para Cadastro): "))

if OpcEnter == 2:
    Login = input("Digite seu user: ")
    Senha = input("Digite sua senha: ")
    while cadastrar(Login,Senha) != True:
        Login = input("Digite o user desejado: ")
        Senha = input("Digite a senha desejada: ")
        cadastrar(Login,Senha)
        if cadastrar(Login,Senha):
            break
'''
            
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
            print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
            continue
        
        if opcao == 0:
            print("Sistema encerrado! PF PROGRAME EM JAVA")
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
                    print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
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
                            print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
                            continue
                        if opcao_cliente == 1:
                            criar_cliente()
                        elif opcao_cliente == 2:
                            relatorio_clientes()
                        elif opcao_cliente == 3:
                            editar_cliente()
                        elif opcao_cliente == 4:
                            excluir_cliente()
                        elif opcao_cliente == 0:
                            break
                        else:
                            print("ESCOLHA UMA OPCAO VÁLIDA PHP DEVELOPER.")
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
                            print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
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
                            print("ESCOLHA UMA OPCAO VÁLIDA PHP DEVELOPER.")
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
                    print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
                    continue
                if opcao_estoque == 1:
                    gerar_estoque()
                elif opcao_estoque == 2:
                    relatorio_estoque()
                elif opcao_estoque == 3:
                    editar_estoque()
                elif opcao_estoque == 4:
                    excluir_lote()
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
                    print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
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
                    print("MEU AMIGO DIGITE UM NÚMERO VALIDO.")
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
            print("ESCOLHA UMA OPCAO VÁLIDA PHP DEVELOPER.")

def cadastro():
    while True:
        nome_usuario = input("Crie um nome de usuário: ")
        senha_usuario = input("Crie uma senha: ")
        if cadastrar(nome_usuario, senha_usuario):
            print("Cadastro realizado!")
            return
        else:
            print("Cadastro falhou.")

def login():
    login_usuario = input("Digite seu nome de usuário: ")
    senha_usuario = input("Digite sua senha de usuário: ")
    if autenticar(login_usuario, senha_usuario):
        return
    else:
        print("Senha ou usuário incorretos!")
    
def main():
    print("Seja Bem Vindo !:\n1 - Logar\n2 - Cadastrar")
    while True:
        try:
            opcao_main = int(input("Digite a opção desejada: "))
            while opcao_main != 1 and opcao_main != 2:
                opcao_main = int(input("Opção inválida! Digite a opção desejada (1 para Logar ou 2 para Cadastrar): "))
        except ValueError:
            print("Entrada inválida! Por favor, digite um número.")
            continue

        if opcao_main == 1:
            login()
            menu_opcoes()
            break
        elif opcao_main == 2:
            cadastro()
            menu_opcoes()
            break

if __name__ == "__main__":
    main()
