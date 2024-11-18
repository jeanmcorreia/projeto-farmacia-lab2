class Product:
    def __init__(self, product_id: int, product_name: str, product_price: float, quantity_stock: int, category_id: int, product_stripe: str): ##Stripe = Tarja
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.quantity_stock = quantity_stock
        self.category_id= category_id
        self.product_stripe = product_stripe