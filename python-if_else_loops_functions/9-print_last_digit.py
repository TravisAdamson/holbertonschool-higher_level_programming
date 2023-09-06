#!/usr/bin/python3
def print_last_digit(number):
    if number >= 0 and number < 10:
        result = number
    elif number >= 10:
        result = number % 10
    else:
        result = abs(number) % 10
    print("{:d}".format(result), end="")
    return result
