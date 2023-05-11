#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    args = sys.argv[1:]
    args_num = len(args)
    total = 0

    for i in range(args_num):
        total += int(args[i])

    print(total)
