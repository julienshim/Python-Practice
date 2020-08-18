# Define Bank Account Below:
class BankAccount:
    def __init__(self, owner):
        self.owner = owner
        self.balance = 0.0

    def deposit(self, deposit):  # could have said "amount"
        self.balance += deposit
        return self.balance

    def withdraw(self, withdraw):  # could have said "amount"
        self.balance -= withdraw
        return self.balance

    def balance(self):  # why does the solution have "getBalance"
        return self.balance
