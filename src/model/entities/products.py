class Product:
    def __init__(self, id: int, name: str, price: float, category: int, stripe: str): ##Stripe = Tarja
        self.id = id
        self.name = name
        self.price = price
        self.category = category
        self.stripe = stripe