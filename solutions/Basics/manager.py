# Python program to show that the varaibles with a value
# assigned  in class declaration, are class variables and 
# variables inside methods and constructors are instance variables

#Class for Computer Science Student

import math
class MathManager:

    #Class Variables
    stream ='cse'

    #The init method or constructor
    def __init__(self, roll):

        # Instance variables
        self.roll=roll

    def calculateDistance(x1,y1,x2,y2):  
     dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     print(dist)
     return dist  

    def calc(x1,y1,x2,y2):  
     self.dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
     return dist  

# Objects of CSS
a=MathManager(101)
b=MathManager(102)

print(a.stream)
print(a.roll)
print(b.roll)

print(a.calc(10,100,300,67))

