"""Sieve.py - A Sieve of Eratosthenes script
by Giovanni Prinzivalli"""

#set n, the largest number to sieve through.
#set p = 2, the smallest prime. Mark all numbers from p + 1 to n multipe of p as not-prime.
#set p = next unmarked number.
#Repeat until p == n
#Return a list of all unmarked numbers.

def sieve(sieve_max=10000000):
    """Performs the Sieve of Eratosthene algorithm on a list of numbers.
       Returns a list of all primes between 2 and max."""

    prime_idx = 2
    full_sieve = range(2, sieve_max + 1)
    complete_sieve = []

    while prime_idx < sieve_max:
        #Set all multiples of prime_idx to 0
        for val in range(prime_idx * 2, sieve_max + 1, prime_idx):
            full_sieve[val - 2] = 0

        #Find the next nonzero number (prime) and set prime_idx equal to it.
        prime_idx += 1
        while prime_idx < sieve_max - 2 and full_sieve[prime_idx - 2] == 0:
            prime_idx += 1

    #Place all nonzero values (primes) into the return list.
    #There's probably a more elegant solution.
    for val in full_sieve:
        if val is not 0:
            complete_sieve.append(val)
    return complete_sieve

if __name__ == "__main__":
    import numHelp
    max_prime = numHelp.get_int_in_range("Please enter the size of the sieve"
                                         + " you wish to use (max 10,000,000) -> ", 2, 10000000)
    primes = sieve(max_prime)
    print primes
