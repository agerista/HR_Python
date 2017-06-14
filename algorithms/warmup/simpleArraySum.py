def simpleArraySum(n, ar):
    """Given an array of  integers, can you find the sum of its elements?"""
    # Complete this function
    sum = 0

    for a in ar:
        sum += a

    return sum

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = simpleArraySum(n, ar)
print(result)
