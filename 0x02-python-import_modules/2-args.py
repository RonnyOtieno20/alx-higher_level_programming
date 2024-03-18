#!/usr/bin/python3
import sys


def main():
    """
    prints the number of and the list of its arguments.
    """
    if len(sys.argv) == 1:
        print("{} arguments.".format(0))
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv) - 1))
        print("{}: {}".format(1, sys.argv[1]))
    else:
        print("{} arguments:".format(len(sys.argv[1:])))
        i = 1
        for arg in sys.argv[1:]:
            print("{}: {}".format(i, arg))
            i += 1


if __name__ == "__main__":
    main()
