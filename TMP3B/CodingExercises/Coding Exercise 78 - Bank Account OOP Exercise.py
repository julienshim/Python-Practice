# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, deposit):
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):
        self.balance -= withdraw
        return self.balance

    def balance(self):
        return self.balance
