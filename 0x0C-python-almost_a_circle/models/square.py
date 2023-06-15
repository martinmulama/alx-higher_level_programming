#!/usr/bin/python3
#square.py
# Martin <martin.mulama@yahoo.com>
""" square.py is a module that inherits from rectangle class """

from models.rectangle import Rectangle

class Square(Rectangle):
    """ A class square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ sets the size of the square """
        return self.width

    @size.setter
    def size(self, value):
        """ sets the value of the size of the square """
        self.width = value
        self.height = value

    def __str__(self):
        """ Returns print representation of the square """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

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
        """ returns the dictionary representation of Square """
        return {
            "id": self.id,
            "size": self.width,
            "x": self.x,
            "y": self.y
        }
