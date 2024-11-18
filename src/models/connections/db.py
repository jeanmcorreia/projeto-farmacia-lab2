import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname= 'postgres',
            user= 'postgres',
            password= '021122',
            host= '127.0.0.1',
            port= '5432'
        )
        
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
    
create_connection()