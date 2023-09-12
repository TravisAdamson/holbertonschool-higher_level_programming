#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):
    list_div = 0
    new_list = []
    for i in range(list_length):
        try:
            list_div = my_list_1[i] / my_list_2[i]
        except ZeroDivisionError as ze:
            print("division by 0")
            list_div = 0
        except IndexError as ind:
            print("out of range")
            list_div = 0
        except TypeError as typ:
            print("wrong type")
            list_div = 0
        finally:
            new_list.append(list_div)
    return new_list
