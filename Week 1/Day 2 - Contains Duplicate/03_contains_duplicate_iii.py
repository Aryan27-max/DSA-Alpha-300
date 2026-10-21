# ============================================================
# Day 2 - VARIANT: Contains Duplicate III  (LeetCode 220)
# ============================================================
# The question:
#   Return True if there are indexes i != j such that
#     |i - j| <= indexDiff     (close in position)
#     |nums[i] - nums[j]| <= valueDiff   (close in value)
#
#   Example: nums = [1, 2, 3, 1], indexDiff = 3, valueDiff = 0 -> True
#            nums = [1, 5, 9, 1, 5, 9], indexDiff = 2, valueDiff = 3 -> False
#
# The big idea (buckets):
#   Put numbers into buckets of width (valueDiff + 1).
#   e.g. valueDiff = 3 -> bucket width 4 -> 0..3 go in bucket 0, 4..7 in bucket 1...
#   - Two numbers in the SAME bucket are definitely within valueDiff.
#   - Numbers in NEIGHBOUR buckets might be - so we check them directly.
#   - Only keep the last indexDiff numbers in the buckets (a sliding window).
#   Each bucket holds at most one number (if two land together we already return True).
# ============================================================


def contains_nearby_almost_duplicate_brute(nums, indexDiff, valueDiff):
    # Brute force: for each i, compare with the next indexDiff elements.
    n = len(nums)
    for i in range(n):
        j = i + 1
        while j < n and j - i <= indexDiff:
            if abs(nums[i] - nums[j]) <= valueDiff:
                return True
            j += 1
    return False


def contains_nearby_almost_duplicate(nums, indexDiff, valueDiff):
    width = valueDiff + 1
    buckets = {}                            # bucket id -> the number sitting in it

    for i in range(len(nums)):
        num = nums[i]
        b = num // width                    # Python's // floors, so negatives work too

        if b in buckets:
            return True                     # same bucket = close enough in value

        if (b - 1) in buckets and abs(num - buckets[b - 1]) <= valueDiff:
            return True                     # left neighbour bucket is close enough
        if (b + 1) in buckets and abs(num - buckets[b + 1]) <= valueDiff:
            return True                     # right neighbour bucket is close enough

        buckets[b] = num

        # keep the window size at indexDiff: drop the number that just fell out
        if i >= indexDiff:
            old = nums[i - indexDiff]
            del buckets[old // width]

    return False


if __name__ == "__main__":
    print(contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0))         # True
    print(contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3))   # False
    print(contains_nearby_almost_duplicate([-3, 3], 2, 4))              # False
