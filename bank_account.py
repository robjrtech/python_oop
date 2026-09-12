
class BankAccount:
    def __init__(self, account_number: int, owner: str, balance=0):
        self.account_number = account_number
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        if amount < 0:
            raise ValueError("Please enter a number greater than zero.")
        else:
            print(f'{self.owner} deposited ${amount}. New balance: ${self.balance}')

    def withdraw(self, withdrawn):
        self.balance -= withdrawn
        if withdrawn > self.balance:
            raise ValueError("Insufficient funds")
        else:
            print(f'New balance: ${self.balance}')

    def run_menu(self):
        while True:
            print(f"\n---{self.owner}'s Bank Menu ---")
            print("1. Check Balance")
            print("2. Deposit Money")
            print("3. Withdraw Money")
            print("4. Exit")

            choice = input("Choose an option (1-4): ")

            if choice == "1":
                print(f"Current Balance: ${self.balance}")
            elif choice == "2":
                amt = float(input("Enter deposit amount: "))
                self.deposit(amt) 
            elif choice == "3":
                new_bal = float(input("Enter withdrawn amount: "))
                self.withdraw(new_bal)
            else:
                choice == "4"
                break
    
account = BankAccount(1223245, "Kelly")

account.run_menu()

# print(account.owner)
# print(account.account_number)
# print(account.deposit(int(input("Enter your deposit: "))))