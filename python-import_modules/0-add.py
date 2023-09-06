#!/usr/bin/python3
from add_0 import add

def main():
    a = 1
    b = 2
    print("{:i} + {:i} = {:i}".format(a, b, add(a, b)), end="\n")

if __name__ == "__main__":
    main()
