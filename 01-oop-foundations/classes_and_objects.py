# Create a BankAccount class with the following requirements:
# Its constructor accepts owner and balance.
# It has a deposit(amount) method that increases the balance.
# It has a withdraw(amount) method that decreases the balance.
# It has a display_balance() method that prints the current balance.

class BankAccount:
    def __init__(self, owner:str, balance:int):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount:int) -> None:
        self.balance = self.balance + amount

    def withdraw(self, amount: int) -> None:
        self.balance = self.balance - amount

    def display_balance(self) -> None:
        print(f"Current Balance is: {self.balance}")


account = BankAccount("Alice", 1000)

account.deposit(500)
account.withdraw(200)
account.display_balance()
