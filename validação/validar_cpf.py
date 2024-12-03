import re

def validar_cpf(cpf):
    padrao = r"^[0-9]{3}[0-9]{3}[0-9]{3}[-][0-9]{2}$"
    if re.match(padrao, cpf):
        return True
    else:
        return False