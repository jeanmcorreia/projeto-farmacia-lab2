from src.models.entities.products import Product
from src.models.connections.db import create_connection

class ProductRepository:
    def __init__(self):
        self.connection = create_connection()
    
    def report_all_products(self):
        query = 'SELECT * FROM \"pharma\".products'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()

        products = [Product(*[row[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]) for row in rows]
        return products
    
    def find_product_by_id(self, product_id):
        query = 'SELECT * FROM \"pharma\".products WHERE product_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (product_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            row_sorted = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])  
            return Product(*row_sorted)
        else:
            return None
    
    def create_product(self, product):
        query = '''
            INSERT INTO \"pharma\".products (product_name, product_price, quantity_stock, category_id, product_stripe)
            VALUES (%s, %s, %s, %s, %s)   
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (product.product_name, product.product_price, product.quantity_stock, product.category_id, product.product_stripe))
        self.connection.commit()
        cursor.close()

    def update_product(self, product):
        query = '''
            UPDATE \"pharma\".products
            SET product_name = %s, product_price = %s, quantity_stock = %s, category_id = %s, product_stripe = %s
            WHERE product_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (product.product_name, product.product_price, product.quantity_stock, product.category_id, product.product_stripe, product.product_id))
        self.connection.commit()
        cursor.close()

    def delete_product(self, product_id):
        query = 'DELETE FROM \"pharma\".products WHERE product_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (product_id,))
        self.connection.commit()
        cursor.close()

    