from src.model.entities.person_client import PersonClient
from src.model.connections.db import create_connection

class PersonClientRepository:
    def __init__(self):
        self.connection = create_connection()

    def report_all_clients(self):
        query = 'SELECT * FROM \"pharma\".clients;'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        clients = [PersonClient(*row) for row in rows]
        return clients
    
    def find_client_by_id(self, client_id):
        query = 'SELECT * FROM \"pharma\".clients WHERE client_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (client_id,))
        row = cursor.fetchone()
        cursor.close()

        return PersonClient(*row) if row else None
    
    def registry_client(self, client):
        query = '''
            INSERT INTO \"pharma\".clients (client_name, client_cpf, client_address, client_telephone, client_registration_date)
            VALUES(%s, %s, %s, %s, %s)
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (client.client_name, client.client_cpf, client.client_address, client.client_telephone, client.client_registration_date))
        self.connection.commit()
        cursor.close()

    def update_client(self, client):
        query = '''
            UPDATE \"pharma\".client
            SET client_name = %s, client_cpf = %s, client_addess = %s, client_telephone = %s, client_registration_date = %s
            WHERE client_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (client.client_name, client.client_cpf, client.client_address, client.client_telephone, client.client_registration_date, client.client_id))
        self.connection.commit()
        cursor.close()

    def delete_client(self, client_id):
        query = 'DELETE FROM \"pharma\".clients WHERE client_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (client_id,))
        self.connection.commit()
        cursor.close()