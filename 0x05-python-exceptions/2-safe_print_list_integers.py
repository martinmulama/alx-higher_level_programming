#!/usr/bin/puthon3
def safe_print_list_integers(my_list=[], x=0):
    count = 0
    try:
        for i, element in enumerate(my_list):
            try:
                print("{:d}".format(int(element)), end=' ')
                count += 1
                if count == x:
                    break
            except ValueError:
                pass
    except TypeError:
        pass
    finally:
        print()
        if count < x:
            print("{:d}".format(int(element)), end=' ')
            raise IndexError("out of range")
        return count
