#!/usr/bin/python3
def raise_exception():
    try:
        raise TypeError("Exception Raised")
    except TypeError as raisedexception:
        raise raisedexception
