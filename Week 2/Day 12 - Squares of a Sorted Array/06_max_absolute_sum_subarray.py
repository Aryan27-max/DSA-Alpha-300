# ============================================================
# Day 12 - VARIANT: Maximum Absolute Sum of Any Subarray  (LeetCode 1749)
# ============================================================
# The question:
#   For any (possibly empty) subarray, take the absolute value of its sum.
#   Return the largest such value.
#
#   Example: [1,-3,2,3,-4] -> 5   (subarray [2,3])
#            [2,-5,1,-4,3,-2] -> 8 (subarray [-5,1,-4])
#
# The big idea (where is the extremum? - prefix sums):
#   Any subarray sum = prefix[j] - prefix[i].
#   To make |that| as big as possible, pick the BIGGEST prefix and the
#   SMALLEST prefix (including the empty prefix 0).
#   Answer = max prefix - min prefix. One pass, O(1) space.
#   (Same idea as today's primary: the answer lives at the extremes.)
# ============================================================


def max_absolute_sum_brute(nums):
    # Brute force: every subarray sum.
    best = 0
    n = len(nums)
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += nums[j]
            if abs(s) > best:
                best = abs(s)
    return best


def max_absolute_sum(nums):
    prefix = 0
    highest = 0                 # the empty prefix counts, so start at 0
    lowest = 0

    for x in nums:
        prefix += x
        if prefix > highest:
            highest = prefix
        if prefix < lowest:
            lowest = prefix

    return highest - lowest


def max_absolute_sum_kadane(nums):
    # Another O(n) way: Kadane twice - biggest sum and smallest sum.
    best_max = cur_max = 0
    best_min = cur_min = 0
    for x in nums:
        cur_max = max(x, cur_max + x)
        cur_min = min(x, cur_min + x)
        best_max = max(best_max, cur_max)
        best_min = min(best_min, cur_min)
    return max(best_max, -best_min)


if __name__ == "__main__":
    print(max_absolute_sum([1, -3, 2, 3, -4]))              # 5
    print(max_absolute_sum([2, -5, 1, -4, 3, -2]))          # 8
    print(max_absolute_sum_kadane([2, -5, 1, -4, 3, -2]))   # 8
