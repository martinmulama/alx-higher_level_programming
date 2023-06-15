#!/usr/bin/python3
# rectangle.py
# Martin <martin.mulama@yahoo.com>
""" rectangle module """
from models.base import Base

class Rectangle(Base):
    """ A rectangle class that inherits from Base class """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ initializes the rectangle class """
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """ Retrieves the width of rectangle """
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width of rectangle """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """ retrieves the height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the height of the rectangle """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """ retrieves x """
        return self.__x

    @x.setter
    def x(self, value):
        """ sets value of x """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """ Retrieves value of y """
        return self.__y

    @y.setter
    def y(self, value):
        """ sets value of y """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__width = value

    def area(self):
        """ returns the area of the rectangle instance """
        return self.__width * self.__height

    def display(self):
        """ prints in stdout the Rectangle instance with the character # """
        for height_co_ordinate in range (self.__y):
            print()
        for height_symbol in range(self.__height):
            print(" " * self.__x, end="")
            for width_symbol in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """ returns [Rectangle] (<id>) <x>/<y> - <width>/<height> """
        return f"[Rectangle] ({self.id}) {self.__x}/{self.__y} - {self.__width}/{self.__height}"

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute """
        if args:
            num_args = len(args)
            if num_args > 0:
                self.id = args[0]
            if num_args > 1:
                self.width = args[1]
            if num_args > 2:
                self.height = args[2]
            if num_args > 3:
                self.x = args[3]
            if num_args > 4:
                self.y = args[4]
        elif kwargs:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Rectangle """
        return {
            "id": self.id,
            "width": self.__width,
            "height": self.__height,
            "x": self.__x,
            "y": self.__y
            }

