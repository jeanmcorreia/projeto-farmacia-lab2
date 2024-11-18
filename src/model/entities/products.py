class Product:
    def __init__(self, product_id: int, product_name: str, product_price: float, category_id: int, product_stripe: str): ##Stripe = Tarja
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.category_id= category_id
        self.product_stripe = product_stripe