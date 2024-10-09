from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar


user = "admin4"
pw = "admin4"
resultado = autenticar(user, pw)
if resultado:
    print("Usuário autenticado com sucesso!")
else:
    print("Falha na autenticação.")


resultado2 = cadastrar(user, pw)


