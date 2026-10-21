# ============================================================
# Day 12 - VARIANT: Relative Sort Array  (LeetCode 1122)
# ============================================================
# The question:
#   Sort arr1 so that items follow the order they appear in arr2 (arr2 has
#   distinct values, all of which are in arr1). Numbers not in arr2 go at
#   the end in ascending order.
#
#   Example: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
#            -> [2,2,2,1,4,3,3,9,6,7,19]
#
# The big idea (frequency dict + counting):
#   1. Count every number in arr1 with our own dict.
#   2. Walk arr2: write each number as many times as it was counted, then
#      remove it from the dict.
#   3. What's left wasn't in arr2. Values are 0..1000, so walk 0..1000 in
#      order and write any leftovers (counting sort - no sorted()).
# ============================================================


def relative_sort_brute(arr1, arr2):
    # Brute force: for each value in arr2, scan arr1 to collect it.
    # Then insertion-sort whatever is left.
    result = []
    used = [False] * len(arr1)
    for v in arr2:
        for i in range(len(arr1)):
            if not used[i] and arr1[i] == v:
                result.append(v)
                used[i] = True
    rest = []
    for i in range(len(arr1)):
        if not used[i]:
            rest.append(arr1[i])
    for i in range(1, len(rest)):
        cur, j = rest[i], i - 1
        while j >= 0 and rest[j] > cur:
            rest[j + 1] = rest[j]
            j -= 1
        rest[j + 1] = cur
    return result + rest


def relative_sort_array(arr1, arr2):
    counts = {}
    for x in arr1:
        counts[x] = counts.get(x, 0) + 1

    result = []
    for v in arr2:                          # arr2's order comes first
        for _ in range(counts[v]):
            result.append(v)
        del counts[v]                       # done with this value

    for v in range(1001):                   # leftovers in ascending order
        if v in counts:
            for _ in range(counts[v]):
                result.append(v)

    return result


if __name__ == "__main__":
    print(relative_sort_array([2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19], [2, 1, 4, 3, 9, 6]))
    # [2, 2, 2, 1, 4, 3, 3, 9, 6, 7, 19]
    print(relative_sort_array([28, 6, 22, 8, 44, 17], [22, 28, 8, 6]))
    # [22, 28, 8, 6, 17, 44]
