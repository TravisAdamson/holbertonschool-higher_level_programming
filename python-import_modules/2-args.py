#!/usr/bin/python3
import sys


def main():
    num = len(sys.argv)
    if num != 0 and num > 1:
        print("{:d} arguments:".format(num))
    elif num == 1:
        print("1 arguement:")
    else:
        print("0 arguements.")
    if num > 0:
        for i in range(1, num + 1):
            print("{:d}: {:s}".format(i, sys.argv[i]))


if __name__ == "__main__":
    main()
