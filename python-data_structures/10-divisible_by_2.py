#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    for i in new_list:
        if i % 2 == 1:
            new_list[i] = False
        else:
            new_list[i] = True
    return new_list
