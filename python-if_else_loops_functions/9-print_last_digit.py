#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        alt_num = number * -1
        last = (alt_num % 10)
        if last >= 0:
            print("{}".format(last), end="")
            return last
        else:
            last = last * -1
            print("{}".format(last), end="")
            return last
    else:
        last = (number % 10)
        print("{}".format(last), end="")
        return last
