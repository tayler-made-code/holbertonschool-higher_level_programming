#!/usr/bin/python3
def search_replace(my_list, search, replace):
    santas_list = my_list[:]
    for i in range(len(santas_list)):
        if santas_list[i] == search:
            santas_list[i] = replace
    return santas_list
