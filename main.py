from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_clientes, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionarios, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produto, relatorio_produtos, atualizar_produto, excluir_produto
from estoque.crud_estoque import gerar_estoque, relatorio_estoque, editar_estoque, excluir_lote
from pedidos.crud_pedidos import gerar_pedido, relatorio_pedidos, editar_pedido, excluir_pedido

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
