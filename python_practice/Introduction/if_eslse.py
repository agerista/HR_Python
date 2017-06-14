def is_weird(n):
    """Given an integer, , perform the following conditional actions:

    - If  is odd, print Weird
    - If  is even and in the inclusive range of  to , print Not Weird
    - If  is even and in the inclusive range of  to , print Weird
    - If  is even and greater than , print Not Weird

    is_weird(3)
    >>> Weird

    is_weird(24)
    >>> Not Weird
    """
    if n % 2 != 0:

        print "Weird"

    elif n % 2 == 0 and n >= 2 and n <= 5:

        print "Not Weird"

    elif n % 2 == 0 and n >= 6 and n <= 20:

        print "Weird"

    else:

        print "Not Weird"


if __name__ == '__main__':
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nALL TESTS PASSED. GOOD WORK!\n"
