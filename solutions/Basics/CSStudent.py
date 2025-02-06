# Python program to show that the varaibles with a value
# assigned  in class declaration, are class variables and 
# variables inside methods and constructors are instance variables

#Class for Computer Science Student

class CSStudent:

    #Class Variables
    stream ='cse'

    #The init method or constructorcd ocd 
    def __init__(self, roll):

        # Instance variables
        self.roll=roll
# Objects of CSS
a=CSStudent(101)
b=CSStudent(102)

print(a.stream)
print(a.roll)
print(b.roll)
print(b.stream)
