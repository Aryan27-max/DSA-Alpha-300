# ============================================================
# Day 20 - VARIANT: Left and Right Sum Differences  (LeetCode 2574)
# ============================================================
# The question:
#   For every index i, return |leftSum[i] - rightSum[i]|, where
#   leftSum is the sum before i and rightSum is the sum after i.
#
#   Example: [10,4,8,3] -> [15,1,11,22]
#
# The big idea:
#   Find Pivot Index asks "where is left == right?". This asks "how far
#   apart are they at every index?". Same machinery: total + running left.
# ============================================================


def left_right_difference_brute(nums):
    # Build separate leftSum and rightSum arrays, then compare. O(n) extra space.
    n = len(nums)
    left = [0] * n
    for i in range(1, n):
        left[i] = left[i - 1] + nums[i - 1]
    right = [0] * n
    for i in range(n - 2, -1, -1):
        right[i] = right[i + 1] + nums[i + 1]
    result = []
    for i in range(n):
        result.append(abs(left[i] - right[i]))
    return result


def left_right_difference(nums):
    total = 0
    for x in nums:
        total += x

    result = []
    left_sum = 0
    for x in nums:
        right_sum = total - left_sum - x
        result.append(abs(left_sum - right_sum))
        left_sum += x
    return result


if __name__ == "__main__":
    print(left_right_difference([10, 4, 8, 3]))         # [15, 1, 11, 22]
    print(left_right_difference([1]))                   # [0]
    print(left_right_difference_brute([10, 4, 8, 3]))   # [15, 1, 11, 22]
