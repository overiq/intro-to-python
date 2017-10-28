import math

class Circle:

    def __init__(self, radius):
        self.__radius = radius  #

    def get_area(self):
        return math.pi * self.__radius ** 2

    def get_perimeter(self):
        return 2 * math.pi * self.__radius

    # getter method for radius attribute

    def get_radius(self):
        return self.__radius

    # setter method for radius attribute

    def set_radius(self, radius):
        if not isinstance(radius, int):
            print("Error: ", radius, "is not an int")
            return
        self.__radius = radius