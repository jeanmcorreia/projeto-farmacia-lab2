from src.models.connections.db import create_connection
from src.models.entities.person_employee import PersonEmployee

class PersonEmployeeRepository:
    def __init__(self):
        self.connection = create_connection()

    def report_all_employees(self):
        query = 'SELECT * FROM \"pharma\".employees'
        cursor = self.connection.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        
        employees = [PersonEmployee(*[row[i] for i in [1, 2, 3, 4, 5, 6, 7, 0]]) for row in rows]
        return employees
    
    def find_employee_by_id(self, employee_id):
        query = 'SELECT  * FROM \"pharma\".employees WHERE employee_id = %s;'
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id,))
        row = cursor.fetchone()
        cursor.close()

        if row:
            row_sorted = (row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[0])  
            return PersonEmployee(*row_sorted)
        else:
            return None
    
    def registry_employee(self, employee):
        query = '''
            INSERT INTO \"pharma\".employees (employee_name, employee_cpf, employee_address, employee_telephone, employee_level_permission, employee_password, employee_admission_date)
            VALUES(%s, %s, %s, %s, %s, %s, %s)
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (employee.employee_name, employee.employee_cpf, employee.employee_address, employee.employee_telephone, employee.employee_level_permission, employee.employee_password, employee.employee_admission_date))
        self.connection.commit()
        cursor.close()

    def update_employee(self, employee):
        query = '''
            UPDATE \"pharma\".employees 
            SET employee_name = %s, employee_cpf = %s, employee_address = %s, employee_telephone = %s, employee_level_permission = %s, employee_password = %s, employee_admission_date = %s
            WHERE employee_id = %s
        '''
        cursor = self.connection.cursor()
        cursor.execute(query, (employee.employee_name, employee.employee_cpf, employee.employee_address, employee.employee_telephone, employee.employee_level_permission, employee.employee_password, employee.employee_admission_date, employee.employee_id))
        self.connection.commit()
        cursor.close()

    def delete_employee(self, employee_id):
        query = 'DELETE FROM \"pharma\".employees WHERE employee_id = %s'
        cursor = self.connection.cursor()
        cursor.execute(query, (employee_id,))
        self.connection.commit()
        cursor.close()

