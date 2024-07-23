#!/usr/bin/python3
from .base import Base


class Rectangle(Base):
    """
    Represents a rectangle that inherits from the Base class.
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
                Initializes a new Rectangle instance.
        pass
                Args:
                    width (int): The width of the rectangle.
                    height (int): The height of the rectangle.
                    x (int, optional): The x-coordinate of the rectangle.
                    Defaults to 0.
                    y (int, optional): The y-coordinate of the rectangle.
                    Defaults to 0.
                    id (int, optional): The ID of the rectangle.
                    Defaults to None.
        """
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
        Base.__init__(self, id)

    @property
    def width(self):
        """
                Getter for the width of the rectangle.
        pass
                Returns:
                    int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
                Setter for the width of the rectangle.
        pass
                Args:
                    value (int): The new width of the rectangle.
        """
        self.__width = value

    @property
    def height(self):
        """
                Getter for the height of the rectangle.
        pass
                Returns:
                    int: The height of the rectangle.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
                Setter for the height of the rectangle.
        pass
                Args:
                    value (int): The new height of the rectangle.
        """
        self.__height = value

    @property
    def x(self):
        """
                Getter for the x-coordinate of the rectangle.
        pass
                Returns:
                    int: The x-coordinate of the rectangle.
        """
        return self.__x

    @x.setter
    def x(self, value):
        """
                Setter for the x-coordinate of the rectangle.
        pass
                Args:
                    value (int): The new x-coordinate of the rectangle.
        """
        self.__x = value

    @property
    def y(self):
        """
                Getter for the y-coordinate of the rectangle.
        pass
                Returns:
                    int: The y-coordinate of the rectangle.
        """
        return self.__y

    @y.setter
    def y(self, value):
        """
                Setter for the y-coordinate of the rectangle.
        pass
                Args:
                    value (int): The new y-coordinate of the rectangle.
        """
        self.__y = value
