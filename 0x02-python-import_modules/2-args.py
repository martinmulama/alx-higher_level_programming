#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    arg_count = len(args)

    if arg_count == 0:
        print(arg_count, "arguments.")
    elif arg_count == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(arg_count))
    for i in range(arg_count):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
