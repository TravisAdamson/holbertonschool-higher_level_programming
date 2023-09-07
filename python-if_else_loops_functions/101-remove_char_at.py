#!/usr/bin/python3


def remove_char_at(str, n):
    sw = 0
    newstr = ""
    for i in range(0, len(str)):
        if i != n:
            newstr += str[i]
    return newstr
