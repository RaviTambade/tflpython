
# Attributes

"""
    Reflection in Python refers 
    to the ability of a program to inspect and 
    modify its own structure and behavior at runtime. 
    This can include accessing attributes, methods, and 
    other properties of an object dynamically.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old."

# Example usage of reflection
if __name__ == "__main__":
    person = Person("Chaitanya", 23)

    # Inspecting the attributes and methods of the person instance
    print("Attributes of person:")
    for attribute in dir(person):
        if not attribute.startswith("__"):  # Skip built-in attributes
            print(attribute)

    # Accessing attributes dynamically


    name_attr = 'name'
    age_attr = 'age'
    print(f"\nAccessing attributes dynamically:")
    print(f"Name: {getattr(person, name_attr)}")
    print(f"Age: {getattr(person, age_attr)}")

    # Calling a method dynamically
    method_name = 'greet'
    greet_message = getattr(person, method_name)()  # Call greet() method
    print(f"\nMethod call using reflection: {greet_message}")

    # Adding a new attribute dynamically
    setattr(person, 'location', 'Wonderland')
    print(f"\nNew attribute 'location' added: {getattr(person, 'location')}")
