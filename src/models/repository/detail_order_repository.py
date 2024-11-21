from src.models.entities.detail_order import DetailOrder
from src.models.connections.db import create_connection

class DetailOrderRepository:
    def __init__(self):
        self.connection = create_connection()
    
    def report_all_details_orders(self):
        query = 'SELECT * FROM \"pharma\".details_orders'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        details_orders = [DetailOrder(*[row[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]) for row in rows]
        return details_orders
    
    def find_details_orders_by_order_id(self, order_id):
        query = 'SELECT * FROM \"pharma\".details_orders WHERE order_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (order_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            row_sorted = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])  
            return DetailOrder(*row_sorted)
        else:
            return None
    
    def add_detail_order(self, detail_order):
        query = '''
            INSERT INTO \"pharma\".details_orders (order_id, product_id, quantity)
            VALUES (%s, %s, %s)
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (detail_order.order_id, detail_order.product_id, detail_order.quantity))
        self.connection.commit()
        cursor.close()

    def edit_detail_order(self, detail_order):
        query = '''
            UPDATE \"pharma\".details_orders
            SET order_id = %s, product_id = %s, quantity = %s
            WHERE detail_order_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (detail_order.order_id, detail_order.product_id, detail_order.quantity, detail_order.detail_order_id))
        self.connection.commit()
        cursor.close()

    def delete_detail_order(self, detail_order_id):
        query = 'DELETE FROM \"pharma\".details_orders WHERE detail_order_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (detail_order_id,))
        self.connection.commit()
        cursor.close()
    
