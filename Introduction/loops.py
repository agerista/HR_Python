def squared(n):

    i = 0

    while i < n:

        print i ** 2
        i += 1


if __name__ == '__main__':
    n = int(raw_input())
    squared(n)
