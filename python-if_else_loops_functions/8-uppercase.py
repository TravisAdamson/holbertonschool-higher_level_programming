#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 127:
            ni = ord(str[i]) - 32
        else:
            ni = ord(str[i])
        print("{}".format(str[ni]), end="")
