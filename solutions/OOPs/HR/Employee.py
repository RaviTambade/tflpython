#   class
#    methods (behaviors)
#    constructors, getter , setter, and other operations

class Employee:


    def __init__(self, name, position, workingdays, dailywages):
        self.name = name
        self.position = position
        self.workingdays =workingdays
        self.dailywages=dailywages

    def computePay(self):
        return self.dailywages * self.workingdays
    
    
    def display_info(self):
        print(f"Name: {self.name}\nPosition: {self.position}\n")

    def getName(self):
        return self.name
    def setName(self, name):
        self.name = name

    def getPosition(self):
        return self.position

    def setPosition(self, position):
        self.position = position
    
    def getWorkingdays(self):
        return self.workingdays
    def setWorkingdays(self, workingdays):
        self.workingdays = workingdays
    
    def getDailywages(self):
        return self.dailywages

    def setDailywages(self, dailywages):
        self.dailywages = dailywages


# Example usage for getting and setting attributes

emp1= Employee("John Doe", "Developer", 22, 300)
emp1.display_info()
emp1.setName("Ravi Tambade")
emp1.display_info()

fullName=emp1.getName()
print(fullName)
