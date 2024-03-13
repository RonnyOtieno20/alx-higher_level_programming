#!/usr/bin/python3


def fizzbuzz():
    """
    function that prints the numbers from 1 to 100 separated by a space.
    for numbers which are multiple of both 3 and 5, print FizzBuzz
    for numbers which are multiple of 3, print Fizz
    for numbers which are multiple of 5, print Buzz
    """


for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz", end=" ")
    elif i % 3 == 0:
        print("Fizz", end=" ")
    elif i % 5 == 0:
        print("Buzz", end=" ")
    else:
        print(i, end=" ")

if __name__ == "__main__":
    fizzbuzz()
