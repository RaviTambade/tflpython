class Stack:
    def __init__(self):
        self.items=[]
        se
    

    def push(self, num ):
        print("pushing data into stack")
        self.items.append(num)
    
    def pop(self):
        print("Popping data from stack")
        self.items.pop()

    
    def show(self):
        for item in self.items:
            print(item)


print("Hello Transflower")
stk=Stack()
stk.push(12)
stk.push(54)
stk.push(22)
stk.show()
stk.pop()
stk.pop()
stk.show()


