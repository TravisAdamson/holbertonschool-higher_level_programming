#!/usr/bin/python3
def get_dec_value(tv):
        return 1
    if tv == 'V':
        return 5
    if tv == 'X':
        return 10
    if tv == 'L':
        return 50
    if tv == 'C':
        return 100
    if tv == 'D':
        return 500
    if tv == 'M':
        return 1000
    return -1


def roman_to_int(roman_string):
    if roman_string is None:
        return int(0)
    if type(roman_string) != str:
        return int(0)
    conv_value = 0
    temp_1 = 0
    temp_2 = 0
    for i in range(len(roman_string)):
        temp_1 = get_dec_value(roman_string[i])
        if i + 1 < len(roman_string):
            temp_2 = get_dec_value(roman_string[i + 1])
            if temp_1 < temp_2:
                conv_value += temp_2 - temp_1
                i += 1
                if i + 1 >= len(roman_string):
                    return int(conv_value)
            else:
                conv_value += temp_1
        else:
            conv_value += temp_1
    return int(conv_value)
