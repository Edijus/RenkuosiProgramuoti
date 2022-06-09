from record import Record


class RevenueRecord(Record):
    def __init__(self, amount: float, sender: str, additional_information: str):
        super().__init__(amount)
        self.sender = sender
        self.additional_information = additional_information

    def __str__(self):
        return f'Revenue {self.amount}; Sender: {self.sender}; Add. Information: {self.additional_information}'
