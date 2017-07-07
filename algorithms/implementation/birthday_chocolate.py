def solve(n, s, d, m):
    """Lily has a chocolate bar consisting of a row of n squares where each square
    has an integer written on it. She wants to share it with Ron for his birthday,
    which falls on month m and day d. Lily wants to give Ron a piece of chocolate
    only if it contains m consecutive squares whose integers sum to d.

    Given m, d, and the sequence of integers written on each square of Lily's
    chocolate bar, how many different ways can Lily break off a piece of
    chocolate to give to Ron?

    solve(5, [1, 2, 1, 3, 2], 3, 2)
    >>> 2

    solve(6, [1 1 1 1 1 1], 3, 2)
    >>> 0

    solve(1, [4], 4 1)
    >>> 1
    """

    i = 0
    options = 0

    while i < n:

        if sum(s[i: i + m]) == d:
            options += 1

        i += 1

    return options


n = int(raw_input().strip())
s = map(int, raw_input().strip().split(' '))
d, m = raw_input().strip().split(' ')
d, m = [int(d), int(m)]
result = solve(n, s, d, m)
print(result)
