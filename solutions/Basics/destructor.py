class Manager:
    def __init__(self, name):
        self.name = name
        print(f"{self.name} has been created.")

    def __del__(self):
        print(f"{self.name} is being destroyed.")

# Example usage
obj = Manager("Object1")
del obj  # This will call the destructor
