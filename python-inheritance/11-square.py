#!/usr/bin/python3
'''Class Square that inherits from Rectangle'''

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Square class that inherits from Rectangle'''

    def __init__(self, size):
        '''Initialize a new square.

        Args:
            size (int): The size of the new square.
        '''
        self.integer_validator('size', size)
        super().__init__(size, size)

    def __str__(self):
        '''Return the print() and str() representation of a Square'''
        return "[Square] {}/{}".format(self._Rectangle__width, self._Rectangle__height)
