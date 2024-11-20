class DetailOrder:
    def __init__(self, order_id: int, product_id: int, quantity: int, detail_order_id: int = None):
        self.detail_order_id = detail_order_id
        self.order_id = order_id
        self.product_id = product_id
        self.quantity = quantity

    def __repr__(self):
        return(f"DetailOrder(id={self.detail_order_id}, order_id={self.order_id}, product={self.product_id}, quantity={self.quantity})")
    
if __name__ == "__main__":
    detail = DetailOrder(
        order_id=1,
        product_id=2,
        quantity=3
    )

    print(detail)

# Sucesso