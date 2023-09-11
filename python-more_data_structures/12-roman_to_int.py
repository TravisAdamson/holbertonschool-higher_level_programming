#!/usr/bin/python3
def get_dec_value(tv):
    if tv == 'I':
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
    flag = 0
    set_I = ('V', 'X')
    set_X = ('L', 'C')
    set_C = ('D', 'M')
    for i in range(len(roman_string)):
        if roman_string[i] == 'I' and i + 1 < len(roman_string):
            if roman_string[i + 1] in set_I:
                flag = 1
        if roman_string[i] == 'X' and i + 1 < len(roman_string):
            if roman_string[i + 1] in set_X:
                flag = 1
        if roman_string[i] == 'C' and i + 1 < len(roman_string):
            if roman_string[i + 1] in set_C:
                flag = 1
        temp_1 = get_dec_value(roman_string[i])
        if temp_1 == -1:
            return 0
        if flag = 1:
            temp_2 = get_dec_value(roman_string[i + 1])
            if temp_2 == -1:
                return 0
            if temp_1 < temp_2:

                conv_value += temp_2 - temp_1
                i += 1
                if i + 1 >= len(roman_string):
                    return int(conv_value)
            else:
                conv_value += temp_1
        else:
            conv_value += temp_1
        flag = 0
    return int(conv_value)
