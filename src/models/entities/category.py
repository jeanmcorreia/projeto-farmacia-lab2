class Category:
    def __init__(self, category_name: str, description: str, category_id: int = None):
        self.category_id = category_id
        self.category_name = category_name
        self.description = description

    def __repr__(self):
        return (f"Category(id={self.category_id}, name='{self.category_name}', description='{self.description}')")
    

# Teste de entidade
if __name__ == "__main__":
    category = Category(
        category_name="Medicamentos",
        description="Remédios"
    )

    print(category)

# Sucesso
