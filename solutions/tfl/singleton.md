 

👨‍🏫 **Singleton: The Bank Manager and the Vault**

Imagine a **bank** in a busy city.

* The bank has **one main vault** where all the money is stored.
* No matter how many bank branches or staff you have, there is **only one vault** — it’s **centralized**, **consistent**, and **secure**.

Now, in programming, sometimes you want a class to behave like this **single vault**:

* Only **one instance** exists.
* All parts of your application **share this single instance**.
* This is called the **Singleton Pattern**.



### 🐍 Python Essentials — Singleton Pattern

A **Singleton** ensures that **no matter how many times you try to create an object**, you always get **the same instance

### 🔹 Classic Example: Bank Vault

```python
class BankVault:
    __instance = None  # private class variable to hold single instance

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            print("Creating the vault...")
            cls.__instance = super(BankVault, cls).__new__(cls)
        return cls.__instance

    def __init__(self):
        self.balance = 1000000  # initial money in vault

# Trying to create multiple vaults
vault1 = BankVault()
vault2 = BankVault()

print(vault1 == vault2)  # True, same instance
print(vault1.balance)    # 1000000
vault2.balance += 50000
print(vault1.balance)    # 1050000, reflects change in both
```

✅ Key Points:

1. `__instance` keeps track of the single instance.
2. `__new__` ensures that **if an instance exists, it’s returned**, otherwise a new one is created.
3. Every “vault” in the system **shares the same balance**, just like a real bank vault.



### 🔹 Mentor Analogy:

* **Multiple branches** of a bank = multiple places in code trying to create an object.
* **Vault** = Singleton object.
* **Money inside vault** = shared state across all code locations.

Without Singleton → **each branch could have its own vault**, leading to **inconsistency**.
With Singleton → **one vault is shared**, safe and consistent.

---

### 🔹 Quick Pythonic Singleton (Decorator Style)

```python
def singleton(cls):
    instances = {}
    def get_instance(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
        return instances[cls]
    return get_instance

@singleton
class Logger:
    def __init__(self):
        self.logs = []

log1 = Logger()
log2 = Logger()

log1.logs.append("System started")
print(log2.logs)  # ['System started'], same instance
```

---

✨ **Mentor Wisdom:**

* Use **Singleton** for resources that must be **shared globally**, like:

  * Logger systems
  * Database connections
  * Configuration managers
  * Cache managers

* Avoid using Singleton for objects that **need independent state**, otherwise you risk **unexpected side effects**.

