
class BankAccount:
    def __init__(self, account_number: int, owner: str, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a number greater than zero.")

        self.balance += amount
        print(f"{self.owner} deposited ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Please enter a number greater than zero.")

        if amount > self.balance:
            raise ValueError("Insufficient funds.")

        self.balance -= amount
        print(f"New balance: ${self.balance:.2f}")

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


account = BankAccount(1223245, "Kelly")
account.run_menu()














# print(account.owner)
# print(account.account_number)
# print(account.deposit(int(input("Enter your deposit: "))))