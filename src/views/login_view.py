def introduction_page():
    message = '''
        Bem-vindo!
        
        Caso usuário novo ou esqueceu a senha, peça seu acesso ao TI/Administrador do seu estabelecimento.
    '''

    print(message)
    username = input('Digite seu usuario: ')
    password = input('Digite sua senha: ')

    return {"username": username, "password": password}