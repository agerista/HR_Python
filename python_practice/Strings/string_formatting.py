def print_formatted(number):

    width = len(bin(n).replace("0b", ''))
    for i in range(1, n+1):

        d = str(i).rjust(width, " ")
        h = hex(i).replace("0x", "").upper().rjust(width, " ")
        o = oct(i).replace("0", '', 1).rjust(width, " ")
        b = bin(i).replace("0b", "").rjust(width, " ")
        print d, o, h, b

if __name__ == '__main__':
    n = int(raw_input())
    print_formatted(n)
