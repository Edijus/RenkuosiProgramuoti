from record import Record


class ExpenseRecord(Record):
    def __init__(self, amount: float, payment_type: str, product: str):
        super().__init__(amount)
        self.payment_type = payment_type
        self.product = product

    def __str__(self):
        return f'Expense {self.amount}; Payment type: {self.payment_type}; Product: {self.product}'
