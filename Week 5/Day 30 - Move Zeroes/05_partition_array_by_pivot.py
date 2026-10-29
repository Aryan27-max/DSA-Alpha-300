# ============================================================
# Day 30 - VARIANT: Partition Array According to Given Pivot  (LeetCode 2161)
# ============================================================
# The question:
#   Rearrange nums so that:
#     all numbers < pivot come first,
#     then all numbers == pivot,
#     then all numbers > pivot,
#   and the relative order inside the "<" group and the ">" group stays
#   the same as in the input (stable).
#
#   Example: nums = [9,12,5,10,14,3,10], pivot = 10
#            -> [9,5,3,10,10,12,14]
#
# The big idea (partition by a predicate, with two pointers):
#   Stability is what makes in-place hard, so use one result array and
#   fill it from both ends in a single pass:
#     left  pointer reads nums from the START; every "< pivot" goes to
#           result[lo], lo += 1      -> keeps their order
#     right pointer reads nums from the END;   every "> pivot" goes to
#           result[hi], hi -= 1      -> filling from the back keeps their order too
#   Whatever's left between lo and hi is filled with pivot.
# ============================================================


def pivot_array_brute(nums, pivot):
    # Three separate lists glued together.
    less, equal, greater = [], [], []
    for x in nums:
        if x < pivot:
            less.append(x)
        elif x == pivot:
            equal.append(x)
        else:
            greater.append(x)
    return less + equal + greater


def pivot_array(nums, pivot):
    n = len(nums)
    result = [pivot] * n            # everything not overwritten will be the pivot
    lo, hi = 0, n - 1

    for i in range(n):
        if nums[i] < pivot:
            result[lo] = nums[i]            # front, in reading order
            lo += 1
        j = n - 1 - i
        if nums[j] > pivot:
            result[hi] = nums[j]            # back, in reverse reading order
            hi -= 1

    return result


if __name__ == "__main__":
    print(pivot_array([9, 12, 5, 10, 14, 3, 10], 10))   # [9, 5, 3, 10, 10, 12, 14]
    print(pivot_array([-3, 4, 3, 2], 2))                # [-3, 2, 4, 3]
