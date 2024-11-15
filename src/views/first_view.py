def introduction_page():
    message = '''
        Sistema Farmácia

        * Login - 1
        * Cadastrar novo usuário - 2
        * Sair - 5

    '''

    print(message)
    command = input('Comando: ')

    return command