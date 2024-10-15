import customtkinter as ctk
from login.autenticar import autenticar

def autenticar_usuario():
    login_usuario = entry_username.get()
    senha_usuario = entry_password.get()

    if autenticar(login_usuario, senha_usuario):
        label_feedback.configure(text="Login bem-sucedido!", text_color="green")
    else:
        label_feedback.configure(text="Usuário ou senha incorretos", text_color="red")

app = ctk.CTk()
app.geometry("400x300")
app.title("Tela de Login")

frame_login = ctk.CTkFrame(master=app)
frame_login.pack(padx=20, pady=20)

label_username = ctk.CTkLabel(master=frame_login, text="Usuário")
label_username.pack(pady=5)

entry_username = ctk.CTkEntry(master=frame_login)
entry_username.pack(pady=5)

label_password = ctk.CTkLabel(master=frame_login, text="Senha")
label_password.pack(pady=5)

entry_password = ctk.CTkEntry(master=frame_login, show="*")
entry_password.pack(pady=5)

label_feedback = ctk.CTkLabel(master=frame_login, text="")
label_feedback.pack(pady=5)

button_login = ctk.CTkButton(master=frame_login, text="Login", command=autenticar_usuario)
button_login.pack(pady=10)

app.mainloop()

#esta dando erro Erro ao acessar o banco de dados: ERRO:  relação "Projeto.usuario" não existe
#LINE 1: SELECT usuario, password FROM "Projeto".usuario