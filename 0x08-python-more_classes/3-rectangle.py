#!/usr/bin/python3
"""
 class `Rectangle` that defines a rectangle
"""


class Rectangle:
    """Representation of a rectangle"""

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """getter for the private instance attribute width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """getter for the private instance attribute width"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute width"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def print(self):
        """returns the printable string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for h in range(self.height):
                for w in range(self.width):
                    print("#", end="")
                print("\n")

    def __str__(self):
        rectangle_str = ""
        if self.width == 0 or self.height == 0:
            return rectangle_str
        else:
            for row in range(self.height):
                rect_row = "#" * self.width
                rectangle_str += rect_row
                if row < self.height - 1:
                    rectangle_str += "\n"
            return rectangle_str
