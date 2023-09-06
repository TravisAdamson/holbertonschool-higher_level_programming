#!/usr/bin/python3
def uppercase(str):
    for i in range(0, len(str)):
        for j in range(97, 123):
            if ord(str[i]) == i:
                str[i] = str(ord(str[i]) - 32) 
