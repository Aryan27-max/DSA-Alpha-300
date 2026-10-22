# ============================================================
# Day 21 - VARIANT: Continuous Subarray Sum  (LeetCode 523)
# ============================================================
# The question:
#   Return True if there's a subarray of length AT LEAST 2 whose sum is
#   a multiple of k (0 counts as a multiple of k).
#
#   Example: nums = [23,2,4,6,7], k = 6 -> True   ([2,4] sums to 6)
#            nums = [23,2,6,4,7], k = 13 -> False
#
# The big idea (prefix sums mod k):
#   If two prefix sums leave the SAME remainder when divided by k, the
#   numbers between them add up to a multiple of k.
#   So store: remainder -> the FIRST index where we saw it.
#   When the remainder shows up again at index j, check the gap is >= 2.
#   Start with {0: -1} so a valid subarray starting at index 0 is found.
#   We store the first index (never overwrite) to keep the gap as large
#   as possible.
# ============================================================


def check_subarray_sum_brute(nums, k):
    # Brute force: every subarray of length >= 2.
    n = len(nums)
    for i in range(n):
        s = nums[i]
        for j in range(i + 1, n):
            s += nums[j]
            if s % k == 0:
                return True
    return False


def check_subarray_sum(nums, k):
    first_index = {0: -1}               # remainder -> first index it appeared at
    prefix = 0

    for j in range(len(nums)):
        prefix += nums[j]
        r = prefix % k

        if r in first_index:
            if j - first_index[r] >= 2:
                return True             # the numbers in between sum to a multiple of k
        else:
            first_index[r] = j          # remember only the earliest

    return False


if __name__ == "__main__":
    print(check_subarray_sum([23, 2, 4, 6, 7], 6))    # True
    print(check_subarray_sum([23, 2, 6, 4, 7], 6))    # True (whole array = 42)
    print(check_subarray_sum([23, 2, 6, 4, 7], 13))   # False
    print(check_subarray_sum([5, 0, 0, 0], 3))        # True ([0, 0])
