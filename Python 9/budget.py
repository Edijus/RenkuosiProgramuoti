from revenue_record import RevenueRecord
from expense_record import ExpenseRecord


class Budget:
    def __init__(self):
        self.book = []

    def add_revenue_record(self, amount: float, sender: str = '', additional_information: str = ''):
        record = RevenueRecord(amount, sender, additional_information)
        self.book.append(record)

    def add_expense_record(self, amount: float, payment_type: str = '', product: str = ''):
        record = ExpenseRecord(amount, payment_type, product)
        self.book.append(record)

    def show_balance(self):
        balance = 0
        for record in self.book:
            if isinstance(record, RevenueRecord):
                balance += record.amount
            elif isinstance(record, ExpenseRecord):
                balance -= record.amount

        print(balance)

    def show_report(self):
        for record in self.book:
            print(record)
