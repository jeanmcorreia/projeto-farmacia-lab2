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
        print("1 - Criar Cliente")
        print("2 - Relatório de Clientes")
        print("3 - Editar Cliente")
        print("4 - Excluir Cliente")
        print("5 - Criar Funcionário")
        print("6 - Relatório de Funcionários")
        print("7 - Editar Funcionário")
        print("8 - Excluir Funcionário")
        print("9 - Criar Produto")
        print("10 - Relatório de Produtos")
        print("11 - Atualizar Produto")
        print("12 - Excluir Produto")
        print("13 - Gerar Estoque")
        print("14 - Relatório de Estoque")
        print("15 - Editar Estoque")
        print("16 - Excluir Lote")
        print("17 - Gerar Pedido")
        print("18 - Relatório de Pedidos")
        print("19 - Editar Pedido")
        print("20 - Excluir Pedido")
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
            criar_cliente()
        elif opcao == 2:
            relatorio_clientes()
        elif opcao == 3:
            editar_cliente()
        elif opcao == 4:
            excluir_cliente()
        elif opcao == 5:
            criar_funcionario()
        elif opcao == 6:
            relatorio_funcionarios()
        elif opcao == 7:
            editar_funcionario()
        elif opcao == 8:
            excluir_funcionario()
        elif opcao == 9:
            criar_produto()
        elif opcao == 10:
            relatorio_produtos()
        elif opcao == 11:
            atualizar_produto()
        elif opcao == 12:
            excluir_produto()
        elif opcao == 13:
            gerar_estoque()
        elif opcao == 14:
            relatorio_estoque()
        elif opcao == 15:
            editar_estoque()
        elif opcao == 16:
            excluir_lote()
        elif opcao == 17:
            gerar_pedido()
        elif opcao == 18:
            relatorio_pedidos()
        elif opcao == 19:
            editar_pedido()
        elif opcao == 20:
            excluir_pedido()
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
