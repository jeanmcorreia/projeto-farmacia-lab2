from src.models.entities.person_employee import PersonEmployee
from src.models.repository.person_employee_repository import PersonEmployeeRepository

repository = PersonEmployeeRepository()

# Teste 1: Listar todos os funcionários
print("----- Lista de Todos os Funcionários -----")
employees = repository.report_all_employees()
for emp in employees:
    print(vars(emp))

# Teste 2: Encontrar funcionário por ID
print("\n----- Buscar Funcionário por ID -----")
employee_id = 1
employee = repository.find_employee_by_id(employee_id)
if employee:
    print(vars(employee))
else:
    print(f"Funcionário com ID {employee_id} não encontrado.")

# Teste 3: Registrar um novo funcionário
print("\n----- Registrar Novo Funcionário -----")
new_employee = PersonEmployee(
    employee_id=None,
    employee_name="Teste Novo",
    employee_cpf=12345678901,
    employee_address="Rua de Teste",
    employee_telephone=987654321,
    employee_level_permission=1,
    employee_password=1314,
    employee_admission_date="2024-11-20"
)
repository.registry_employee(new_employee)
print("Funcionário registrado com sucesso!")

# Teste 4: Atualizar funcionário
print("\n----- Atualizar Funcionário -----")
employee_to_update = repository.find_employee_by_id(employee_id)
if employee_to_update:
    employee_to_update.employee_name = "Nome Atualizado"
    repository.update_employee(employee_to_update)
    print(f"Funcionário com ID {employee_id} atualizado!")
else:
    print(f"Funcionário com ID {employee_id} não encontrado para atualizar.")

# Teste 5: Deletar funcionário
print("\n----- Deletar Funcionário -----")
repository.delete_employee(employee_id)
print(f"Funcionário com ID {employee_id} deletado!")
