"""
artih.py
Module containing basic artihmetic functions.

by Giovanni Prinzivalli
"""
from numHelp import get_int_in_range
import math

def find_tile_cost(cost, width, height):
    """Calculates the total cost """
    return '{:,.2f}'.format(cost * width * height)

def mortgage(base, terms, apr, rate):
    """Figures out the monthly payments for a loan."""
    pass

def change_return(payment, cost):
    """Figures out the change to pay out for a given cost and payment."""
    dollars = int(math.floor(payment - cost))
    coins = int((payment - cost - dollars) * 100)
    quarters = coins // 25
    coins %= 25
    dimes = coins // 10
    coins %= 10
    nickels = coins // 5
    pennies = coins % 5
    return {"Pennies": pennies, "Nickels": nickels,
            "Dimes": dimes, "Quarters": quarters,
            "Dollars": dollars}

def bin_to_dec(binary):
    """Convets a given binary number to decimal"""
    total = 0

    for i in range(0, len(binary)):
        if binary[i] == '1':
            total += pow(2, len(binary) - i - 1)

    return total

def dec_to_bin(decimal):
    """Converts a given decimal number to binary."""
    return bin(decimal)[2:]

def distance_two_cities(c1, c2):
    """Finds the distance between two cities based on longitude and latitude."""
    return c1 + c2

def validate_cc(cc_number):
    """Performs Luhn's Algorithm on a credit card to validate it."""
    odds = cc_number[-1::-2]
    evens = cc_number[-2::-2]
    checksum = sum(int(dig) for dig in odds)
    for dig in evens:
        temp = int(dig) * 2
        if temp >= 10:
            temp -= 9
        checksum += temp

    return checksum % 10 == 0

if __name__ == "__main__":
    print "Arith.py == Arithmetic functions module."
    print "1) Find the cost to tile a W x H floor."
    print "2) Calculate monthly payments and term period of a loan."
    print "3) Calculate the change given back from a payment."
    print "4) Convert an integer from binary to decimal."
    print "5) Convert an integer from decimal to binary."
    print "6) Find the distance between two cities."
    print "7) Validate a credit card number."
    print "8) Calculate the cost of something after tax is applied."
    response = get_int_in_range("Please make a selection -> ", 1, 8)

    if response == 1:
        cost = float(raw_input("Enter the cost per square foot of tile. -> "))
        width = int(raw_input("Enter the width of the floor in feet. -> "))
        height = int(raw_input("Enter the height of the floor in feet. -> "))
        print find_tile_cost(cost, width, height)
    elif response == 2:
        pass
    elif response == 3:
        cost = float(raw_input("Enter the cost of the item. -> "))
        payment = float(raw_input("How much will you pay? ->"))
        change = change_return(payment, cost)
        for value in change:
            print "%s %s" % (change[value], value)
    elif response == 4:
        print bin_to_dec(raw_input("Enter the binary number you wish to convert. -> "))
    elif response == 5:
        print dec_to_bin(int(raw_input("Enter the integer you wish to convert. -> ")))
    elif response == 6:
        pass
    elif response == 7:
        print validate_cc(raw_input("Enter the credit card number you wish to validate. -> "))
    elif response == 8:
        pass
