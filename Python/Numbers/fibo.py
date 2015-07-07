"""
fibo.py
A module containing fibonacci sequence operations.

by Giovanni Prinzivalli
"""
from numHelp import get_int_in_range
from sys import maxint

RANGE_MAX = 100000

def fibonacci(n):
    """Returns the first n digits of the fibonacci sequence as a list."""
    seq = [0]

    if n >= 2:
        seq.append(1)
    if n >= 3:
        for i in range(2, n + 1):
            seq.append(seq[i-1] + seq[i-2])

    return seq

def find_n_in_fibo(number):
    """Returns a fibonacci sequence up to n or the next digit greater than n as a list"""
    if number == 0:
        return [0]

    seq = [0, 1]
    i = 1
    while seq[i] < number:
        seq.append(seq[i] + seq[i - 1])
        i += 1

    return seq

if __name__ == "__main__":
    print "Fibo.py == Fibonacci sequence generator."
    print "1) Return the first N digits of a fibonacci sequence."
    print "2) Return the fibonacci sequence up to a specified number."
    response = get_int_in_range("Please make a selection -> ", 1, 2)

    if response == 1:
        num = get_int_in_range("Please select the length of "+
                               "the fibonacci sequence to be generated (max 100) -> ", 1, 100)
        print fibonacci(num)
    elif response == 2:
        num = get_int_in_range("Please select the number you "+
                               "wish to go to in the sequence (max %s) => " % RANGE_MAX, 0, RANGE_MAX)
        print find_n_in_fibo(num)
        