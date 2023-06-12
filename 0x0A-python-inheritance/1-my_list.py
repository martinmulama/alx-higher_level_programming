#!/usr/bin/python3

class MyList(list):
    """
    A subclass of list that provides additional methods.

    This class inherits from the built-in list class and adds a
    method to print the list in sorted order.
    """

    def print_sorted(self):
        """
        Print the list in ascending sorted order.

        This method sorts the list in ascending order and prints
        the sorted list.
        """
        sortedlist = sorted(self)
        print(sorted_list)
