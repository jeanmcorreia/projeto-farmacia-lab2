from typing import Dict
from src.models.repository.person_employee_repository import PersonEmployeeRepository
from src.models.entities.person_employee import PersonEmployee

class ReportPersonEmployeeController:
    def __init__(self):
        self.person_employee_repository = PersonEmployeeRepository()
    
    def report_all_employees(self, query_params: Dict) -> Dict:
        pass

    def __validate_fields(self):
        pass