import customtkinter as ctk
from config.db import criar_conexao
from login.autenticar import autenticar
from login.cadastrar import cadastrar
from pessoas.crud_clientes import criar_cliente, relatorio_clientes, editar_cliente, excluir_cliente
from pessoas.crud_funcionarios import criar_funcionario, relatorio_funcionarios, editar_funcionario, excluir_funcionario
from produtos.crud_produtos import criar_produto, relatorio_produtos, atualizar_produto, excluir_produto
from estoque.crud_estoque import gerar_estoque, relatorio_estoque, editar_estoque, excluir_lote
from pedidos.crud_pedidos import gerar_pedido, relatorio_pedidos, editar_pedido, excluir_pedido


def menu_pessoas():
    pass

def menu_estoque():
    pass 

def menu_produtos():
    pass

def menu_pedidos():
    pass 

def menu_principal():
    main_menu = ctk.CTk()
    main_menu.title("Sistema de Farmácia")
    main_menu.geometry("500x400")

    ctk.CTkLabel(main_menu, text="Menu de Opções", font=("Arial", 18)).pack(pady=10)

    ctk.CTkButton(main_menu, text="Gerenciar Pessoas", command=menu_pessoas, width=200).pack(pady=5)
    ctk.CTkButton(main_menu, text="Gerenciar Estoque", command=menu_estoque, width=200).pack(pady=5)
    ctk.CTkButton(main_menu, text="Gerenciar Produtos", command=menu_produtos, width=200).pack(pady=5)
    ctk.CTkButton(main_menu, text="Gerenciar Pedidos", command=menu_pedidos, width=200).pack(pady=5)
    ctk.CTkButton(main_menu, text="Sair", command=main_menu.quit, width=200).pack(pady=20)

    main_menu.mainloop()

def login():
    login_window = ctk.CTk()
    login_window.title("Tela de Login")
    login_window.geometry("400x300")

    def login():
        user = entry_user.get()
        password = entry_password.get()
        if autenticar(user, password):
            login_window.destroy()
            menu_principal()
        else:
            ctk.CTkLabel(login_window, text="Usuário ou senha incorretos.", text_color="red").pack(pady=5)

    def register():
        user = entry_user.get()
        password = entry_password.get()
        if cadastrar(user, password):
            ctk.CTkLabel(login_window, text="Cadastro realizado com sucesso!", text_color="green").pack(pady=5)
        else:
            ctk.CTkLabel(login_window, text="Erro ao cadastrar. Tente novamente.", text_color="red").pack(pady=5)

    ctk.CTkLabel(login_window, text="Sistema de Farmácia", font=("Arial", 20)).pack(pady=10)

    ctk.CTkLabel(login_window, text="Usuário").pack()
    entry_user = ctk.CTkEntry(login_window, width=250)
    entry_user.pack(pady=5)


    ctk.CTkLabel(login_window, text="Senha").pack()
    entry_password = ctk.CTkEntry(login_window, show="*", width=250)
    entry_password.pack(pady=5)

    ctk.CTkButton(login_window, text="Login", command=login, width=200).pack(pady=10)
    ctk.CTkButton(login_window, text="Cadastrar", command=register, width=200).pack(pady=5)

    login_window.mainloop()

if __name__ == "__main__":
    login()