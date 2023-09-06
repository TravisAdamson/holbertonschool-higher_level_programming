#!/usr/bin/python3
import uncompyle6


def main():
    with open("hidden.pyc", "rb") as line:
        data = f.read()
    narray = uncompyle6.disassemble(code)

    for name in narray:
        print("{:s}".format(name))


if __name__ == "__main__":
    main()
