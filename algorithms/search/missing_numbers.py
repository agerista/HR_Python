def missing_numbers(a, b):

    a.sort()
    b.sort()
    i = 0
    j = 0
    missing = []

    while i <= len(a) - 1 and j <= len(b) - 1:
        if a[i] != b[j]:
            missing.append(b[j])
            j += 1

        else:
            i += 1
            j += 1

    return " ".join(missing)

n = int(raw_input().strip())
a = map(str, raw_input().split())
m = int(raw_input().strip())
b = map(str, raw_input().split())
print missing_numbers(a, b)
