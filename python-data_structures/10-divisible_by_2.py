#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list[:]
    j = 0
    for i in new_list:
        if i % 2 == 1:
            new_list[j] = False
            j += 1
        else:
            new_list[j] = True
            j += 1
    return new_list
