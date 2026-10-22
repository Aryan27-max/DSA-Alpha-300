# ============================================================
# Day 16 - VARIANT: Unique Number of Occurrences  (LeetCode 1207)
# ============================================================
# The question:
#   Return True if every value in arr appears a DIFFERENT number of times.
#
#   Example: [1,2,2,1,1,3] -> True   (1 appears 3x, 2 appears 2x, 3 appears 1x)
#            [1,2] -> False         (both appear once)
#
# The big idea (build a map, then check the map's values):
#   Pass 1: count each value.
#   Pass 2: walk the counts and check none repeats, using a set.
#   (Same "have I seen this?" idea from Day 2 - just applied to counts.)
# ============================================================


def unique_occurrences_brute(arr):
    # Brute force: build the counts, then compare every pair of counts.
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1
    values = []
    for x in counts:
        values.append(counts[x])
    for i in range(len(values)):
        for j in range(i + 1, len(values)):
            if values[i] == values[j]:
                return False
    return True


def unique_occurrences(arr):
    counts = {}
    for x in arr:
        counts[x] = counts.get(x, 0) + 1

    seen_counts = set()
    for x in counts:
        if counts[x] in seen_counts:
            return False            # two values share the same number of occurrences
        seen_counts.add(counts[x])
    return True


if __name__ == "__main__":
    print(unique_occurrences([1, 2, 2, 1, 1, 3]))                      # True
    print(unique_occurrences([1, 2]))                                  # False
    print(unique_occurrences([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0]))      # True
