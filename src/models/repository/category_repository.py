from src.models.entities.category import Category
from src.models.connections.db import create_connection

class CategoryRepository:
    def __init__(self):
        self.connection = create_connection()
    
    def report_all_categories(self):
        query = 'SELECT * FROM \"pharma\".categories'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        
        categories = [Category(*row) for row in rows]
        return categories
    
    def find_category_by_id(self, category_id):
        query = 'SELECT * FROM \"pharma\".categories WHERE category_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (category_id,))
        row = cursor.fetchone()
        cursor.close()

        return Category(*row) if row else None
    
    def registry_category(self, category):
        query = '''
            INSERT INTO \"pharma\".categories (category_name, description)
            VALUES(%s, %s)
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (category.category_name, category.description))
        self.connection.commit()
        cursor.close()

    def update_category(self, category):
        query = '''
            UPDATE \"pharma\".categories
            SET category_name = %s, description = %s
            WHERE category_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (category.category_name, category.description, category.category_id))
        self.connection.commit()
        cursor.close()

    def delete_category(self, category_id):
        query = 'DELETE FROM \"pharma\".categories WHERE category_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (category_id,))
        self.connection.commit()
        cursor.close()