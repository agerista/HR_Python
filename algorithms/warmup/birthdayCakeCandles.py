def birthdayCakeCandles(n, ar):
    """Colleen is turning n years old! Therefore, she has n candles of various
    heights on her cake, and candle i has height heighti. Because the taller candles
    tower over the shorter ones, Colleen can only blow out the tallest candles.

    Given the heighti for each individual candle, find and print the number of
    candles she can successfully blow out.
    """

    tallest = max(ar)
    return ar.count(tallest)

n = int(raw_input().strip())
ar = map(int, raw_input().strip().split(' '))
result = birthdayCakeCandles(n, ar)
print(result)
