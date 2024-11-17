class Product:
    def __init__(self, product_id: int, product_name: str, product_price: float, id_category: int, product_stripe: str): ##Stripe = Tarja
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.id_category = id_category
        self.product_stripe = product_stripe