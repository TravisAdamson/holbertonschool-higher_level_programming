#!/usr/bin/python3
import sys
import calculator_1

def main():
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(sys.argv[1])
    b = int(sys.argv[3])
    operator = ord(sys.argv[2])
    if operator == 43:
        print("{} {} {} = {}".format(a, b, calculator_1.add(a, b)))
    elif operator == 45:
        print("{} {} {} = {}".format(a, str(operator), b, calculator_1.sub(a, b)))
    elif operator == 42:
        print("{} {} {} = {}".format(a, str(operator), b, calculator_1.mul(a, b)))
    elif operator == 47:
        print("{} {} {} = {}".format(a, str(operator), b, calculator_1.div(a, b)))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main()
