from Rectangle_class import Rectangle
from Square_class import Square
from Circle_class import Circle
from Hexagon_class import Hexagon
from Triangle_class import Triangle

class ShapeManager:
    @staticmethod
    def menu():
        try:
            while True:
                print("Welcome to Shape Manager Menu!")
                print("Please select an option:")
                print("1. Create a Square")
                print("2. Create a Rectangle")
                print("3. Create a Circle")
                print("4. Create a Hexagon")
                print("5. Create a Triangle")
                print("6. Exit")
                choice = str(input("Enter your choice: "))
                shape = None
                match(choice):
                    case "1":
                        side = float(input("Enter the side length of the square: "))
                        shape = Square(side)
                        print(shape)
                    case "2":
                        width = float(input("Enter the width of the rectangle: "))
                        height = float(input("Enter the height of the rectangle: "))
                        shape = Rectangle(width, height)
                        print(shape)
                    case "3":
                        radius = float(input("Enter the radius of the circle: "))
                        shape = Circle(radius)
                        print(shape)
                    case "4":
                        side = float(input("Enter the side length of the hexagon: "))
                        shape = Hexagon(side)
                        print(shape)
                    case "5":
                        base = float(input("Enter the base of the triangle: "))
                        height = float(input("Enter the height of the triangle: "))
                        shape = Triangle(base, height)
                        print(shape)
                    case "6":
                        print("Exiting the program.")
                        break
                    case _:
                        print("Invalid choice. Please try again.")
                        continue
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")