import psycopg2

def create_connection():
    try:
        conn = psycopg2.connect(
            dbname= 'postgres',
            user= 'postgres',
            password= 'Kako021122',
            host= 'localhost',
            port= '5432'
        )
        
        return conn
    except Exception as e:
        print(f"Erro ao conectar com o banco de dados: {e}")
        return None
    
# Teste da conexão
if __name__ == "__main__":
    connection = create_connection()
    if connection:
        connection.close()
        print("Conexão fechada com sucesso.")
#SUCESSO