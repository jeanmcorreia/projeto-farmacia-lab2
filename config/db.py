import psycopg2

def criar_conexao():
    try:
        conn = psycopg2.connect(
            dbname= 'postgres',
            user= 'postgres',
            password= '021122',
            host= 'localhost',
            port= '5432'
        )
        
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
criar_conexao()