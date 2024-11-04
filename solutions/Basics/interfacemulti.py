from abc import ABC, abstractmethod
import math

class Drawable(ABC):
    @abstractmethod
    def draw(self):
        pass

class Resizable(ABC):
    @abstractmethod
    def resize(self, factor):
        pass

class Circle(Drawable, Resizable):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def perimeter(self):
        return 2 * math.pi * self.radius

    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")

    def resize(self, factor):
        self.radius *= factor
        print(f"Resized circle to radius {self.radius}")

# Example usage
if __name__ == "__main__":
    circle = Circle(5)

    circle.draw()  # Drawing the circle
    print(f"Area: {circle.area()}")          # Area calculation
    print(f"Perimeter: {circle.perimeter()}")  # Perimeter calculation

    circle.resize(2)  # Resize the circle
    circle.draw()      # Draw the resized circle
