# ============================================================
# Day 13 - VARIANT: Max Sum Subarray of Size K  (GeeksforGeeks)
# ============================================================
# The question:
#   Find the maximum sum of any contiguous subarray of size k.
#
#   Example: arr = [100, 200, 300, 400], k = 2 -> 700
#            arr = [1, 4, 2, 10, 23, 3, 1, 0, 20], k = 4 -> 39
#
# The big idea:
#   The pure template from today's primary, just without the division.
#   Write it from memory: build the first window, then add one / drop one.
# ============================================================


def max_sum_brute(arr, k):
    # Brute force: sum every window again.
    best = None
    for i in range(len(arr) - k + 1):
        s = 0
        for j in range(i, i + k):
            s += arr[j]
        if best is None or s > best:
            best = s
    return best


def max_sum(arr, k):
    window = 0
    for i in range(k):
        window += arr[i]

    best = window
    for right in range(k, len(arr)):
        window += arr[right] - arr[right - k]   # slide: one in, one out
        if window > best:
            best = window
    return best


if __name__ == "__main__":
    print(max_sum([100, 200, 300, 400], 2))              # 700
    print(max_sum([1, 4, 2, 10, 23, 3, 1, 0, 20], 4))    # 39
    print(max_sum_brute([100, 200, 300, 400], 2))        # 700
