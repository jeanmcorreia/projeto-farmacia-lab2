class PersonEmployee:
    def __init__(self, employee_name: str, employee_cpf: str, employee_address: str, employee_telephone: str,employee_permission_level: int, employee_password: str, employee_admission_date: str, employee_id: int = None):
        self.employee_id = employee_id
        self.employee_name = employee_name
        self.employee_cpf = employee_cpf
        self.employee_address = employee_address
        self.employee_telephone = employee_telephone
        self.employee_permission_level = employee_permission_level
        self.employee_password = employee_password
        self.employee_admission_date = employee_admission_date
    
    def __repr__(self):
        return (f"PersonEmployee("
                f"id={self.employee_id}, name='{self.employee_name}', cpf='{self.employee_cpf}', "
                f"address='{self.employee_address}', telephone='{self.employee_telephone}', "
                f"permission_level={self.employee_permission_level}, admission_date='{self.employee_admission_date}')")
    

# Teste da entidade
if __name__ == "__main__":
    employee = PersonEmployee(
        employee_name="admin",
        employee_cpf="12345678901",
        employee_address="Rua ABC, 123",
        employee_telephone="82912345678",
        employee_permission_level=2,
        employee_password="admin", 
        employee_admission_date="2024-11-20"
    )

    print(employee)

#SUCESSO!
        
    
    