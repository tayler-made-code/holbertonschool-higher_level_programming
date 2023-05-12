#!/usr/bin/python3
def element_at(my_list, idx):
    #if idx  is negative return None
    #if idx is greater than my_list return None
    listlen = len(my_list)
    if listlen < idx or listlen < 0:
        return None
    else:
        return my_list[idx]

