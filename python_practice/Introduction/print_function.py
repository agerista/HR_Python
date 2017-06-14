from __future__ import print_function


def print_func(n):

    for i in range(1, n + 1):

        print (i, end='')

################################################################################
if __name__ == '__main__':
    n = int(raw_input())
    print_func(n)
