from Shape_class import Shape
import math

class Hexagon(Shape):
    def __init__(self, side):
        self.side = side

    def get_area(self):
        return (self.side ** 2) * ((math.sqrt(3) * 3) / 2)

    def get_perimeter(self):
        return 6 * self.side