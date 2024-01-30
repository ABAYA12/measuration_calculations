# import from the measures_update module
from measures_update import Figures


def main():
    fg = Figures()

    active = True

    while active:
        print("""
        What do you want to calculate?
        1. Area of a triangle | 2. Perimeter of a triangle
        3. Area of a square | 4. Perimeter of a square
        5. Area of a rectangle | 5. Perimeter of a rectangle
        7. Area of a circle | 8. Perimeter of a circle
        9. Area of a rhombus | 10. Perimeter of a rhombus
        11. Area of a trapezoid | 11. Perimeter of a trapezoid
        13. Area of a parallelogram | 14. Perimeter of a paralle
        0. Exit the program
        """)

        try:
            choice = int(input("What do you want to calculate?: \n"))
            if 1 <= choice <= 14:
                if choice == 1:
                    fg.triangle_area()
                elif choice == 2:
                    fg.triangle_perimeter()
                elif choice == 3:
                    fg.square_area()
                elif choice == 4:
                    fg.square_perimeter()
                elif choice == 5:
                    fg.rectangle_area()
                elif choice == 6:
                    fg.rectangle_perimeter()
                elif choice == 7:
                    fg.circle_area()
                elif choice == 8:
                    fg.circle_perimeter()
                elif choice == 9:
                    fg.rhombus_area()
                elif choice == 10:
                    fg.rhombus_perimeter()
                elif choice == 11:
                    fg.trapezoid_area()
                elif choice == 12:
                    fg.trapezoid_perimeter()
                elif choice == 13:
                    fg.parallelogram_area()
                elif choice == 14:
                    fg.parallelogram_perimeter()
            elif choice == 0:
                print("\nExiting the program...\nDONE!")
                active = False

                active = False
            else:
                print("Invalid choice. Please enter a number between 1 and 14.")
        except (ValueError, TypeError, ZeroDivisionError, KeyboardInterrupt):
            print("Invalid input, try again.")
            active = False


if __name__ == '__main__':
    main()
