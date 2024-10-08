def autenticar(login, senha):
    usuarios = [
        {
            "username": "teste",
            "password": "admin"
        },
        {
            "username": "teste2",
            "password": "admin2"
        },
        {
            "username": "teste3",
            "password": "admin3"
        },
        {
            "username": "teste4",
            "password": "admin4"
        }
    ]
    for usuario in usuarios:
        if usuario["username"] == login and usuario["password"] == senha:
            return True
    
    return False

user = "teste"
pw = "admin"
autenticar(user, pw)