#!/usr/bin/puthon3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    max_index = x - 1

    try:
        for i in range(x):
            if i > max_index:
                raise IndexError("Index out of range")

            try:
                element = my_list[i]
                print("{:d}".format(int(element)), end=' ')
                count += 1
            except ValueError:
                pass
    except TypeError:
        pass
    finally:
        print()
        return count
