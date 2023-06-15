#!/usr/bin/python3
# base.py
# Martin <martin.mulama@yahoo.com"
""" A module that contains base class """

import json

class Base:
    """ This is a base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ initializes base class instance """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ that returns the JSON string representation of list_dictionaries """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation of list_objs to a file """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as file:
            for obj in list_objs:
                json_data = cls.to_json_string([obj.to_dictionary()])
                file.write(json_data)

    @staticmethod
    def from_json_string(json_string):
        """ that returns the list of the JSON string representation json_string """
        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ that returns an instance with all attributes already set """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances from a JSON file """
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r') as file:
                json_data = file.read()
            if json_data:
                dictionaries_list = cls.from_json_string(json_data)
                for dictionary in dictionaries_list:
                    instances = cls.create(**dictionary)
            else:
                return []
        except FileNotFoundError:
            return []
