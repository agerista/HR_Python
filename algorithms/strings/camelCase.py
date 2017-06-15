def camelCase(s):

    words = []
    count = 0
    last = 0

    for char in s:

        if char.isupper() is True:
            words.append(s[last:count])
            last = count

        count += 1

    words.append(s[last:])
    return len(words)

s = raw_input().strip()
print camelCase(s)
