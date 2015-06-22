"""
A series of practice problems for Python involving numbers and math.

by Giovanni Prinzivalli
"""
from pip._vendor.distlib.compat import raw_input
import math

def find_float_digits(float, number):
    """Returns a float to the nth digit as specified by the caller"""
    return '{:.{width}f}'.format(float, width=number)

if __name__ == "__main__":
    while True:
        try:
            dig = raw_input("Select the digits (max 50) of Pi and e you want to find >> ")
            if int(dig) > 0 and int(dig) <= 50:
                break
            else:
                print("Out of bounds. Try again.")
        except ValueError:
            print("Not an integer. Try again.")
    
    #Exercises 1 and 2: Finding pi/e to the nth digit.
    print("Pi to " + dig + " digits:")
    print(find_float_digits(math.pi, dig) + "\n")
    print("e to " + dig + " digits:")
    print(find_float_digits(math.e, dig) + "\n")
    
    