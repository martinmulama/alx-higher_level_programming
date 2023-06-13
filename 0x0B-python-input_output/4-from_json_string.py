#!/usr/bin/python3
# 3-to_json.py
# Martin <martin.mulama@yahoo.com>
""" Module returns an object (Python data structure) represented by a JSON string """

import json

def from_json_string(my_str):
    """ returns object represented by a json string """
    return json.loads(my_str)
