from Rectangle_class import Rectangle

class Triangle(Rectangle):
    def __init__(self, base,height):
        super().__init__(base,height)

    def get_area(self):
        return super().get_area() /2