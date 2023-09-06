#!/usr/bin/python3
import hidden_4


def main():
    if len(dir(hidden_4)) > 0:
        for i in range(0, len(dir(hidden_4))):
            if dir(hidden_4)[i][0] != '_' and dir(hidden_4)[i][1] != '_':
                print("{:s}".format(dir(hidden_4)[i]))


if __name__ == "__main__":
    main()
