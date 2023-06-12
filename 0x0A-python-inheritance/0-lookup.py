#!/usr/bin/python3

def lookup(obj):
    """
    Returns a list of available attributes and methods of an object.

    Args:
        obj: An object to inspect.

    Returns:
        A list of strings representing the available attributes and methods of the object.

    Example:
        class Person:
            def __init__(self, name, age):
                self.name = name
                self.age = age

            def say_hello(self):
                print(f"Hello, my name is {self.name}!")

        person = Person("John", 25)
        attributes_and_methods = lookup(person)
        print(attributes_and_methods)
        # Output: ['age', 'name', 'say_hello']
    """
    attributes = []
    methods = []

    for attr in dir(obj):
        if not attr.startswith('__'):
            value = getattr(obj, attr)
            if callable(value):
                methods.append(attr)
            else:
                attributes.append(attr)

    return attributes + methods

