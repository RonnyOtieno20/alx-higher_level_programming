#!/usr/bin/python3

def read_file(filename=""):
    
    with open("my_file_0.txt", "r") as filename:
        f = filename.read()
        print(f)
