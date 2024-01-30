class Planefigure():
    def __init__(self):
        pass

    # perimeter of a rectangle
    def peri_rectangle(self, length, width):
        """
        **parameters**:

        length(float): length of the rectangle in cm.
        width(float): width of the rectangle in cm.

        **returns**:

        The function will return the perimeter of the rectangle if all the parameters are valid otherwise it will return None. 
        method returns the value of perimeter.

        **raises**:

        TypeError: if the length or width is not a number.
        ValueError: if the length or width is less than 0.
        """
        perimetr = 2 * (length + width)
        return perimetr

    # area of  a rectangle
    def area_rectangle(self, length, width):
        """
        **parameters**:

        length(float): length of the rectangle in cm.
        width(float): width of the rectangle in cm.

        **returns**:

        The function will return the area of the rectangle if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the length or width is not a number.
        ValueError: if the length or width is less than 0.
        """
        area = length * width
        return area

    # perimeter of a square
    def peri_square(self, length):
        """
        **parameters**:

        length(float): length of the square in cm.

        **note**:

        perimeter = 4 * (length)

        **returns**:

        The function will return the perimeter of the square if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the length is not a number.
        ValueError: if the length is less than 0.
        """
        perimeter = 4 * (length)
        return perimeter

    # area of a square
    def area_square(self, length):
        """
        **parameters**:

        length(float): length of the square in cm.

        **returns**:
        The function will return the area of the square if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the length is not a number.
        ValueError: if the length is less than 0.
        """
        area = length * length
        return area

    # perimeter of a triangle
    def peri_triangle(self, length, width, base):
        """
        **parameters**:

        length(float): length of the triangle in cm.
        width(float): width of the triangle in cm.
        base(float): base of the triangle in cm.

        **returns**:

        The function will return the perimeter of the triangle if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the length, width or base is not a number.
        ValueError: if the length, width or base is less than 0.
        """
        perimeter = base + length + width
        return perimeter

    # area of a triangle
    def area_triangle(self, height, base):
        """
        **parameters**:

        height(float): height of the triangle in cm.
        base(float): base of the triangle in cm.

        **returns**:

        The function will return the area of the triangle if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the height or base is not a number.
        ValueError: if the height or base is less than 0.
        """

        area = (base * height) / 2
        return area

    # perimeter of a parallelogram
    def peri_parallelogram(self, base, sides):
        """
        **parameters**:

        base(float): base of the parallelogram in cm.
        sides(float): sides of the parallelogram in cm.

        **returns**:

        The function will return the perimeter of the parallelogram if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the base or sides is not a number.
        ValueError: if the base or sides is less than 0.
        """
        perimeter = 2 * (base + sides)
        return perimeter

    # area of a parallelogram
    def area_parallelogram(self, base, height):
        """
        **parameters**:

        base(float): base of the parallelogram in cm.
        height(float): height of the parallelogram in cm.

        **returns**:

        The function will return the area of the parallelogram if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the base or height is not a number.
        ValueError: if the base or height is less than 0.
        """
        area = base * height
        return area

    # perimeter of a trapezoid
    def peri_trapezoid(self, base1, base2, side1, side2):
        """
        **parameters**:

        base1(float): base1 of the trapezoid in cm.
        base2(float): base2 of the trapezoid in cm.
        side1 and side2(float): sides of the trapezoid in cm.

        **returns**:

        The function will return the perimeter of the trapezoid if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the base1, base2 or sides is not a number.
        ValueError: if the base1, base2 or sides is less than 0.
        """
        perimeter = (base1 + base2 + side1 + side2)
        return perimeter

    # area of a trapezoid
    def area_trapezoid(self, base1, base2, height):
        """
        **parameters**:

        base1(float)-parallel side: base1 of the trapezoid in cm.
        base2(float)-parallel side: base2 of the trapezoid in cm.
        height(float): height of the trapezoid in cm.

        **returns**:

        The function will return the area of the trapezoid if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the base1, base2 or height is not a number.
        ValueError: if the base1, base2 or height is less than 0.
        """
        area = ((base1 + base2) / 2) * height
        return area

    # perimeter of a rhombus

    def peri_rhombus(self, length):
        """
        **parameters**:

        length(float): length of the rhombus in cm.

        **returns**:

        The function will return the perimeter of the rhombus if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the length is not a number.
        ValueError: if the length is less than 0.
        """
        perimeter = 4 * (length)
        return perimeter

    # area of a rhombus

    def area_rhombus(self, diagonal_length_1, diagonal_length_2):
        """
        **parameters**:

        diagonal_length_1(float): diagonal_length_1 of the rhombus in cm.
        diagonal_length_2(float): diagonal_length_2 of the rhombus in cm.

        **returns**:

        The function will return the area of the rhombus if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the diagonal_length_1 or diagonal_length_2 is not a number.
        ValueError: if the diagonal_length_1 or diagonal_length_2 is less than 0.
        """
        area = (diagonal_length_1 * diagonal_length_2) / 2
        return area

    # perimeter of a circle
    def peri_circle(self, radius):
        """
        **parameters**:

        radius(float): radius of the circle in cm.

        **returns**:

        The function will return the perimeter of the circle if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the radius is not a number.
        ValueError: if the radius is less than 0.
        """
        perimeter = 2 * (3.14 * radius)
        return perimeter

    # area of a circle
    def area_circle(self, radius):
        """
        **parameters**:

        radius(float): radius of the circle in cm.

        **returns**:

        The function will return the area of the circle if all the parameters are valid otherwise it will return None.

        **raises**:

        TypeError: if the radius is not a number.
        ValueError: if the radius is less than 0.
        """
        area = 3.14 * (radius ** 2)
        return area
