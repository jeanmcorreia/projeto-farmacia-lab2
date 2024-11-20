class Order:
    def __init__(self, employee_id: int, client_id: int, order_payment_method: str, total_value: float, order_date, order_id: int = None):
        self.order_id = order_id
        self.employee_id = employee_id
        self.client_id = client_id
        self.order_payment_method = order_payment_method
        self.total_value = total_value
        self.order_date = order_date

    def __repr__(self):
        return (f"Order(id={self.order_id}, employee={self.employee_id}, client={self.client_id}, paymethod='{self.order_payment_method}', total={self.total_value}, date='{self.order_date}')")
    
if __name__ == "__main__":
    order = Order(
        employee_id=1,
        client_id=2,
        order_payment_method='Cartão',
        total_value=2000.00,
        order_date='2024-11-20'
    )

    print(order)

# Sucesso
