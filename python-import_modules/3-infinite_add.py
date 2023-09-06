#!/usr/bin/python3
import sys


def main():
    total = 0
    if len(sys.argv) - 1 > 1:
        for i in sys.argv:
            if sys.argv.index(i) > 0:
                total = total + int(i)
    elif len(sys.argv) - 1 == 1:
        total = int(sys.argv[1])
    print("{:d}".format(total))


if __name__ == "__main__":
    main()
