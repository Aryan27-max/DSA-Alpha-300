# ============================================================
# Day 29 - VARIANT: Maximum Subarray  (LeetCode 53)
# ============================================================
# The question:
#   Find the contiguous subarray with the largest sum (it must contain
#   at least one number) and return that sum.
#
#   Example: [-2,1,-3,4,-1,2,1,-5,4] -> 6   ([4,-1,2,1])
#            [-3,-1,-2] -> -1
#
# The big idea (Kadane's algorithm - a related one-pass pattern):
#   Same shape as the primary: one pass, two running variables.
#     current = best sum of a subarray that ENDS at today's number
#     best    = best sum seen anywhere so far
#   For each number x: either extend the previous run (current + x) or
#   start fresh at x - whichever is bigger. If the run so far is
#   negative, it only drags x down, so start fresh.
#
#   Link to stock prices: the day-to-day price CHANGES form an array;
#   the best single trade is the maximum subarray of those changes.
# ============================================================


def max_sub_array_brute(nums):
    # Brute force: every start, extend and track the best sum.
    best = nums[0]
    for i in range(len(nums)):
        s = 0
        for j in range(i, len(nums)):
            s += nums[j]
            if s > best:
                best = s
    return best


def max_sub_array(nums):
    current = nums[0]
    best = nums[0]

    for i in range(1, len(nums)):
        x = nums[i]
        if current < 0:
            current = x             # the old run only hurts - start fresh
        else:
            current += x            # extend the run
        if current > best:
            best = current

    return best


if __name__ == "__main__":
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))         # 6
    print(max_sub_array([1]))                                     # 1
    print(max_sub_array([5, 4, -1, 7, 8]))                        # 23
    print(max_sub_array([-3, -1, -2]))                            # -1
    print(max_sub_array_brute([-2, 1, -3, 4, -1, 2, 1, -5, 4]))   # 6
