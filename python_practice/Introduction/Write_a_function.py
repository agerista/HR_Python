def is_leap(year):
    """In the Gregorian calendar three criteria must be taken into account to
    identify leap years:

    - The year can be evenly divided by 4, unless;
    - The year can be evenly divided by 100, it is NOT a leap year, unless;
    - The year is also evenly divisible by 400. Then it is a leap year.

    is_leap(2000)
    >>> True
    is_leap(1900)
    >>> False
    is_leap(2001)
    >>> False
    """

    leap = False

    # Write your logic here
    if ((year % 4 == 0) and (year % 100 != 0)) or (year % 400 == 0):

        leap = True

    return leap

################################################################################
if __name__ == "__main__":
    import doctest

    result = doctest.testmod()
    if not result.failed:
        print "\nAll tests passed. Good job!\n"
