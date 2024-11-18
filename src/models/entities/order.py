class Order:
    def __init__(self, order_id: int, employee_id: int, client_id: int, order_payment_method: str, total_value: float, order_date):
        self.order_id = order_id
        self.employee_id = employee_id
        self.client_id = client_id
        self.order_payment_method = order_payment_method
        self.total_value = total_value
        self.order_date = order_date
