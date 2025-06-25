from Rectangle_class import Rectangle

# Right-angled triangle only:
class Triangle(Rectangle):
    def __init__(self, base,height):
        super().__init__(base,height)

    def get_area(self):
        return super().get_area() /2

    def get_perimeter(self):
        pythagoras = (self.width ** 2 + self.height ** 2) ** 0.5
        return self.height + self.width + pythagoras