#!/usr/bin/python3
import sys


def main():
    num = len(sys.argv) - 1
    if num > 0 and not sys.argv[1]:
        print("0 arguments.")
        num = -1
    elif num > 1:
        print("{:d} arguments:".format(num))
    elif num == 1:
        print("1 argument:")
    else:
        print("0 arguments.")
    for i in sys.argv:
        if sys.argv.index(i) > 0:
            print("{:d}: {:s}".format(sys.argv.index(i), i))


if __name__ == "__main__":
    main()
