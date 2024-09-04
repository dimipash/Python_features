"""
This code demonstrates the use of abstract base classes in Python.
Abstract base classes are used to define a common interface for a set of subclasses.
In this example, the Shape class is an abstract base class that defines a common interface for all shapes.
The Circle and Rectangle classes are concrete subclasses that implement the Shape interface.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculate the perimeter of the shape."""
        pass

    @abstractmethod
    def describe(self):
        """Return a description of the shape."""
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 2 * 3.14 * self.radius

    def describe(self):
        return f"Circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def describe(self):
        return f"Rectangle with width {self.width} and height {self.height}"


if __name__ == "__main__":
    # This would raise TypeError: Can't instantiate abstract class Shape with abstract methods area, describe, perimeter
    # shape = Shape()

    circle = Circle(5)
    print(circle.describe())
    print(f"Area: {circle.area():.2f}")
    print(f"Perimeter: {circle.perimeter():.2f}")

    print()

    rectangle = Rectangle(4, 6)
    print(rectangle.describe())
    print(f"Area: {rectangle.area()}")
    print(f"Perimeter: {rectangle.perimeter()}")

    print()

    # Demonstrating polymorphism
    shapes = [Circle(3), Rectangle(2, 5)]
    for shape in shapes:
        print(f"{shape.describe()}:")
        print(f"  Area: {shape.area():.2f}")
        print(f"  Perimeter: {shape.perimeter():.2f}")
