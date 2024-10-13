import math

class Shape:
    def area(self):
        """Method to calculate the area. Should be overridden in subclasses."""
        raise NotImplementedError("This method should be overridden by subclasses")


class Rectangle(Shape):
    def __init__(self, length, width):
        """Initialize Rectangle with length and width."""
        self.length = length
        self.width = width

    def area(self):
        """Override area method to calculate the area of the rectangle."""
        return self.length * self.width


class Circle(Shape):
    def __init__(self, radius):
        """Initialize Circle with radius."""
        self.radius = radius

    def area(self):
        """Override area method to calculate the area of the circle."""
        return math.pi * (self.radius ** 2)

# This file contains the definitions of Shape, Rectangle, and Circle classes.