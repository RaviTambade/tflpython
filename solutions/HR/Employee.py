

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
        
