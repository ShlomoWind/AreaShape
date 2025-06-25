from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass

    def __str__(self):
        return f"the area from the {self.__class__.__name__} is {self.get_area()}"