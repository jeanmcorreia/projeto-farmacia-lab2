class Product:
    def __init__(self, product_name: str, product_price: float, quantity_stock: int, category_id: int, product_stripe: str, product_id: int = None): ##Stripe = Tarja
        self.product_id = product_id
        self.product_name = product_name
        self.product_price = product_price
        self.quantity_stock = quantity_stock
        self.category_id= category_id
        self.product_stripe = product_stripe

    def __repr__(self):
        return(f"Product(id={self.product_id}, nome='{self.product_name}', price={self.product_price}, quantity_stock={self.quantity_stock}, category={self.category_id}, stripe='{self.product_stripe}')")
    

# Teste de entidades
if __name__ == "__main__":
    product = Product(
        product_name="Tadala",
        product_price=100.00,
        quantity_stock=10,
        category_id=4,
        product_stripe="Preta"
    )

    print(product)

#Sucesso