#!/usr/bin/python3
""" creates a private instance attribute size  """


class Square:
    """ this is a class with a private attribute size """
    def __init__(self, size=0):
        if type(size) != int:
            raise TypeError("type must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
