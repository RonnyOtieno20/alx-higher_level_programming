#!/usr/bin/python3

for i in range(1, 99):
    if (i // 10) < (i % 10):
        if i == 89:
            print("89")
        else:
            print("{:02}".format(i), end=", ")
