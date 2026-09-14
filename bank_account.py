class BankAccount:
    def __init__(self, account_number: int, owner: str, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def run_menu(self):
        while True:
            print(f"\n--- {self.owner}'s Bank Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            try:
                if choice == "1":
                    print(f"Current Balance: ${self.balance:.2f}")

                elif choice == "2":
                    amount = float(input("Enter deposit amount: "))
                    self.deposit(amount)

                elif choice == "3":
                    amount = float(input("Enter withdrawal amount: "))
                    self.withdraw(amount)

                elif choice == "4":
                    print("Exited")
                    break

                else:
                    print("Invalid selection.")

            except ValueError as e:
                print(f"Error: {e}")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a number greater than zero.")

        self.balance += amount
        print(
            f"{self.owner} deposited ${amount:.2f}. "
            f"New balance: ${self.balance:.2f}"
        )

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a number greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        print(f"New balance: ${self.balance:.2f}")

    def __str__(self):
        return (
            f"Account Number: {self.account_number}, "
            f"Owner: {self.owner}, "
            f"Balance: ${self.balance:.2f}"
        )


class SavingsAccount(BankAccount):
    def __init__(self, account_number, owner, balance, interest_rate):
        super().__init__(account_number, owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        self.balance += interest

    def __str__(self):
        return (
            f"{super().__str__()}, "
            f"Interest Rate: {self.interest_rate}%"
        )

account = SavingsAccount(1223245, "Kelly", 1000, 5)

print(account)

account.deposit(200)
print(account)

account.withdraw(100)
print(account)

account.apply_interest()
print(account)
