from bank_account import BankAccount


class SavingsAccount(BankAccount):
    def __init__(self, interest_rate):
        super().__init__(1223245, "Kelly")
        self.interest_rate = interest_rate

    def interest(self, interest_rate):
        interest_rate *= self.balance
        print(self.balance)
        print


savings = SavingsAccount(0.05)

print("annualized return: " )