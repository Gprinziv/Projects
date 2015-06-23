"""
fibo.py
A module containing fibonacci sequence operations.

by Giovanni Prinzivalli
"""
from numHelp import get_int_in_range

def fibonacci(n):
    """Returns the first n digits of the fibonacci sequence as a list."""
    seq = []
    if n == 1:
        seq.append(0)
    elif n == 2:
        seq.append(0)
        seq.append(1)
    for i in range(3, n):
        seq.append(seq[i-1] + seq[i-2])

    return seq

def find_n_in_fibo(number):
    """Returns a fibonacci sequence up to n or the next digit greater than n as a list"""
    return number

if __name__ == "__main__":
    print "Fibo.py == Fibonacci sequence generator."
    print "1) Return the first N digits of a fibonacci sequence."
    print "2) Return the fibonacci sequence up to a specified number."
    response = get_int_in_range("Please make a selection -> ", 1, 2)

    if response == 1:
        num = get_int_in_range("Please select the length of "+
                               "the fibonacci sequence to be generated (max 100) -> ", 1, 100)
        sequence = fibonacci(num)
        print sequence
    elif response == 2:
        num = get_int_in_range("Please select the number you "+
                               "wish to find in the fibo sequence (max 100,000) => ", 0, 100000)
        print find_n_in_fibo(num)
