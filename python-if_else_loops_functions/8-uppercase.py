#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 127:
            ni = chr(ord(str[i]) - 32)
        else:
            ni = str[i]
        print("{}".format(ni), end="")
print("\n", end="")
