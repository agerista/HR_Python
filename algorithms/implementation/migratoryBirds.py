def migratoryBirds(n, ar):
    """A flock of  birds is flying across the continent. Each bird has a type,
    and the different types are designated by the ID numbers 1, 2, 3, 4, and 5.

    Given an array of n integers where each integer describes the type of a bird
    in the flock, find and print the type number of the most common bird. If two
    or more types of birds are equally common, choose the type with the smallest
    ID number.
    """

    birds = {}

    for a in ar:

        if birds.get(a, 0):
            birds[a] += 1

        else:
            birds[a] = 1

    return max(birds, key=birds.get)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = migratoryBirds(n, ar)
print(result)
