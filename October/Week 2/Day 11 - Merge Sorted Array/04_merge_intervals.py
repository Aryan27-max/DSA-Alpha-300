# ============================================================
# Day 11 - VARIANT: Merge Intervals  (LeetCode 56)
# ============================================================
# The question:
#   Given a list of intervals [start, end], merge every group that
#   overlaps and return the non-overlapping result.
#
#   Example: [[1,3],[2,6],[8,10],[15,18]] -> [[1,6],[8,10],[15,18]]
#            [[1,4],[4,5]] -> [[1,5]]   (touching counts as overlapping)
#
# The big idea:
#   1. Sort intervals by start (our OWN merge sort - sorted() is banned).
#   2. Walk through them. If the current one starts before (or exactly when)
#      the last merged one ends, stretch the last one's end.
#      Otherwise start a new merged interval.
# ============================================================


def merge_sort_by_start(arr):
    # Our own merge sort that compares intervals by their start value.
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_by_start(arr[:mid])
    right = merge_sort_by_start(arr[mid:])
    out, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i][0] <= right[j][0]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    while i < len(left):
        out.append(left[i]); i += 1
    while j < len(right):
        out.append(right[j]); j += 1
    return out


def merge_brute(intervals):
    # Brute force: keep merging any overlapping pair until nothing changes. O(n^3) worst.
    items = []
    for a, b in intervals:
        items.append([a, b])
    changed = True
    while changed:
        changed = False
        for i in range(len(items)):
            for j in range(i + 1, len(items)):
                a, b = items[i], items[j]
                if a[0] <= b[1] and b[0] <= a[1]:       # they overlap
                    items[i] = [min(a[0], b[0]), max(a[1], b[1])]
                    items.pop(j)
                    changed = True
                    break
            if changed:
                break
    return merge_sort_by_start(items)


def merge(intervals):
    intervals = merge_sort_by_start(intervals)
    merged = []

    for start, end in intervals:
        if len(merged) > 0 and start <= merged[-1][1]:
            # overlaps the last one: just stretch its end if needed
            if end > merged[-1][1]:
                merged[-1][1] = end
        else:
            merged.append([start, end])     # gap -> brand new interval

    return merged


if __name__ == "__main__":
    print(merge([[1, 3], [2, 6], [8, 10], [15, 18]]))   # [[1, 6], [8, 10], [15, 18]]
    print(merge([[1, 4], [4, 5]]))                      # [[1, 5]]
    print(merge([[4, 7], [1, 4]]))                      # [[1, 7]]
    print(merge_brute([[1, 3], [2, 6], [8, 10]]))       # [[1, 6], [8, 10]]
