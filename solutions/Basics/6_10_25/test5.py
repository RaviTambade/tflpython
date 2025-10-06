
class Employee:
    def __init__(self, name, salary,contactnumber): # constructor
        self.name = name                #instance variables (member Variable)
        self.salary = salary
        self.contactnumber=contactnumber

    def showDetails(self):      #Member functions
        print(f" Full Name: {self.name}  salary: {self.salary} Contact Number: {self.contactnumber}" )

    def spendMoney(self, amount):
        self.salary=self.salary-amount


# Objet has state and behaviour and identity
e1 = Employee("Seeta", 50000,"9773456892")  # object is constructed using Class

e2= Employee("Sonam Wangchuk","780000","9565464564")   # orphan, unrefernced object
e2= Employee("Shakrukh Khan",788000,"855683454")

e1.spendMoney(5000)
e1.showDetails()

e2.spendMoney(2000)
e2.showDetails()




