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
        
        categories = [Category(*[row[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]) for row in rows]
        return categories
    
    def find_category_by_id(self, category_id):
        query = 'SELECT * FROM \"pharma\".categories WHERE category_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (category_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            row_sorted = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])  
            return Category(*row_sorted)
        else:
            return None
    
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