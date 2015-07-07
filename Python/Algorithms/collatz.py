"""collatz.py - A Collatz Conjecture script
by Giovanni Prinzialli"""

def collatz(start, steps = 0):
    if start == 1:
        return steps
    else:
        steps += 1

    if start % 2:
        return collatz(start * 3 + 1, steps)
    else:
        return collatz(start / 2, steps)

if __name__ == "__main__":
    import numHelp
    collatz_start = numHelp.get_int_in_range("Please enter the number you wish"
                                             + " to start with (max 10,000,000) -> ", 2, 10000000)
    print collatz(collatz_start)
