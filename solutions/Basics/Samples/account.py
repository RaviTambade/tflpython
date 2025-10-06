class  Account:
    def __init__(self, balance):
        self._balance = balance  # Protected attribute

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance

account =  Account(100)
account.deposit(50)
print(account.get_balance())  # Output: 150
