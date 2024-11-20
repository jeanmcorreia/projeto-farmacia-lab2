class PersonClient:
    def __init__(self, client_name: str, client_cpf: str, client_address: str, client_telephone: str, client_registration_date: str, client_id: int = None):
        self.client_id = client_id
        self.client_name = client_name
        self.client_cpf = client_cpf
        self.client_address = client_address
        self.client_telephone = client_telephone
        self.client_registration_date = client_registration_date

    def __repr__(self):
        return (f"PersonClient("
                f"id={self.client_id}, name='{self.client_name}', cpf='{self.client_cpf}', "
                f"address='{self.client_address}', telephone='{self.client_telephone}', "
                f"registration='{self.client_registration_date}'")
    

# Teste de entidade
if __name__ == "__main__":
    client = PersonClient(
        client_name="Kaua",
        client_cpf="52364846524",
        client_address="Rua do Cabare",
        client_telephone="84623569485",
        client_registration_date="2024-11-20"
    )

    print(client)