options = {1: 1, 2: 2, 3: 4}


def davis_staircase(n):

    if n < 0:
        return 0

    if n in options.keys():
        return options[n]

    options[n] = davis_staircase(n-1) + davis_staircase(n-2) + davis_staircase(n-3)
    return options[n]

s = int(raw_input().strip())
for a0 in xrange(s):
    n = int(raw_input().strip())
    print davis_staircase(n)
