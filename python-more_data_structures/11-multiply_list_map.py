#!/usr/bin/python3
def multiply_list_map(my_list=[], number=0):
    late_fees = my_list[:]
    for i in range(len(late_fees)):
        late_fees[i] *= number
    return late_fees
