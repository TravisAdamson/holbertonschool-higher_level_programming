#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    new_list = []
    if my_list:
        for i in my_list:
            if my_list[i] >= 0:
                if my_list[i] % 2 is True:
                    new_list.append(True)
                else:
                    new_list.append(False)
            else:
                if abs(my_list[i]) % 2 is True:
                    new_list.append(True)
                else:
                    new_list.append(False)
    else:
        return None
    return new_list
