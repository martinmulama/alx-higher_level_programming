#!/usr/bin/python3
# 7-add_item.py
# Martin <martin.mulama@yahoo.com>
""" Module that adds all arguments to a Python list, and then save them to a file """
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file


def add_arguments_to_list(arguments, filename):
    """ adds all arguments to a Python list, and then save them to a file """
    try:
        data = load_from_json_file(filename)
    except FileNotFoundError:
        data = []

    data.extend(arguments)
    save_to_json_file(data, filename)

arguments = sys.argv[1:]

filename = "add_item.json"

add_arguments_to_list(arguments, filename)
