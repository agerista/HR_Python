def percentages(n, arr):
    """Given an array of integers, calculate which fraction of its elements are
    positive, which fraction of its elements are negative, and which fraction of
    its elements are zeroes, respectively. Print the decimal value of each fraction
    on a new line.
    """

    positive = 0
    negative = 0
    zero = 0

    for a in arr:

        if a > 0:
            positive += 1
        elif a == 0:
            zero += 1
        else:
            negative += 1

    positive = float(positive)/n
    negative = float(negative)/n
    zero = float(zero)/n

    return "{0:.6f}\n{1:.6f}\n{2:.6f}".format(positive, negative, zero)

n = int(raw_input().strip())
arr = map(int, raw_input().strip().split(' '))
print percentages(n, arr)
