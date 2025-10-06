class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner          # Public attribute
        self._balance = balance     # Protected attribute
        self.__transaction_count = 0  # Private attribute

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            self.__transaction_count += 1
            print(f"Deposited: ${amount}. New balance: ${self._balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount
            self.__transaction_count += 1
            print(f"Withdrew: ${amount}. New balance: ${self._balance}")
        else:
            print("Invalid withdrawal amount.")

    def get_balance(self):
        return self._balance

    def get_transaction_count(self):
        return self.__transaction_count

# Example usage
if __name__ == "__main__":
    
    account = Account("Sameera", 1000)

    account.deposit(500)
    account.withdraw(200)

    print(f"Current Balance: ${account.get_balance()}")
    print(f"Transaction Count: {account.get_transaction_count()}")

    # Accessing public and protected members
    print(f"Owner: {account.owner}")  # Public access
    print(f"Balance (protected): {account._balance}")  # Protected access (not recommended)
    
    # Trying to access private member (will raise an error)
    # print(account.__transaction_count)  # Uncommenting this will cause an AttributeError

"""
Encapsulation in Python helps protect the internal state of an object and 
ensures that only specific methods can modify its data. 
This leads to better control of the data and helps maintain the integrity of the object's state. 
"""