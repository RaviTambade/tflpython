
from HR import Employee

class SalesEmployee(Employee):

    def __init__(self, name,position, workingDays,dailywages,incentive, targetAmount,totalSalesDone ):
        super().__init__(name,position, workingDays,dailywages)
        self.incentive = incentive 
        self.targetAmount=targetAmount
        self.totalSalesDone = totalSalesDone
        self.totalsalary=0



    def computePay(self):
        basicSalary=super().computePay()

        if self.totalSalesDone >= self.targetAmount:
            calculatedSalary= basicSalary+self.incentive
        else:
            calculatedSalary=basicSalary
        tax = 0.18 * calculatedSalary
        self.totalsalary=calculatedSalary-tax
        return self.totalsalary
        

    def display_info(self):
        super().display_info()
        print(f"total salary :{self.computePay()}")


        
