from config.db import criar_conexao
from login.autenticar import autenticar


user = "admin"
pw = "admin123"
resultado = autenticar(user, pw)
if resultado:
    print("Usuário autenticado com sucesso!")
else:
    print("Falha na autenticação.")

