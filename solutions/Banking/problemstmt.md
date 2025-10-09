
## **Problem Statement: Bank Account Management System using Inheritance**

### **Objective:**

Design a Python program to simulate a bank account management system using **inheritance**. The system should support different types of accounts with specific behaviors while sharing common functionality from a base account class.

---

### **Requirements:**

1. **Create a Base Class: `BankAccount`**

   * Attributes:

     * `account_number` (int)
     * `account_holder` (string)
     * `balance` (float, default = 0)
   * Methods:

     * `deposit(amount)` → Adds money to the balance.
     * `withdraw(amount)` → Deducts money from the balance if sufficient funds exist.
     * `get_details()` → Returns account information (number, holder, balance).

2. **Create Derived Classes:**

   **a) `SavingAccount`**

   * Inherits from `BankAccount`.
   * Additional attribute: `interest_rate` (default 4%).
   * Additional method: `add_interest()` → Adds interest to the balance.

   **b) `CurrentAccount`**

   * Inherits from `BankAccount`.
   * Additional attribute: `overdraft_limit` (default 1000).
   * Override `withdraw(amount)` → Allow withdrawal up to balance + overdraft limit.

   **c) `FixedDeposit`**

   * Inherits from `BankAccount`.
   * Additional attributes: `tenure_years`, `interest_rate` (default 6%).
   * Additional method: `calculate_maturity_amount()` → Calculates and returns maturity amount using compound interest.

---

### **Tasks to Perform:**

1. Create instances of each account type.
2. Test deposit and withdrawal operations.
3. Test account-specific operations:

   * Add interest for savings account.
   * Handle overdraft in current account.
   * Calculate maturity for fixed deposit account.
4. Print account details after each operation.

---

### **Expected Learning Outcomes:**

* Understand **single inheritance** in Python.
* Practice **method overriding** in derived classes.
* Learn to **extend functionality** of a base class for specialized behaviors.
* Get hands-on experience with **encapsulation** of account data.

-