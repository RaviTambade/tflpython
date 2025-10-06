class Student:
    def __init__(self, name):
        self.name = name  # Stored in heap

def handler():
    temp = 10  # Stored in stack
    obj = Student("Ravi Tambade")  # Object created in heap
    return temp

result = handler()
print(result)