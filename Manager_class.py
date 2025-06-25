from Rectangle_class import Rectangle
from Square_class import Square
from Circle_class import Circle
from Hexagon_class import Hexagon
from Triangle_class import Triangle

class ShapeManager:
    @staticmethod
    def menu():
        try:
            print("Welcome to Shape Manager Menu!")
            shape_list = []
            while True:
                print("==========================================")
                print("Please select an option:")
                print("1. Create a Square")
                print("2. Create a Rectangle")
                print("3. Create a Circle")
                print("4. Create a Hexagon")
                print("5. Create a Triangle")
                print("6. Compare or combine two existing shapes")
                print("7. Exit")
                print("==========================================")
                choice = input("Enter your choice: ")
                shape = None
                match choice:
                    case "1":
                        side = float(input("Enter the side length of the square: "))
                        shape = Square(side)
                    case "2":
                        width = float(input("Enter the width of the rectangle: "))
                        height = float(input("Enter the height of the rectangle: "))
                        shape = Rectangle(width, height)
                    case "3":
                        radius = float(input("Enter the radius of the circle: "))
                        shape = Circle(radius)
                    case "4":
                        side = float(input("Enter the side length of the hexagon: "))
                        shape = Hexagon(side)
                    case "5":
                        base = float(input("Enter the base of the triangle: "))
                        height = float(input("Enter the height of the triangle: "))
                        shape = Triangle(base, height)
                    case "6":
                        if len(shape_list) < 2:
                            print("Please create at least two shapes first.")
                            continue
                        print("Available shapes:")
                        print("-----------------------------------")
                        for index,s in enumerate(shape_list):
                            print(f"{index + 1}. {s.__class__.__name__} - Area: {s.get_area()}, Perimeter: {s.get_perimeter()}")
                        print("-----------------------------------")
                        try:
                            first_index = int(input("Select the first shape: ")) - 1
                            second_index = int(input("Select the second shape: ")) - 1
                            if not(0 <= first_index < len(shape_list)) or not(0 <= second_index < len(shape_list)):
                                print("Invalid selection. Please try again.")
                                continue
                            s1 = shape_list[first_index]
                            s2 = shape_list[second_index]
                            op = input("Choose an operation: (+, -, *, ==, !=, <, >, <=, >=)\nEnter your choice: ")
                            result = None
                            match op:
                                case "+":
                                    result = s1 + s2
                                case "-":
                                    result = s1 - s2
                                case "*":
                                    result = s1 * s2
                                case "==":
                                    result = s1 == s2
                                case "!=":
                                    result = s1 != s2
                                case "<":
                                    result = s1 < s2
                                case ">":
                                    result = s1 > s2
                                case "<=":
                                    result = s1 <= s2
                                case ">=":
                                    result = s1 >= s2
                                case _:
                                    print("Invalid operation. Please try again.")
                                    continue
                            print(f"\nResult of {s1.__class__.__name__} {op} {s2.__class__.__name__} is: {result}")
                        except (ValueError, IndexError) as e:
                            print(f"Error: {e}. Please select valid shapes and operations.")
                            continue
                    case "7":
                        print("Exiting the program.")
                        break
                    case _:
                        print("Invalid choice. Please try again.")
                        continue
                if shape:
                    shape_list.append(shape)
                    print(shape)
        except ValueError as e:
            print(f"Error: {e}. Please enter valid numbers.")