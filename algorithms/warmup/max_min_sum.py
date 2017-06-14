def max_min_sum(arr):
    """Given five positive integers, find the minimum and maximum values that can
    be calculated by summing exactly four of the five integers. Then print the
    respective minimum and maximum values as a single line of two space-separated
    long integers.
    """

    sums = []
    a = 0

    while a < len(arr):
        temp = sum(arr) - arr[a]
        sums.append(temp)
        a += 1

    sums.sort()
    final = str(sums[0]) + ' ' + str(sums[-1])
    return final

arr = map(int, raw_input().strip().split(' '))
print max_min_sum(arr)
