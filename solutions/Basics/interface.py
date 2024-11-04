"""
Using abstract base classes is a powerful way to define interfaces in Python.
It allows you to enforce a contract for subclasses 
while providing flexibility in how they implement the required methods.
"""

from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Example usage
if __name__ == "__main__":
    shapes = [
        Circle(5),
        Rectangle(4, 6)
    ]

    for shape in shapes:
        print(f"Area: {shape.area()}")
        print(f"Perimeter: {shape.perimeter()}")
