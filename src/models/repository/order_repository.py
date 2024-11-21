from src.models.entities.order import Order
from src.models.connections.db import create_connection

class OrderRepository:
    def __init__(self):
        self.connection = create_connection()
    
    def report_all_orders(self):
        query = 'SELECT * FROM \"pharma\".orders'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        orders = [Order(*[row[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]) for row in rows]
        return orders
    
    def find_order_by_id(self, order_id):
        query = 'SELECT * FROM \"pharma\".orders WHERE order_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (order_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            row_sorted = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])  
            return Order(*row_sorted)
        else:
            return None
    
    def registry_order(self, order):
        query = '''
            INSERT INTO \"pharma\".orders (employee_id, client_id, order_payment_method, total_value, order_date)
            VALUES (%s, %s, %s, %s, %s)
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (order.employee_id, order.client_id, order.order_payment_method, order.total_value, order.order_date))
        self.connection.commit()
        cursor.close()

    def update_order(self, order):
        query = '''
            UPDATE \"pharma\".orders
            SET (employee_id = %s, client_id = %s, order_payment_method = %s, total_value = %s, order_date = %s)
            WHERE order_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (order.employee_id, order.client_id, order.order_payment_method, order.total_value, order.order_date, order.order_id))
        self.connection.commit()
        cursor.close()

    def delete_order(self, order_id):
        query = 'DELETE FROM \"pharma\".orders WHERE order_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (order_id,))
        self.connection.commit()
        cursor.close()
    