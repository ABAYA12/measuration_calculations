from main import Planefigure


# functions for calculations

pf = Planefigure()


class Figures:

    def triangle_area(self):
        # area of a triangle
        print('\nCalculating area of a trinagle\n')
        base = float(input("Enter the base of the triangle: "))
        height = float(input("Enter the height of the triangle: "))
        result = pf.area_triangle(base, height)
        print(f"\nArea: {result: .2f}cm squared")

    def triangle_perimeter(self):
        # perimeter of a triangle

        print("\nCalculating perimter of a triangle\n")
        base = float(input("Enter the base of the triangle: "))
        length = float(input("Enter the length of the triangle: "))
        width = float(input("Enter the width of the triangle: "))
        result = pf.peri_triangle(length, width, base)
        print(f"\nPerimeter: {result: .2f}cm")

        # # perimeter of a triangle
        # base = float(input("Enter the base of the triangle: "))
        # length = float(input("Enter the length of the triangle: "))
        # width = float(input("Enter the width of the triangle: "))
        # result = pf.peri_triangle(length, width, base)
        # print(f"\nPerimeter: {result: .2f}cm")

    def square_area(self):
        # area of a square
        print('\nCalculating area of a square\n')
        length = float(input("Enter the length of the square: "))
        result = pf.area_square(length)
        print(f"\nArea: {result: .2f}cm squared")

    def square_perimeter(self):
        # perimeter of a square
        print('\nCalculating perimeter of a square\n')
        length = float(input("Enter the length of the square: "))
        result = pf.peri_square(length)
        print(f"\nPerimeter: {result: .2f}cm")

    def rectangle_area(self):
        # area of a rectangle
        print('\nCalculating area of a rectangle\n')
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = pf.area_rectangle(length, width)
        print(f"\nArea: {result: .2f}cm squared")

    def rectangle_perimeter(self):
        # perimeter of a rectangle
        print('\nCalculating perimeter of a rectangle\n')
        length = float(input("Enter the length of the rectangle: "))
        width = float(input("Enter the width of the rectangle: "))
        result = pf.peri_rectangle(length, width)
        print(f"\nPerimeter: {result: .2f}cm")

    # continue the functions

    def circle_area(self):
        # area of a circle
        print('\nCalculating area of a circle\n')
        radius = float(input("Enter the radius of the circle: "))
        result = pf.area_circle(radius)
        print(f"\nArea: {result: .2f}cm squared")

    def circle_perimeter(self):
        # perimeter of a circle
        print('\nCalculating perimeter of a circle\n')
        radius = float(input("Enter the radius of the circle: "))
        result = pf.peri_circle(radius)
        print(f"\nPerimeter: {result: .2f}cm")

    def trapezoid_area(self):
        # area of a trapezoid
        print("\nCalculating area of a trapezoid\n")
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        height = float(input("Enter the height of the trapezoid: "))
        result = pf.area_trapezoid(base1, base2, height)
        print(f"\nArea: {result: .2f}cm squared")

    def trapezoid_perimeter(self):
        # perimeter of a trapezoid
        print("\nCalculating perimeter of a trapezoid\n")
        base1 = float(input("Enter the first base of the trapezoid: "))
        base2 = float(input("Enter the second base of the trapezoid: "))
        length = float(input("Enter the length of the trapezoid: "))
        width = float(input("Enter the width of the trapezoid: "))
        result = pf.peri_trapezoid(base1, base2, length, width)
        print(f"\nPerimeter: {result: .2f}cm")

    def parallelogram_area(self):
        # area of a parallelogram
        print("\nCalculating area of a parallelogram\n")
        base = float(input("Enter the base of the parallelogram: "))
        height = float(input("Enter the height of the parallelogram: "))
        result = pf.area_parallelogram(base, height)
        print(f"\nArea: {result: .2f}cm squared")

    def parallelogram_perimeter(self):
        # perimeter of a parallelogram
        print('\nCalculatin perimeter of a parallelogram\n')
        length = float(input("Enter the length of the parallelogram: "))
        width = float(input("Enter the width of the parallelogram: "))
        result = pf.peri_parallelogram(length, width)
        print(f"\nPerimeter: {result: .2f}cm")

    def rhombus_area(self):
        # area of a rhombus
        print('\nCalculating area of a rhombus\n')
        diagonal_length_1 = float(
            input("Enter the first diagonal length of the rhombus: "))
        diagonal_length_2 = float(
            input("Enter the second diagonal length of the rhombus: "))
        result = pf.area_rhombus(diagonal_length_1, diagonal_length_2)
        print(f"\nArea: {result: .2f}cm squared")

    def rhombus_perimeter(self):
        # perimeter of a rhombus
        print('\nCalculating perimeter of a rhombus\n')
        length = float(input("Enter the length of the rhombus: "))
        result = pf.peri_rhombus(length)
        print(f"\nPerimeter: {result: .2f}cm")
