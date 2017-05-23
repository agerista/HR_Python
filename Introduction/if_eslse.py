def is_weird(n):

    if n % 2 != 0:
        print "Weird"

    elif n % 2 == 0 and n >= 2 and n <= 5:
        print "Not Weird"

    elif n % 2 == 0 and n >= 6 and n <= 20:
        print "Weird"

    else:
        print "Not Weird"


if __name__ == '__main__':
    n = int(raw_input())
    is_weird(n)
