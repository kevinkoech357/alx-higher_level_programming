#!/usr/bin/python3
def uppercase(str):
    transform = ""
    for c in str:
        if ord('a') <= ord(c) <= ord('z'):
            transform += chr(ord(c) - 32)
        else:
            transform += c
    print(transform + "\n")
