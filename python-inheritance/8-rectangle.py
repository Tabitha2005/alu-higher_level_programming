#!/usr/bin/python3
'''Defines Class Rectangle that inherits from BaseGeometry '''


BaseGeometry = _import_('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    '''Rectangle class that inherits the BaseGeometry '''

    def _init_(self, width, height):
        '''A function that created a rectangle '''
        self.integer_validator('width', width)
        self.__width = width
        self.integer_validator('height', height)
        self.__height = height
Tabitha
