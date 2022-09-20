#!/usr/bin/python3
""" Class Rectangle """


class Rectangle:
        """ rectangle """
            number_of_instances = 0
                print_symbol = "#"

                    def __init__(self, width=0, height=0):
                                """ constructor """
                                        self.width = width
                                                self.height = height
                                                        Rectangle.number_of_instances += 1

                                                            @property
                                                                def width(self):
                                                                            """ getter """
                                                                                    return self.__width

                                                                                    @width.setter
                                                                                        def width(self, value):
                                                                                                    """ setter """
                                                                                                            if type(value) != int:
                                                                                                                            raise TypeError("width must be an integer")
                                                                                                                                if value < 0:
                                                                                                                                                raise ValueError("width must be >= 0")
