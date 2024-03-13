#!/usr/bin/python3

for i in range(97, 123):
    if "q" and "e" not in chr(i):
        print("{}".format(chr(i)), end="")
