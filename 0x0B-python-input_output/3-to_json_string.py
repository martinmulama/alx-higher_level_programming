#!/usr/bin/python3
# 3-to_json.py
# Martin <martin.mulama@yahoo.com>
""" Module thst returns a json string rep of anobject """

import json

def to_json_string(my_obj):
    """ returns json string rep of an aobject """
    return json.dumps(my_obj)
