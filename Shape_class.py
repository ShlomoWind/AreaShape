from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass
    @abstractmethod
    def get_perimeter(self):
        pass


    def __str__(self):
        return f"the area from the {self.__class__.__name__} is {self.get_area()} and the perimeter is {self.get_perimeter()}"

    def __add__(self, other):
        if isinstance(other, Shape):
            return self.get_area() + other.get_area()
        return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Shape):
            return self.get_area() - other.get_area()
        return NotImplemented

    def __mul__(self, other):
        if isinstance(other, Shape):
            return self.get_area() * other.get_area()
        return NotImplemented

    def __eq__(self, other):
        if isinstance(other, Shape):
            return self.get_area() == other.get_area()
        return NotImplemented

    def __ne__(self, other):
        if isinstance(other, Shape):
            return self.get_area() != other.get_area()
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() < other.get_area()
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, Shape):
            return self.get_area() > other.get_area()
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, Shape):
            return self.get_area() <= other.get_area()
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, Shape):
            return self.get_area() >= other.get_area()
        return NotImplemented

