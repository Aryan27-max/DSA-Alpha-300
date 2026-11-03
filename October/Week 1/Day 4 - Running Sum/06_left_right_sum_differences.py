# ============================================================
# Day 4 - VARIANT: Left and Right Sum Differences  (LeetCode 2574)
# ============================================================
# The question:
#   For each index i:
#     leftSum  = sum of everything BEFORE i
#     rightSum = sum of everything AFTER i
#   Return a list of |leftSum - rightSum| for every i.
#
#   Example: [10, 4, 8, 3] -> [15, 1, 11, 22]
#
# The big idea:
#   Get the total once. Walk left to right carrying leftSum.
#   rightSum = total - leftSum - nums[i]. No need for two extra arrays.
# ============================================================


def left_right_difference_brute(nums):
    # Brute force: for each i, add up both sides from scratch.
    n = len(nums)
    result = []
    for i in range(n):
        left = 0
        for j in range(i):
            left += nums[j]
        right = 0
        for j in range(i + 1, n):
            right += nums[j]
        result.append(abs(left - right))
    return result


def left_right_difference(nums):
    total = 0
    for num in nums:
        total += num

    result = []
    left_sum = 0
    for num in nums:
        right_sum = total - left_sum - num      # everything that's not left and not me
        result.append(abs(left_sum - right_sum))
        left_sum += num                         # I become part of the left side now
    return result


if __name__ == "__main__":
    print(left_right_difference([10, 4, 8, 3]))   # [15, 1, 11, 22]
    print(left_right_difference([1]))             # [0]
