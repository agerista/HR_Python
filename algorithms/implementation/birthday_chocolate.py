def solve(n, s, d, m):
    """
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
