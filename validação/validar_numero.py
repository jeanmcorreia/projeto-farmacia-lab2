import re

def validar_numero(numero):
    padrao = r"^[0-9]{2}[9][0-9]{8}$"
    if re.match(padrao, numero):
        return True
    else:
        return False