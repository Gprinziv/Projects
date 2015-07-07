"""
primes.py
Prime number functions

by Giovanni Prinzivalli
"""
from numHelp import get_int_in_range

FACTOR_MAX = 100000000

def get_prime_factors(number):
    """Gets all of the prime factors of an int."""
    pass

def get_next_prime(old_prime):
    """Continually gets the next prime number until the user tells it to stop."""
    pass

if __name__ == "__main__":
    print "Primes.py == Prime numbers module."
    print "1) Get the prime factors of a number."
    print "2) Get prime numbers in order until told to stop."
    response = get_int_in_range("Please make a selection -> ", 1, 2)

    if response == 1:
        num = get_int_in_range("What number would you like to" +
                               " factorize (max %s)? -> " % FACTOR_MAX, 0, FACTOR_MAX)
        print get_prime_factors(num)
    elif response == 2:
        print "Null"
