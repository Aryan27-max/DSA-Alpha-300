# ============================================================
# Day 14 - VARIANT: Contains Duplicate III  (LeetCode 220 - Hard)
# ============================================================
# The question:
#   Return True if there are indexes i != j with
#     |i - j| <= indexDiff   AND   |nums[i] - nums[j]| <= valueDiff.
#
#   Example: [1,2,3,1], indexDiff = 3, valueDiff = 0 -> True
#            [1,5,9,1,5,9], indexDiff = 2, valueDiff = 3 -> False
#
# The big idea (bucket-sort window):
#   Today's primary kept a window SET of exact values. Here "close in
#   value" replaces "equal", so we put values in buckets of width
#   valueDiff + 1:
#     - same bucket       -> definitely close enough
#     - neighbour bucket  -> maybe; check the actual difference
#   The dict of buckets holds only the last indexDiff values, exactly
#   like the primary's window set. Each bucket holds at most one value
#   (a second one would already have returned True).
# ============================================================


def contains_nearby_almost_duplicate_brute(nums, index_diff, value_diff):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, min(i + index_diff + 1, n)):
            if abs(nums[i] - nums[j]) <= value_diff:
                return True
    return False


def contains_nearby_almost_duplicate(nums, index_diff, value_diff):
    width = value_diff + 1
    buckets = {}                            # bucket id -> value currently in the window

    for i in range(len(nums)):
        x = nums[i]
        b = x // width                      # floor division handles negatives correctly

        if b in buckets:
            return True
        if b - 1 in buckets and x - buckets[b - 1] <= value_diff:
            return True
        if b + 1 in buckets and buckets[b + 1] - x <= value_diff:
            return True

        buckets[b] = x

        if i >= index_diff:                 # keep only the last index_diff values
            del buckets[nums[i - index_diff] // width]

    return False


if __name__ == "__main__":
    print(contains_nearby_almost_duplicate([1, 2, 3, 1], 3, 0))         # True
    print(contains_nearby_almost_duplicate([1, 5, 9, 1, 5, 9], 2, 3))   # False
    print(contains_nearby_almost_duplicate([-3, 3], 2, 4))              # False
    print(contains_nearby_almost_duplicate([8, 1, 6, 3], 2, 2))         # True (1 and 3)
