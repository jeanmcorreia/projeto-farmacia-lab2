from config.db import criar_conexao
import bcrypt
import psycopg2

def criptografar (senha):
    bytes = senha.encode('utf-8')
    hashed = bcrypt.hashpw(bytes, bcrypt.gensalt(14))
    return hashed