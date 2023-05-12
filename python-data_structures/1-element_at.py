#!/usr/bin/python3
def element_at(my_list, idx):
    listlen = len(my_list)
    if listlen < idx or idx < 0:
        return None
    else:
        return my_list[idx]

