# A Sample class with init method
class Person:
    # init method or constructor
    def __init__(self, firstName,lastName):
        self.firstName=firstName
        self.lastName=lastName
    
    def __del__(self):
        print('Destructor called, vehicle deleted.')

    # sample Method
    def say_hi(self):
        print('Hello, my name is', self.firstName, self.lastName)


p=Person('Ravi','Tambade')
p.say_hi()
del p   //
p