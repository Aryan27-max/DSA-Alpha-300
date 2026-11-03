# ============================================================
# Day 7 - VARIANT: Intersection of Three Sorted Arrays  (LeetCode 1213 - Premium)
# ============================================================
# The question:
#   Three arrays, each sorted in strictly increasing order.
#   Return the numbers that appear in ALL three, in sorted order.
#
#   Example: [1,2,3,4,5], [1,2,5,7,9], [1,3,4,5,8] -> [1, 5]
#
# The big idea (three pointers):
#   Since they're sorted, keep one pointer per array.
#   - All three equal -> it's in the answer, move all three.
#   - Otherwise the smallest value can't be in the answer,
#     so move the pointer(s) pointing at the smallest value.
#   No dict needed, O(1) extra space.
# ============================================================


def arrays_intersection_brute(arr1, arr2, arr3):
    # Count version: count every number across all three arrays.
    # Arrays are strictly increasing, so a count of 3 means "in all three".
    counts = {}
    for arr in (arr1, arr2, arr3):
        for x in arr:
            counts[x] = counts.get(x, 0) + 1
    result = []
    for x in arr1:                  # walk arr1 to keep sorted order
        if counts[x] == 3:
            result.append(x)
    return result


def arrays_intersection(arr1, arr2, arr3):
    i = j = k = 0
    result = []

    while i < len(arr1) and j < len(arr2) and k < len(arr3):
        a, b, c = arr1[i], arr2[j], arr3[k]

        if a == b == c:
            result.append(a)
            i += 1
            j += 1
            k += 1
        else:
            smallest = min(a, b, c)
            # move whichever pointers are sitting on the smallest value
            if a == smallest:
                i += 1
            if b == smallest:
                j += 1
            if c == smallest:
                k += 1

    return result


if __name__ == "__main__":
    print(arrays_intersection([1, 2, 3, 4, 5], [1, 2, 5, 7, 9], [1, 3, 4, 5, 8]))  # [1, 5]
    print(arrays_intersection([197, 418, 523, 876, 1356],
                              [501, 880, 1593, 1710, 1870],
                              [521, 682, 1337, 1395, 1764]))                       # []
