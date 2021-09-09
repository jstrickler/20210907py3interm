"""
Tools for geometric calculations

This library contains many geometric functions for computing
area and volume of geometric shapes

"""
import math
import sys

def main(args):
    diameter = float(args[0])  # 1st arg
    print(circle_area(diameter))

def circle_area(diameter):
    """
    Calculate area of a circle

    :param diameter: Diameter (not radius)
    :return: Area as a float
    """
    return math.pi * ((diameter/2) ** 2)

def rectangle_area(length, width):
    """
    Calculate area of a rectangle

    :param length: Length of rectangle
    :param width: Width of rectangle
    :return: Area as a float
    """
    return length * width

def square_area(length):
    """
    Calculate area of a square

    :param length: Length of side
    :return: Area as a float
    """
    return rectangle_area(length, length)

# print(f"my __name__ is {__name__}")

if __name__ == '__main__':
    main(sys.argv[1:])




