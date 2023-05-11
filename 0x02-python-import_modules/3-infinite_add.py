#!/usr/bin/python3

if __name__ == "__main__":

    import sys

    argument = len(sys.argv) - 1
    sum_of_args = 0

    for index in range(argument):
        sum_of_args += int(sys.argv[index + 1])
    print("{}".format(sum_of_args))
