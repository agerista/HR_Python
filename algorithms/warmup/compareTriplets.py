def solve(a0, a1, a2, b0, b1, b2):
    """Alice and Bob each created one problem for HackerRank. A reviewer rates
    the two challenges, awarding points on a scale from 1 to 100 for three categories:
    problem clarity, originality, and difficulty.

    Given A and B, can you compare the two challenges and print their respective
    comparison points?
    """

    alice = ((1 if a0 > b0 else 0) + (1 if a1 > b1 else 0) + (1 if a2 > b2 else 0))
    bob = ((1 if a0 < b0 else 0) + (1 if a1 < b1 else 0) + (1 if a2 < b2 else 0))

    return alice, bob

a0, a1, a2 = raw_input().strip().split(' ')
a0, a1, a2 = [int(a0), int(a1), int(a2)]
b0, b1, b2 = raw_input().strip().split(' ')
b0, b1, b2 = [int(b0), int(b1), int(b2)]
result = solve(a0, a1, a2, b0, b1, b2)
print " ".join(map(str, result))
