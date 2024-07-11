#!/usr/bin/python3
"""
 - Private instance attribute: `width`:
      - property `def width(self):` to retrieve it
      - property setter `def width(self, value):` to set it:
          - `width` must be an integer, otherwise raise a `TypeError`
          exception with the message 'width must be an integer'
          - if `width` is less than `0`, raise a `ValueError` exception
          with the message 'width must be >= 0'
  - Private instance attribute: `height`:
      - property `def height(self):` to retrieve it
      - property setter `def height(self, value):` to set it:
          - `height` must be an integer, otherwise raise a `TypeError`
          exception with the message 'height must be an integer'
          - if `height` is less than `0`, raise a `ValueError` exception
          with the message 'height must be >= 0'
  - Public class attribute: `number_of_instances`:
      - initialized to `0`
      - incremented during each new instance instantiation
      - decremented during each instance deletion
  - Instantiation with optional `width` and `height`: `def __init__(self,
      width=0, height=0):`
  - Public instance method: `def area(self):` that returns the rectangle
  area
  - Public instance method: `def perimeter(self):` that returns the
  rectangle perimeter:
      - if `width` or `height` is equal to `0`, perimeter has to be equal
      to `0`
  -`print()` and `str()` should print the rectangle with the character `#`
      - if `width` or `height` is equal to `0`, return an empty string
  - repr() should return a string representation of the rectangle to be able
  to recreate a new instance by using eval() (see example below)
    - Print the message Bye rectangle... (... being 3 dots not ellipsis)
    when an instance of Rectangle is deleted

  - You are not allowed to import any module
  """


class Rectangle:
    """Representation of a rectangle"""

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializes the rectangle"""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
        """getter for the private instance attribute height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for the private instance attribute height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self) -> int:
        """returns the area of the rectangle"""
        return self.width * self.height

    def perimeter(self) -> int:
        """returns the perimeter of the rectangle"""
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * (self.width + self.height)

    def print_rectangle(self):
        """returns the printable string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            print("")
        else:
            for h in range(self.height):
                for w in range(self.width):
                    print("#", end="")
                print("\n")

    def __str__(self) -> str:
        """String representation of an object for readers"""
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

    def __repr__(self) -> str:
        """string representation of an object for developers"""
        # return f"Rectangle({self.width}, {self.height})"
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        """prints a delete message when object is destroyed"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
