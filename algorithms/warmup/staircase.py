def printer(n):
    """Consider a staircase of size n:

                       #
                      ##
                     ###
                    ####

   Observe that its base and height are both equal to n, and the image is drawn
   using # symbols and spaces. The last line is not preceded by any spaces.

    Write a program that prints a staircase of size n.
    """

    count = 1

    for i in range(n):
        print ('#' * count).rjust(n)
        count += 1

n = int(raw_input().strip())
printer(n)
