from .constructor.introduction_process import introduction_process


def start() -> None:
    while True:
        command = introduction_process()

        if command == '1': print('Login')
        elif command == '2': print('Cadastrar')
        elif command == '5': exit()
        else: print('\n Digite um comando válido! \n\n')