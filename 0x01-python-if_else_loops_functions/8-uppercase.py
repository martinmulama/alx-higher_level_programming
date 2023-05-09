#!/usr/bin/python3
def uppercase(s):
    for c in s:
        if ord(c) >= ord('a') and ord(c) <= ord('z'):
            c = chr(ord(c) - 32)
        print("{:s}".format(c), end="")
    print()
