"""stringOps.py - Various String manipulation operations
   by Giovanni Prinzivalli """

def fizz_buzz(length):
    """Prints all numbers between 1 and length, replacing multiples
       of 3 with Fizz, multiples of 5 with Buzz, and multiples of 15 with FizzBuzz"""
    arr = []
    for i in range(1, length + 1):
        if not i % 15:
            arr.append("FizzBuzz")
        elif not i % 3:
            arr.append("Fizz")
        elif not i % 5:
            arr.append("Buzz")
        else:
            arr.append(i)
    return arr

def reverse_string(text):
    """Reverses a string. Not rocket surgery."""
    return text[::-1]

def pig_latin(text):
    """Later."""
    pass

def count_vowels(text):
    """Counts the number of vowels used in a string. Reports by vowel."""
    pass

def is_palindrome(text):
    """Checks if a string reads the same both ways"""
    return text.lower() == text[::-1].lower()

def count_words(text):
    """Counts the number of words in a string. For added complexity, give a summary and read from a file."""
    pass

if __name__ == "__main__":
    print "Fizzbuzz list..."
    print fizz_buzz(100)

    print "String reverser"
    print reverse_string("Hello!")

    print "Pig latin converter..."
    print "Psyche. Implementing later."

    print "Palindrome checking..."
    print is_palindrome("aha")
    print is_palindrome("racecar")
    print is_palindrome("aHA")
    print is_palindrome("Racecar")
    print is_palindrome("Magic schoolbus")
