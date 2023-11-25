#!/usr/bin/env python
# coding: utf-8

# In[ ]:


class Hexagon:
    def __init__(self, cnic):
        self.side_length = int(cnic[-1])  # Last digit of CNIC
        self.angle = 120  # Angle of a hexagon

    def calculate_area(self):
        return 1.5 * 1.732 * self.side_length

    def calculate_perimeter(self):
        return 6 * self.side_length

    def calculate_sum_angles(self):
        return 6 * self.angle


class Square:
    def __init__(self, cnic):
        self.side_length = int(cnic[-1]) + 1  # Last digit of CNIC + 1

    def calculate_area(self):
        return self.side_length ** 2

    def calculate_perimeter(self):
        return 4 * self.side_length


def main():
    cnic = input("Enter your CNIC: ")
    hexagon = Hexagon(cnic)
    square = Square(cnic)

    while True:
        print("\nMenu:")
        print("Enter 1 to calculate area ,perimeter and sum of angles of Hexagon")
        print("Enter 2 to calculate area and perimeter of Square")
        print("Enter any other key to exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            print("\nHexagon:")
            print(f"Area of Hexagon: {hexagon.calculate_area()}")
            print(f"Perimeter of hexagon: {hexagon.calculate_perimeter()}")
            print(f"Sum of all angles of hexagon: {hexagon.calculate_sum_angles()}")

        elif choice == '2':
            print("\nSquare:")
            print(f"Area: {square.calculate_area()}")
            print(f"Perimeter: {square.calculate_perimeter()}")

        else:
            print("Exiting...")
            break


if __name__ == "__main__":
    main()


# In[ ]:




