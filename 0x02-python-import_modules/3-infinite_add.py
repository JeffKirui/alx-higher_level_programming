#!/usr/bin/python3
# 3-infinite_add.py

if __name__ == "__main__":
    from sys import argv
    total = 0
    for i in range(len(argv) - 1):
        total += int(argv[i + 1])
    print("{}".format(total))
