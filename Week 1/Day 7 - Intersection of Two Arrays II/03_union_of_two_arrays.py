# ============================================================
# Day 7 - VARIANT: Union of Two Arrays with Duplicates  (GeeksforGeeks)
# ============================================================
# The question:
#   Two arrays that may contain duplicates. Find the union: every
#   DISTINCT element that appears in either array.
#   GFG asks for the count of distinct elements - we return both the
#   list and its size.
#
#   Example: a = [1, 2, 3, 4, 5], b = [1, 2, 3] -> union [1, 2, 3, 4, 5], count 5
#            a = [85, 25, 1, 32, 54, 6], b = [85, 2] -> count 7
#
# The big idea:
#   Throw everything from both arrays into one set we fill by hand.
#   We also keep a list so the answer keeps the order we first saw things.
# ============================================================


def union_brute(a, b):
    # Brute force: before adding, scan the result to see if it's already there.
    result = []
    for arr in (a, b):
        for x in arr:
            found = False
            for r in result:
                if r == x:
                    found = True
                    break
            if not found:
                result.append(x)
    return result, len(result)


def union(a, b):
    seen = set()
    result = []

    for x in a:
        if x not in seen:
            seen.add(x)
            result.append(x)

    for x in b:
        if x not in seen:           # only things a didn't already give us
            seen.add(x)
            result.append(x)

    return result, len(result)


if __name__ == "__main__":
    print(union([1, 2, 3, 4, 5], [1, 2, 3]))         # ([1, 2, 3, 4, 5], 5)
    print(union([85, 25, 1, 32, 54, 6], [85, 2]))    # (..., 7)
    print(union([1, 2, 1, 1, 2], [2, 2, 1, 2, 1]))   # ([1, 2], 2)
