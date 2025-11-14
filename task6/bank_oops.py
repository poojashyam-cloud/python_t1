class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited Rs {amount}. New balance: Rs {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew Rs {amount}. New balance: Rs {self.balance}")

    def display_balance(self):
        print(f"{self.owner}'s account balance: Rs {self.balance}")

account1 = BankAccount("pooja", 10000)
account1.display_balance()  # account balance: 100
account1.deposit(500)        # Deposited 50. New balance: 150
account1.withdraw(30)       # Withdrew 30. New balance: 120
account1.withdraw(200)      # Insufficient funds.

class SavingsAccount(BankAccount):
    def __init__(self, owner, balance=0, interest_rate=0.02):
        super().__init__(owner, balance)
        self.interest_rate = interest_rate

    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        print(f"Interest applied: Rs{interest:.2f}. New balance: Rs{self.balance:.2f}")
savings = SavingsAccount("shyam", 1000)
savings.display_balance()    # shyam's account balance: 1000
savings.apply_interest()     # Interest applied: rs20.00. New balance: 1020.00