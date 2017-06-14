def timeConversion(s):
    """Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.

    Note: Midnight is 12:00:00AM on a 12-hour clock, and 00:00:00 on a 24-hour clock.
    Noon is 12:00:00PM on a 12-hour clock, and 12:00:00 on a 24-hour clock.
    """

    if s[-2] == 'P' and int(s[:2]) < 12:
        hour = int(s[:2]) + 12
        s = str(hour) + s[2:-2]

    elif s[:2] == "12" and s[-2] == 'A':
        s = "00" + s[2:-2]

    else:
        s = s[:-2]

    return s

s = raw_input().strip()
result = timeConversion(s)
print(result)
