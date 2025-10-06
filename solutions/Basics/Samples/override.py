class Employee:        # define parent class
   def calculatePay(self):
      print ('Employee CalculatePay')

class WageEmployee(Employee): # define child class
   def calculatePay(self):
      print ('Wage Employee CalculatePay')

c = WageEmployee()          # instance of child
c.calculatePay()         # child calls overridden method