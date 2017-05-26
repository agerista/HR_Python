def capitalize(string):

    l = string.split(" ")
    a = [i.capitalize() for i in l]
    return " ".join(a)
