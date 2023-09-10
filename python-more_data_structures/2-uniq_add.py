#!/usr/bin/python3

def uniq_add(my_list=[]):
    new_list = []
    new_list.append(my_list[0])
    result = my_list[0]
    my_flag = 0
    for i in range(len(my_list)):
        for j in range(len(new_list)):
            if my_list[i] == new_list[j]:
                my_flag = 1
        if my_flag == 0:
            result += my_list[i]
            new_list.append(my_list[i])
        my_flag = 0
    return new_list
