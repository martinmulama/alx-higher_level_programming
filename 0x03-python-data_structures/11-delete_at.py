#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx < 0:
        return (my_list)

    length = len(my_list)

    if idx > length - 1:
        return (my_list)

    brand_new_list = []

    for i in range(len(my_list)):
        if i != idx:
            brand_new_list.append(my_list[i])

    my_list.clear()
    my_list.extend(brand_new_list)

    return (my_list)
