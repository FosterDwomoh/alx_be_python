# bank_account.py
class BankAccount:
    def__init__(self, initial_balance=0):
        self.account_balance = initial_balance
        def deposit(self,amount):
            self.amount_balance += amount
        def withdraw(self, amount):
            if self.account_balance >=amount:
                self.account_balance -= amount
                return True
            selse:
                return False
            def display_balance(self):
                print(f"Current Balance: ${self.account_balance:.2f}")
