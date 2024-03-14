#!/usr/bin/python3

import sys


def main():
    """
        prints the result of the addition of all command line arguments
    """
    total = 0
    if len(sys.argv) == 1:
        print("{}".format(0))

    else:
        for arg in sys.argv[1:]:
            num = int(arg)
            total += num

        print("{:d}".format(total))


if __name__ == "__main__":
    main()
