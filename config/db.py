import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='DBNAME',
            user='DB_USER',
            password= 'DB_PASSWORD',
            host= 'DB_HOST',
            port= 'DB_PORT'
        )
        print("Conexão realizada com sucesso!")
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
criar_conexao()