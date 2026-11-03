# ============================================================
# Day 11 - VARIANT: Insert Interval  (LeetCode 57)
# ============================================================
# The question:
#   intervals is sorted by start and has no overlaps. Insert newInterval
#   so the list stays sorted with no overlaps (merge if needed).
#
#   Example: intervals = [[1,3],[6,9]], newInterval = [2,5] -> [[1,5],[6,9]]
#
# The big idea (three phases, one pass - already sorted, so no sorting!):
#   1. Copy every interval that ends BEFORE newInterval starts.
#   2. Every interval that overlaps newInterval gets swallowed into it
#      (take the smaller start and the bigger end).
#   3. Add the (grown) newInterval, then copy everything after it.
# ============================================================


def insert_brute(intervals, new_interval):
    # Brute force: add it to the end, then run full Merge Intervals (with a sort).
    items = []
    for a, b in intervals:
        items.append([a, b])
    items.append([new_interval[0], new_interval[1]])
    # simple insertion sort by start (no sorted())
    for i in range(1, len(items)):
        cur = items[i]
        j = i - 1
        while j >= 0 and items[j][0] > cur[0]:
            items[j + 1] = items[j]
            j -= 1
        items[j + 1] = cur
    merged = []
    for s, e in items:
        if merged and s <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], e)
        else:
            merged.append([s, e])
    return merged


def insert(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    start, end = new_interval

    # Phase 1: everything completely to the left
    while i < n and intervals[i][1] < start:
        result.append(intervals[i])
        i += 1

    # Phase 2: swallow everything that overlaps
    while i < n and intervals[i][0] <= end:
        start = min(start, intervals[i][0])
        end = max(end, intervals[i][1])
        i += 1
    result.append([start, end])

    # Phase 3: everything completely to the right
    while i < n:
        result.append(intervals[i])
        i += 1

    return result


if __name__ == "__main__":
    print(insert([[1, 3], [6, 9]], [2, 5]))                              # [[1, 5], [6, 9]]
    print(insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))   # [[1, 2], [3, 10], [12, 16]]
    print(insert([], [5, 7]))                                            # [[5, 7]]
