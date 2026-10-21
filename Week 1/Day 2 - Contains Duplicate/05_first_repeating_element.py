# ============================================================
# Day 2 - VARIANT: First Repeating Element  (GeeksforGeeks)
# ============================================================
# The question:
#   Find the first element (lowest index) that occurs MORE than once
#   in the array. Return its position as a 1-based index. If nothing
#   repeats, return -1.
#
#   Example: [1, 5, 3, 4, 3, 5, 6] -> 2
#            5 is at position 2 and repeats later. 3 also repeats but
#            its first appearance (position 3) is later than 5's.
#
# The big idea:
#   Pass 1: count how many times each number appears (our own dict).
#   Pass 2: walk from the left - the first number with count > 1 wins.
# ============================================================


def first_repeated_brute(arr):
    # Brute force: for each element, scan the rest for a copy.
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return i + 1
    return -1


def first_repeated(arr):
    counts = {}
    for num in arr:
        counts[num] = counts.get(num, 0) + 1   # hand-made frequency dict

    for i in range(len(arr)):
        if counts[arr[i]] > 1:
            return i + 1                       # 1-based position

    return -1


if __name__ == "__main__":
    print(first_repeated([1, 5, 3, 4, 3, 5, 6]))   # 2
    print(first_repeated([1, 2, 3, 4]))            # -1
