#!/usr/bin/python3
def print_last_digit(number):
    if number > 9:
        result = number % 10
    elif number >= 0 and number < 10:
        result = number
    else
        result = (abs(number) % 10) * -1
    return result
