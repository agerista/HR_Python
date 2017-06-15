def diagonals(n, a):
    """Given a square matrix of size n x n, calculate the absolute difference between
    the sums of its diagonals.
    """

    primary = 0
    secondary = 0
    i = 0
    j = n - 1

    while i < n:

        primary += a[i][i]
        secondary += a[i][j]
        i += 1
        j -= 1

    return abs(primary - secondary)

n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int, raw_input().strip().split(' '))
    a.append(a_temp)
print diagonals(n, a)
