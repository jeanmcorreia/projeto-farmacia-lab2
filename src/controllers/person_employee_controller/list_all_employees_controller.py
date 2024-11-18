from src.models.repository.person_employee_repository import PersonEmployeeRepository

def list_all_employees_controller():
    repository_employees = PersonEmployeeRepository()
    try:
        employees = repository_employees.report_all_employees()
        return employees
    except Exception as e:
        print(f'Ocorreu um erro {e}')