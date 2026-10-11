
class BankAccount:
    def __init__(self, owner: str, balance: int):

        # TODO: Reject negative balance
        if balance < 0:
            raise ValueError("Balance cannot be negetiv")

        # TODO: Initialize owner using its setter
        self.owner = owner

        # TODO: Initialize private-like balance
        self.__balance = balance
        pass

    @property
    def owner(self) -> str:
        # TODO: Return the owner's name
        return self.__owner 
        

    @owner.setter
    def owner(self, new_owner: str) -> None:
        # TODO: Reject empty or whitespace-only names
        if not new_owner.strip():
            raise ValueError("Name cannot be empty")
        # TODO: Update __owner if valid
        self.__owner = new_owner
        

    @property
    def balance(self) -> int:
        # TODO: Return the balance
        return self.__balance
        

    def deposit(self, amount: int) -> None:
        # TODO: Validate amount and deposit
        if amount <= 0:
            return print("Enter a positive amount to deposit")
        else:
            self.__balance += amount
        

    def withdraw(self, amount: int) -> None:
        # TODO: Validate amount and available funds
        if amount <= 0:
                return ("Enter a positive amount to withdraw")
        else:
            if amount > self.__balance:
                return print("You have insufficient funds")
            else:
                self.__balance -= amount
            
