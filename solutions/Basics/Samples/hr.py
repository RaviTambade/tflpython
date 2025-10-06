class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        return f"Hi, I'm {self.name} and I'm {self.age} years old."

class Employee(Person):
    def __init__(self, name, age, employee_id):
        super().__init__(name, age)  # Call the constructor of the Person class
        self.employee_id = employee_id

    def work(self):
        return f"{self.name} is working."

class SalesEmployee(Employee):
    def __init__(self, name, age, employee_id, sales_target):
        super().__init__(name, age, employee_id)  # Call the constructor of the Employee class
        self.sales_target = sales_target

    def sell(self):
        return f"{self.name} is selling products to meet the sales target of {self.sales_target}."

# Example usage
if __name__ == "__main__":
    person = Person("Aarush", 14)
    print(person.introduce())  # Output: Hi, I'm Alice and I'm 30 years old.

    employee = Employee("Rahul", 25, "E543")
    print(employee.introduce())  # Output: Hi, I'm Rahul and I'm 25 years old.
    print(employee.work())        # Output: Rahul is working.

    sales_employee = SalesEmployee("Swapnil", 28, "E896", 200000)
    print(sales_employee.introduce())  # Output: Hi, I'm Swapnil and I'm 28 years old.
    print(sales_employee.work())         # Output: Charlie is working.
    print(sales_employee.sell())         # Output: Charlie is selling products to meet the sales target of 100000.
