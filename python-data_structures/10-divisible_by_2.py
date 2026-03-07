#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    """
    Returns a list of True/False indicating if elements
    in my_list are divisible by 2.
    """
    result = []
    for number in my_list:
        result.append(number % 2 == 0)
    return result
