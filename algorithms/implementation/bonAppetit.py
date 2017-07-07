def bonAppetit(n, k, b, ar):
    """Anna and Brian order n items at a restaurant, but Anna declines to eat
    any of the kth item (where 0 <= k < n) due to an allergy. When the check comes,
    they decide to split the cost of all the items they shared; however, Brian
    may have forgotten that they didn't split the kth item and accidentally
    charged Anna for it.

    You are given n, k, the cost of each of the n items, and the total amount of
    money that Brian charged Anna for her portion of the bill. If the bill is
    fairly split, print Bon Appetit; otherwise, print the amount of money that
    Brian must refund to Anna.

    bonAppetit(4, 1, [3, 10, 2, 9], 12)
    >>> 5

    bonAppetit(4, 1, [3, 10, 2, 9], 7)
    >>> Bon Appetit
    """

    total = (sum(ar) - ar[k]) / 2

    if total == b:
        return "Bon Appetit"

    else:
        return b - total

n, k = raw_input().strip().split(' ')
n, k = [int(n), int(k)]
ar = map(int, raw_input().strip().split(' '))
b = int(raw_input().strip())
result = bonAppetit(n, k, b, ar)
print(result)
