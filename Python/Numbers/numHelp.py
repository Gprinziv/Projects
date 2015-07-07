"""
numHelp.py
A module with helper functions used by the other numbers modules.

by Giovanni Prinzivalli
"""

def get_int_in_range(string, start=0, stop=50):
    """Returns an integer value from input that has been checked for validity."""
    if start > stop:
        raise ValueError("Start value must be less than stop value of range.")

    while True:
        try:
            num = int(raw_input(string))
            if num >= start and num <= stop:
                return num
            else:
                print "Invalid repsponse - (int out of bounds). Try again."
        except ValueError:
            print "Invalid repsonse - (not an integer). Try again."
