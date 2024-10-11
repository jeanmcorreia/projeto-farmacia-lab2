from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_cliente, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionario, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produtos, relatorio_produtos, editar_produtos, excluir_produtos
from estoque.crud_estoque import gerar_estoque, relatorio_estoque, editar_estoque, excluir_lote



user = "admin4"
pw = "admin4"
resultado = autenticar(user, pw)
if resultado:
    print("Usuário autenticado com sucesso!")
else:
    print("Falha na autenticação.")


resultado2 = cadastrar(user, pw)


