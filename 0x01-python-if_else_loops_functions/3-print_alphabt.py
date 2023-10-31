#!/usr/bin/python3
for _ in range(97, 123):
    if chr(_) == 'q' or chr(_) == 'e':
        continue
    print("{}".format(chr(_)), end="")
