def aVeryBigSum(n, ar):
    """You are given an array of integers of size N. You need to print the sum of
    the elements in the array, keeping in mind that some of those integers may be
    quite large.
    """

    sum = 0

    for a in ar:

        sum += a

    return sum

n = int(raw_input().strip())
ar = map(long, raw_input().strip().split(' '))
result = aVeryBigSum(n, ar)
print(result)
