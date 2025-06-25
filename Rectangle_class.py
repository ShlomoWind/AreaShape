from Exception_class import CheckNumbers
from Shape_class import Shape

class Rectangle(Shape):
    def __init__(self,width,height):
        CheckNumbers.correct_numbers(width,"width")
        CheckNumbers.correct_numbers(height,"height")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)