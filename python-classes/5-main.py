#!/usr/bin/python3
Square = __import__('5-square').Square

my_square = Square(3)
my_square.my_print()

print("--")

my_square.size = 8
my_square.my_print()

print("--")

my_square.size = -1
my_square.my_print()

print("--")
