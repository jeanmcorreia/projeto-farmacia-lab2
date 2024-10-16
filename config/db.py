import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()


def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv('DBNAME'),
            user=os.getenv('DB_USER'),
            password= os.getenv('DB_PASSWORD'),
            host= os.getenv('DB_HOST'),
            port= os.getenv('DB_PORT')
        )
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
criar_conexao()