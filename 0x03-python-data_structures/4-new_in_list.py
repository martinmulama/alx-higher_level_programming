#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    range = len(my_list)
    my_list_copy = my_list[:]

    if idx < 0:
        return (my_list_copy)
    if idx > range - 1:
        return (my_list_copy)

    my_list_copy[idx] = element

    return(my_list_copy)
