# ============================================================
# Day 12 - VARIANT: Height Checker  (LeetCode 1051)
# ============================================================
# The question:
#   Students should stand in non-decreasing order of height. Return how
#   many positions have the WRONG student compared to the sorted order.
#
#   Example: [1,1,4,2,1,3] -> 3
#            sorted is [1,1,1,2,3,4]; positions 2, 4, 5 differ.
#
# The big idea (counting sort - heights are only 1..100):
#   We need the sorted order but can't call sorted().
#   Count how many students have each height (a 101-slot list).
#   Then walk heights from small to big - that "expected" stream is the
#   sorted order - and compare against the real line as we go. O(n + 100).
# ============================================================


def height_checker_brute(heights):
    # Brute force: insertion sort a copy (O(n^2)), then compare.
    expected = []
    for h in heights:
        expected.append(h)
    for i in range(1, len(expected)):
        cur = expected[i]
        j = i - 1
        while j >= 0 and expected[j] > cur:
            expected[j + 1] = expected[j]
            j -= 1
        expected[j + 1] = cur
    wrong = 0
    for i in range(len(heights)):
        if heights[i] != expected[i]:
            wrong += 1
    return wrong


def height_checker(heights):
    count = [0] * 101
    for h in heights:
        count[h] += 1                   # how many students of each height

    wrong = 0
    h = 1                               # the next height in sorted order
    for i in range(len(heights)):
        while count[h] == 0:
            h += 1                      # skip heights nobody has
        if heights[i] != h:
            wrong += 1                  # this person is in the wrong spot
        count[h] -= 1                   # one student of height h is "placed"

    return wrong


if __name__ == "__main__":
    print(height_checker([1, 1, 4, 2, 1, 3]))          # 3
    print(height_checker([5, 1, 2, 3, 4]))             # 5
    print(height_checker([1, 2, 3, 4, 5]))             # 0
    print(height_checker_brute([1, 1, 4, 2, 1, 3]))    # 3
