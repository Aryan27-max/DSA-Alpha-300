# ============================================================
# Day 13 - VARIANT: Kids With the Greatest Number of Candies  (LeetCode 1431)
# ============================================================
# The question:
#   candies[i] = how many candies kid i has. If you gave kid i ALL the
#   extraCandies, would they have the most (ties count)? Return a list of
#   True/False, one per kid.
#
#   Example: candies = [2,3,5,1,3], extraCandies = 3
#            -> [True, True, True, False, True]
#
# The big idea (one boolean check per position):
#   Find the current max once (by hand, no max() on the list needed).
#   Then for each kid: candies[i] + extra >= max ?
#   The brute force recomputes the max for every kid.
# ============================================================


def kids_with_candies_brute(candies, extra_candies):
    # For each kid, check against every other kid.
    result = []
    for i in range(len(candies)):
        ok = True
        for j in range(len(candies)):
            if candies[i] + extra_candies < candies[j]:
                ok = False
                break
        result.append(ok)
    return result


def kids_with_candies(candies, extra_candies):
    most = candies[0]
    for c in candies:
        if c > most:
            most = c                    # the current leader's count

    result = []
    for c in candies:
        result.append(c + extra_candies >= most)
    return result


if __name__ == "__main__":
    print(kids_with_candies([2, 3, 5, 1, 3], 3))   # [True, True, True, False, True]
    print(kids_with_candies([4, 2, 1, 1, 2], 1))   # [True, False, False, False, False]
    print(kids_with_candies([12, 1, 12], 10))      # [True, False, True]
