"""
A series of practice problems for Python involving numbers and math.

by Giovanni Prinzivalli
"""
import math
from numHelp import get_int_in_range

def find_float_digits(float, n):
    """Returns a float to the nth digit as specified by the caller"""
    return '{:.{width}f}'.format(float, width=n)

if __name__ == "__main__":
    n = get_int_in_range("Select the digits (max 50) of Pi and e you want to find -> ")

    #Exercises 1 and 2: Finding pi/e to the nth digit.
    print "Pi to " + n + " digits:"
    print find_float_digits(math.pi, n) + "\n"
    print "e to " + n + " digits:"
    print find_float_digits(math.e, n) + "\n"
