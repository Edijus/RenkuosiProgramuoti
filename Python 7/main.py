class Record:
    def __init__(self, amount: float):
        self.amount = amount

#    def __str__(self): # record = Record('Pajamos', 12) print(record) -> converts to human-readable format
#        return f'{self._type} {self.amount}'


class RevenueRecord(Record):
    def __init__(self, amount: float, sender: str, additional_information: str):
        super().__init__(amount)
        self.sender = sender
        self.additional_information = additional_information

    def __str__(self):
        return f'Revenue {self.amount}; Sender: {self.sender}; Add. Information: {self.additional_information}'


class ExpenseRecord(Record):
    def __init__(self, amount: float, payment_type: str, product: str):
        super().__init__(amount)
        self.payment_type = payment_type
        self.product = product

    def __str__(self):
        return f'Expense {self.amount}; Payment type: {self.payment_type}; Product: {self.product}'


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
                balance = balance + record.amount
            elif isinstance(record, ExpenseRecord):
                balance = balance - record.amount

        print(balance)

    def show_report(self):
        for record in self.book:
            print(record)


budget = Budget()

while True:
    action = int(input(' 1 - Add revenue record\n 2 - Add expense record\n 3 - Show balance\n 4 - Show report\n 5 - Exit '))
    if action == 1:
        amount = float(input('Enter amount:'))
        sender = input('Sender:')
        additional_information = input('Additional information:')
        budget.add_revenue_record(amount, sender, additional_information)
    elif action == 2:
        amount = float(input('Enter amount:'))
        payment_type = input('Payment type:')
        product = input('Product:')
        budget.add_expense_record(amount, payment_type, product)
    elif action == 3:
        budget.show_balance()
    elif action == 4:
        budget.show_report()
    elif action == 5:
        print('Bye')
        break
