def make_hash(integer_list):

    my_tuple = tuple(integer_list)
    return hash(my_tuple)

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print make_hash(integer_list)
