from Shape_class import Shape
from Exception_class import CheckNumbers
import math

class Hexagon(Shape):
    def __init__(self, side):
        CheckNumbers.correct_numbers(side,"side")
        self.side = side

    def get_area(self):
        return (self.side ** 2) * ((math.sqrt(3) * 3) / 2)

    def get_perimeter(self):
        return 6 * self.side